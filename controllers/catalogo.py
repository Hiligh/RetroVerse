from flask import render_template, request
from data.conectarBD import conectarBD

def mostrarCatalogo():
    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    search_query = request.args.get('search', '')

    # Atualizando a consulta para incluir o campo `id`
    if search_query:
        cursor.execute("SELECT CodigoJogo, name, header_image FROM jogos WHERE name LIKE %s", ('%' + search_query + '%',))
    else:
        cursor.execute("SELECT CodigoJogo, name, header_image FROM jogos ORDER BY name")

    jogos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return render_template('paginaCatalogo.html', jogos=jogos)
