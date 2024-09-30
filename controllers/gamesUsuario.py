from flask import render_template
from data.conectarBD import conectarBD

def gamesUsuario():
    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("SELECT name, capsule_image FROM jogos")
    
    jogos = cursor.fetchall()
    cursor.close()
    conexao.close()

    return render_template('paginaGames.html', jogos=jogos)