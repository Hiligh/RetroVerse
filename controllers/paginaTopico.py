from flask import render_template, request, redirect, url_for, session, flash
from data.conectarBD import conectarBD
import mysql.connector
from datetime import datetime

def criarTopico():
    # Verifica se o usuário está logado
    if 'user_id' not in session:
        flash("Você precisa estar logado para criar um tópico.", "danger")
        return redirect(url_for('loginUsuario'))

    # Quando o formulário for submetido via POST
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        codigoConta = session['user_id']  # Pega o ID do usuário logado
        dataCriacao = datetime.now().date()  # Pega a data atual
        curtidas = 0  # Tópicos novos começam com 0 curtidas

        # Conectar ao banco de dados
        conexao = conectarBD()

        insert_topico_query = """
        INSERT INTO topico (CodigoConta, Titulo, Descricao, DataCriação, Curtidas)
        VALUES (%s, %s, %s, %s, %s)
        """
        topico_data = (codigoConta, titulo, descricao, dataCriacao, curtidas)

        try:
            cursor = conexao.cursor()
            cursor.execute(insert_topico_query, topico_data)
            conexao.commit()  # Salva as mudanças no banco de dados

            # Pegar o ID do tópico recém-criado
            topico_id = cursor.lastrowid

            # Salvar o ID do tópico na sessão
            session['topico_id'] = topico_id

            flash('Tópico criado com sucesso!', 'success')
            return redirect(url_for('paginaForum'))

        except mysql.connector.Error as err:
            print(f"Erro ao inserir tópico: {err}")
            flash('Erro ao criar tópico, tente novamente mais tarde.', 'danger')
            return redirect(url_for('paginaTopico'))

        finally:
            cursor.close()
            conexao.close()

    # Se for uma requisição GET, apenas renderiza a página para criar o tópico
    return render_template('topico.html')
