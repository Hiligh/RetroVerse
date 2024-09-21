from flask import render_template, request
from data.conectarBD import conectarBD

def mostrarCatalogo():
    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)
    
    search_query = request.args.get('search', '')  # Captura a query de busca
    if search_query:
        cursor.execute("SELECT name, header_image FROM jogos WHERE name LIKE %s", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT name, header_image FROM jogos")
    
    jogos = cursor.fetchall()
    cursor.close()
    conexao.close()
    
    return render_template('paginaCatalogo.html', jogos=jogos)