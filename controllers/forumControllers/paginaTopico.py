from flask import render_template, request, redirect, url_for, session, flash
from data.conectarBD import conectarBD
import mysql.connector
from datetime import datetime

def criarTopico():

    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))

    user_id = session.get('user_id')

    cursor.execute("SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1", (user_id,))
    conta = cursor.fetchone()

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        codigoConta = session['user_id']
        dataCriacao = datetime.now().date()
        curtidas = 0

        conexao = conectarBD()

        insert_topico_query = """
        INSERT INTO topico (CodigoConta, Titulo, Descricao, DataCriação, Curtidas)
        VALUES (%s, %s, %s, %s, %s)
        """
        topico_data = (codigoConta, titulo, descricao, dataCriacao, curtidas)

        try:
            cursor = conexao.cursor()
            cursor.execute(insert_topico_query, topico_data)
            conexao.commit()

            topico_id = cursor.lastrowid

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

    return render_template('topico.html', dadosUser=conta)