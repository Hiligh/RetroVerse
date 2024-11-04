from flask import render_template, session, redirect, url_for, flash, request
from data.conectarBD import conectarBD
import mysql.connector

def Forum():

    if 'user_id' not in session:
        flash("Você precisa estar logado para acessar o fórum.", "danger")
        return redirect(url_for('loginUsuario'))

    conexao = conectarBD()
    user_id = session.get('user_id')
    ordenacao = request.args.get('ordenacao', 'Mais novos')

    select_usuario_query = """
    SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1
    """

    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute(select_usuario_query, (user_id,))
        conta = cursor.fetchone()
        
        if not conta:
            return redirect(url_for('loginUsuario'))
        
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao conectar ao banco de dados", 500

    if ordenacao == "Mais antigos":
        order_clause = "ORDER BY t.DataCriação ASC"
    elif ordenacao == "Mais comentados":
        order_clause = "ORDER BY num_comentarios DESC"
    elif ordenacao == "Mais curtidos":
        order_clause = "ORDER BY t.Curtidas DESC"
    else:
        order_clause = "ORDER BY t.DataCriação DESC"

    select_topicos_query = f"""
    SELECT t.CodigoTopico, t.Titulo, t.Descricao, t.DataCriação, t.Curtidas, c.Nome,
           COUNT(tc.CodigoComentario) AS num_comentarios
    FROM topico t
    JOIN conta c ON t.CodigoConta = c.CodigoConta
    LEFT JOIN topico_comentario tc ON t.CodigoTopico = tc.CodigoTopico
    GROUP BY t.CodigoTopico, t.Titulo, t.Descricao, t.DataCriação, t.Curtidas, c.Nome
    {order_clause}
    """

    try:
        cursor.execute(select_topicos_query)
        topicos = cursor.fetchall()

    except mysql.connector.Error as err:
        print(f"Erro ao buscar tópicos: {err}")
        flash('Erro ao carregar os tópicos, tente novamente mais tarde.', 'danger')
        return redirect(url_for('paginaInicial'))

    finally:
        cursor.close()
        conexao.close()

    # Renderiza a página com os tópicos recuperados
    return render_template('forum.html', topicos=topicos, dadosUser=conta)
