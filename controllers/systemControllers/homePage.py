from flask import render_template, redirect, url_for, session
from data.conectarBD import conectarBD
import mysql.connector

def homePage():
    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))

    user_id = session.get('user_id')
    conexao = conectarBD()

    select_usuario_query = """
    SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1
    """

    melhores_jogos_query = """
    SELECT j.*, AVG(a.rating) AS media_rating
    FROM jogos j
    JOIN avaliacao_jogo a ON j.CodigoJogo = a.CodigoJogo
    GROUP BY j.CodigoJogo
    ORDER BY media_rating DESC
    LIMIT 4
    """

    jogos_populares_query = """
    SELECT j.*, COUNT(a.rating) AS num_avaliacoes
    FROM jogos j
    JOIN avaliacao_jogo a ON j.CodigoJogo = a.CodigoJogo
    GROUP BY j.CodigoJogo
    ORDER BY num_avaliacoes DESC
    LIMIT 4
    """

    topicos_populares_query = """
    SELECT t.CodigoTopico, t.Titulo, t.Descricao, t.DataCriação, t.Curtidas, c.Nome,
           COUNT(tc.CodigoComentario) AS num_comentarios
    FROM topico t
    JOIN conta c ON t.CodigoConta = c.CodigoConta
    LEFT JOIN topico_comentario tc ON t.CodigoTopico = tc.CodigoTopico
    GROUP BY t.CodigoTopico, t.Titulo, t.Descricao, t.DataCriação, t.Curtidas, c.Nome
    ORDER BY num_comentarios DESC, t.Curtidas DESC
    LIMIT 5
    """

    try:
        cursor = conexao.cursor(dictionary=True)

        cursor.execute(select_usuario_query, (user_id,))
        conta = cursor.fetchone()

        cursor.execute(melhores_jogos_query)
        melhores_jogos = cursor.fetchall()

        cursor.execute(jogos_populares_query)
        jogos_populares = cursor.fetchall()

        cursor.execute(topicos_populares_query)
        topicos_populares = cursor.fetchall()

        if conta:
            return render_template(
                'paginaInicial.html', 
                dadosUser=conta,
                melhores_jogos=melhores_jogos,
                jogos_populares=jogos_populares,
                topicos_populares=topicos_populares
            )
        else:
            return redirect(url_for('loginUsuario'))

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao conectar ao banco de dados", 500

    finally:
        cursor.close()
        conexao.close()
