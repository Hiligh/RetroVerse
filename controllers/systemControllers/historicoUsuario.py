from flask import render_template, redirect, url_for, session, flash
from data.conectarBD import conectarBD
import mysql.connector

def mostrarHistorico():
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

            query_avaliacoes_jogos = """
            SELECT j.name, aj.rating
            FROM avaliacao_jogo aj
            JOIN jogos j ON aj.CodigoJogo = j.CodigoJogo
            WHERE aj.CodigoConta = %s
            """
            cursor.execute(query_avaliacoes_jogos, (user_id,))
            avaliacoes_jogos = cursor.fetchall()

            query_comentarios = """
            SELECT t.Titulo, c.comentario
            FROM comentario c
            JOIN conta_comentario cc ON c.CodigoComentario = cc.CodigoComentario
            JOIN topico_comentario tc ON c.CodigoComentario = tc.CodigoComentario
            JOIN topico t ON tc.CodigoTopico = t.CodigoTopico
            WHERE cc.CodigoConta = %s
            """
            cursor.execute(query_comentarios, (user_id,))
            comentarios = cursor.fetchall()

            query_likes = """
            SELECT t.Titulo
            FROM avaliacao_topico at
            JOIN topico t ON at.CodigoTopico = t.CodigoTopico
            WHERE at.CodigoConta = %s
            """
            cursor.execute(query_likes, (user_id,))
            likes = cursor.fetchall()

            return render_template(
                'paginaHistóricoUsuario.html',
                dadosUser=conta,
                avaliacoes_jogos=avaliacoes_jogos,
                comentarios=comentarios,
                likes=likes
            )
        else:
            return redirect(url_for('loginUsuario'))
    
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao conectar ao banco de dados", 500
    
    finally:
        cursor.close()
        conexao.close()
