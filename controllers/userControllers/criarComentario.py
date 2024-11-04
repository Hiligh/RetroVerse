from flask import request, flash, redirect, session, url_for
from data.conectarBD import conectarBD
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

            insert_comentario_query = """
            INSERT INTO comentario (comentario) 
            VALUES (%s)
            """
            cursor.execute(insert_comentario_query, (comentario_texto,))
            conexao.commit()

            codigoComentario = cursor.lastrowid

            insert_conta_comentario_query = """
            INSERT INTO conta_comentario (CodigoConta, CodigoComentario)
            VALUES (%s, %s)
            """
            cursor.execute(insert_conta_comentario_query, (codigoConta, codigoComentario))

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
