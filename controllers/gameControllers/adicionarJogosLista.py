from flask import request, jsonify, session
from data.conectarBD import conectarBD
import mysql.connector

def adicionarJogos():
    if 'user_id' not in session:
        return jsonify({"error": "Usuário não autenticado"}), 401
    
    user_id = session.get('user_id')
    jogo_id = request.json.get('jogo_id')
    lista_nome = request.json.get('lista_nome')

    if not jogo_id or not lista_nome:
        return jsonify({"error": "Dados inválidos"}), 400
    
    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    try:

        query_achar_lista = """
        SELECT l.CodigoLista
        FROM lista l
        INNER JOIN conta c ON l.CodigoConta = c.CodigoConta
        WHERE c.CodigoConta = %s AND l.TipoLista = %s
        LIMIT 1
        """
        cursor.execute(query_achar_lista, (user_id, lista_nome))
        resultado = cursor.fetchone()

        if not resultado:
            return jsonify({"error": "Lista não encontrada para o usuário"}), 404

        codigoLista = resultado['CodigoLista']

        query_adicionar_codigo_lista = """
        INSERT INTO lista_jogos (CodigoLista, CodigoJogo)
        VALUES (%s, %s)
        """
        cursor.execute(query_adicionar_codigo_lista, (codigoLista, jogo_id))
        conexao.commit()
        
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return jsonify({"error": "Erro ao adicionar o jogo na lista"}), 500
    finally:
        cursor.close()
        conexao.close()

    return jsonify({"message": "Jogo adicionado com sucesso!"}), 200