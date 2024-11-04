from flask import flash, redirect, url_for, session
from data.conectarBD import conectarBD

def descurtirTopico(topico_id):

    if 'user_id' not in session:
        flash("Você precisa estar logado para descurtir o tópico.", "danger")
        return redirect(url_for('loginUsuario'))

    user_id = session['user_id']

    if not topico_id:
        flash('ID do tópico não foi fornecido.', 'danger')
        return redirect('/')

    conexao = conectarBD()
    cursor = conexao.cursor()

    try:

        query_check = """
        SELECT * FROM avaliacao_topico WHERE CodigoTopico = %s AND CodigoConta = %s
        """
        cursor.execute(query_check, (topico_id, user_id))
        curtida_existente = cursor.fetchone()

        if not curtida_existente:
            flash('Você ainda não curtiu este tópico!', 'warning')
            return redirect(url_for('paginaVisualizarTopico', topico_id=topico_id))

        query_delete = """
        DELETE FROM avaliacao_topico 
        WHERE CodigoTopico = %s AND CodigoConta = %s
        """
        cursor.execute(query_delete, (topico_id, user_id))

        query_update_curtidas = """
        UPDATE topico 
        SET Curtidas = Curtidas - 1 
        WHERE CodigoTopico = %s
        """
        cursor.execute(query_update_curtidas, (topico_id,))
        conexao.commit()

        flash('Você descurtiu o tópico com sucesso!', 'success')
    except Exception as e:
        conexao.rollback()
        flash(f'Erro ao descurtir o tópico: {e}', 'danger')
        return redirect('/paginaForum')
    finally:
        cursor.close()
        conexao.close()

    return redirect(url_for('paginaVisualizarTopico', topico_id=topico_id))
