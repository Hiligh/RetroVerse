from flask import request, session, jsonify, redirect, flash, url_for
import mysql.connector
from data.conectarBD import conectarBD


def avaliarJogo():

    if 'user_id' not in session:
        flash("Você precisa estar logado para acessar o fórum.", "danger")
        return redirect(url_for('loginUsuario'))

    user_id = session['user_id']

    data = request.get_json()
    jogo_id = data.get('jogo_id')
    rating = data.get('rating')
    print(jogo_id, rating)

    if not jogo_id or not rating:
        return jsonify({'success': False, 'message': 'Dados incompletos'}), 400

    try:
        conexao = conectarBD()
        cursor = conexao.cursor()

        query = """
        INSERT INTO avaliacao_jogo (CodigoJogo, CodigoConta, rating)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE rating = %s
        """
        cursor.execute(query, (jogo_id, user_id, rating, rating))

        conexao.commit()

        cursor.close()
        conexao.close()

        return jsonify({'success': True}), 200
    
    except mysql.connector.Error as err:
        print(f"Erro: {err}")

        conexao = conectarBD()
        cursor = conexao.cursor()

        log_query = """
        INSERT INTO log (TipoErro, MensagemErro)
        VALUES (%s, %s)
        """
        tipo_erro = "Ranking"
        mensagem_erro = str(err)

        cursor.execute(log_query, (tipo_erro, mensagem_erro))
        conexao.commit()

        cursor.close()
        conexao.close()

        return jsonify({'success': False, 'message': 'Erro ao salvar a avaliação.'}), 500