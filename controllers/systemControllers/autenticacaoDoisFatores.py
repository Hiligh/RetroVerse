from flask import session, jsonify
from data.conectarBD import conectarBD
import mysql.connector

def ativarAutenticacao():
    if 'user_id' in session:
        user_id = session['user_id']

        conexao = conectarBD()
        try:

            update_autenticacao_query = "UPDATE conta SET Autenticacao = 1 WHERE CodigoConta = %s"
            cursor = conexao.cursor()
            cursor.execute(update_autenticacao_query, (user_id,))
            conexao.commit()
            
            return jsonify({"success": True, "message": "Autenticação ativada com sucesso!"})
        
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return jsonify({"success": False, "message": "Erro ao conectar ao banco de dados"}), 500
        
        finally:
            cursor.close()
            conexao.close()
    else:
        return jsonify({"success": False, "message": "Usuário não autenticado"}), 401
