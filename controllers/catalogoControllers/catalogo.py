from flask import render_template, request, redirect, url_for, session
from data.conectarBD import conectarBD
import mysql.connector

def mostrarCatalogo():

    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))
    
    user_id = session.get('user_id')

    conexao = conectarBD()

    select_usuario_query = """
    SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1
    """
    
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(select_usuario_query, (user_id,))
        conta = cursor.fetchone()
        
        if conta:
            pass
        else:
            return redirect(url_for('loginUsuario'))
    
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao conectar ao banco de dados", 500

    search_query = request.args.get('search', '')

    if search_query:
        cursor.execute("SELECT CodigoJogo, name, header_image FROM jogos WHERE name LIKE %s", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT CodigoJogo, name, header_image FROM jogos ORDER BY name")

    jogos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template('paginaCatalogo.html', jogos=jogos, dadosUser=conta)
