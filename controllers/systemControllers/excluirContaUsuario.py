from flask import redirect, session, url_for, flash
from data.conectarBD import conectarBD
import mysql.connector

def excluirConta():
    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))

    user_id = session.get('user_id')

    conexao = conectarBD()

    try:
        cursor = conexao.cursor()

        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")

        delete_usuario_query = "DELETE FROM conta WHERE CodigoConta = %s"
        cursor.execute(delete_usuario_query, (user_id,))

        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")

        conexao.commit()

        session.pop('user_id', None)

        flash('Conta excluída com sucesso!', 'success')
        return redirect(url_for('loginUsuario'))

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao excluir conta", 500

    finally:
        cursor.close()
        conexao.close()