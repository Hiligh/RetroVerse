from flask import render_template, session, redirect, url_for
from data.conectarBD import conectarBD
import mysql.connector

def gamesUsuario():
    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)
    
    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))
    
    user_id = session.get('user_id')

    cursor.execute("SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1", (user_id,))
    conta = cursor.fetchone()

    cursor.execute("""
        SELECT jogos.CodigoJogo, jogos.name, jogos.capsule_image, lista.TipoLista AS lista_nome
        FROM jogos
        JOIN lista_jogos ON jogos.CodigoJogo = lista_jogos.CodigoJogo
        JOIN lista ON lista_jogos.CodigoLista = lista.CodigoLista
        WHERE lista.CodigoConta = %s
    """, (user_id,))

    
    jogos = cursor.fetchall()
    cursor.close()
    conexao.close()

    jogos_dict = {
        'Jogos': [],
        'Jogando Atualmente': [],
        'Jogos Zerados': []
    }
    for jogo in jogos:
        jogos_dict[jogo['lista_nome']].append(jogo)

    return render_template('paginaGames.html', jogos=jogos_dict, dadosUser=conta)


