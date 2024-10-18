from flask import request, flash, redirect, session, url_for
from data.conectarBD import conectarBD  # Certifique-se de que esta função está correta e retorna uma conexão com o banco
from datetime import datetime

def adicionarComentario(topico_id):
    if 'user_id' not in session:
        flash("Você precisa estar logado para comentar.", "danger")
        return redirect(url_for('loginUsuario'))

    if request.method == 'POST':
        comentario_texto = request.form.get('comentario')
        codigoConta = session['user_id']

        conexao = conectarBD()
        cursor = conexao.cursor()

        try:
            # Inserir o comentário na tabela `comentario`
            insert_comentario_query = """
            INSERT INTO comentario (comentario) 
            VALUES (%s)
            """
            cursor.execute(insert_comentario_query, (comentario_texto,))
            conexao.commit()

            # Pegar o ID do comentário inserido
            codigoComentario = cursor.lastrowid

            # Inserir o relacionamento na tabela `conta_comentario`
            insert_conta_comentario_query = """
            INSERT INTO conta_comentario (CodigoConta, CodigoComentario)
            VALUES (%s, %s)
            """
            cursor.execute(insert_conta_comentario_query, (codigoConta, codigoComentario))

            # Inserir o relacionamento na tabela `topico_comentario`
            insert_topico_comentario_query = """
            INSERT INTO topico_comentario (CodigoTopico, CodigoComentario)
            VALUES (%s, %s)
            """
            cursor.execute(insert_topico_comentario_query, (topico_id, codigoComentario))

            conexao.commit()

            flash('Comentário adicionado com sucesso!', 'success')
        except Exception as e:
            flash(f'Erro ao adicionar comentário: {e}', 'danger')
        finally:
            cursor.close()
            conexao.close()

        return redirect(url_for('paginaVisualizarTopico', topico_id=topico_id))

    return redirect('/paginaForum')
