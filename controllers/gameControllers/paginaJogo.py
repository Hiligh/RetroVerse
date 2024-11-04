from flask import render_template, session, redirect, url_for
from data.conectarBD import conectarBD
import mysql.connector

def mostrarJogo(jogo_id):
    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))
    
    user_id = session.get('user_id')

    select_usuario_query = """
    SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1
    """

    try:
        cursor.execute(select_usuario_query, (user_id,))
        conta = cursor.fetchone()
        
        if not conta:
            return redirect(url_for('loginUsuario'))

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao conectar ao banco de dados", 500

    cursor.execute("SELECT * FROM jogos WHERE CodigoJogo = %s", (jogo_id,))
    jogo = cursor.fetchone()

    if not jogo:
        cursor.close()
        conexao.close()
        return "Jogo não encontrado.", 404

    cursor.execute("""
    SELECT AVG(rating) as media_avaliacao, COUNT(rating) as total_avaliacoes
    FROM avaliacao_jogo
    WHERE CodigoJogo = %s
    """, (jogo_id,))
    
    avaliacao = cursor.fetchone()
    media_avaliacao = round(avaliacao['media_avaliacao'], 2) if avaliacao['media_avaliacao'] else 0
    total_avaliacoes = avaliacao['total_avaliacoes']

    cursor.close()
    conexao.close()

    return render_template(
        'paginaJogo.html', 
        jogo=jogo, 
        dadosUser=conta, 
        media_avaliacao=media_avaliacao, 
        total_avaliacoes=total_avaliacoes
    )