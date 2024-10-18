from flask import render_template, session, redirect, url_for, flash
from data.conectarBD import conectarBD
import mysql.connector

def Forum():
    # Verifica se o usuário está logado
    if 'user_id' not in session:
        flash("Você precisa estar logado para acessar o fórum.", "danger")
        return redirect(url_for('loginUsuario'))

    # Conectar ao banco de dados
    conexao = conectarBD()

    select_topicos_query = """
    SELECT t.CodigoTopico, t.Titulo, t.Descricao, t.DataCriação, t.Curtidas, c.Nome
    FROM topico t
    JOIN conta c ON t.CodigoConta = c.CodigoConta
    ORDER BY t.DataCriação DESC
    """

    
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(select_topicos_query)
        topicos = cursor.fetchall()  # Pega todos os tópicos do banco de dados

    except mysql.connector.Error as err:
        print(f"Erro ao buscar tópicos: {err}")
        flash('Erro ao carregar os tópicos, tente novamente mais tarde.', 'danger')
        return redirect(url_for('paginaInicial'))

    finally:
        cursor.close()
        conexao.close()

    # Renderiza a página com os tópicos recuperados
    return render_template('forum.html', topicos=topicos)
