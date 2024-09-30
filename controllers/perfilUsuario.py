from flask import redirect, render_template, session, url_for
from data.conectarBD import conectarBD
import mysql.connector

#Mostra o perfil do usuário usando as informações dele salvas na session.
def perfilUsuario():
    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))
    
    user_id = session.get('user_id')

    conexao = conectarBD()

    select_usuario_query = """
    SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1
    """
    
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(select_usuario_query, (user_id,))
        conta = cursor.fetchone()
        
        if conta:
            return render_template('perfilUsuario.html', dadosUser=conta)
        else:
            return redirect(url_for('loginUsuario'))
    
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao conectar ao banco de dados", 500
    
    finally:
        cursor.close()
        conexao.close()
