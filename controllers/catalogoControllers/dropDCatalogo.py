from flask import session, jsonify, request
from data.conectarBD import conectarBD
import mysql.connector

def dropdownCatalogo():
    if 'user_id' not in session:
        return jsonify({"success": False, "message": "Usuário não autenticado"}), 401

    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    try:
        search_query = request.get_json().get('search_term', '')

        if not search_query:
            return jsonify({"success": False, "message": "Termo de busca vazio"}), 400

        cursor.execute("SELECT name FROM jogos WHERE name LIKE %s LIMIT 10", ('%' + search_query + '%',))

        sugestoes = cursor.fetchall()

        if sugestoes:
            jogos_sugestoes = [jogo['name'] for jogo in sugestoes]
            return jsonify({"success": True, "suggestions": jogos_sugestoes}), 200
        else:
            return jsonify({"success": True, "suggestions": []}), 200

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

        conexao = conectarBD()
        cursor = conexao.cursor()

        log_query = """
        INSERT INTO log (TipoErro, MensagemErro)
        VALUES (%s, %s)
        """
        tipo_erro = "Dropdown"
        mensagem_erro = str(err)

        cursor.execute(log_query, (tipo_erro, mensagem_erro))
        conexao.commit()

        cursor.close()
        conexao.close()

        return jsonify({"success": False, "message": "Erro ao buscar no banco de dados"}), 500

    finally:
        cursor.close()
        conexao.close()