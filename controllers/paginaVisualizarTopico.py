from flask import render_template, request, flash, redirect
from data.conectarBD import conectarBD  # Certifique-se de que esta função está correta e retorna uma conexão com o banco

def visualizarTopico(topico_id):
    if not topico_id:
        flash('ID do tópico não foi fornecido.', 'danger')
        return redirect('/')

    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    try:
        # A consulta agora inclui o CodigoTopico
        query_topico = """
        SELECT t.CodigoTopico, t.Titulo, t.Descricao, c.Nome, t.DataCriação, t.Curtidas 
        FROM topico t 
        JOIN conta c ON t.CodigoConta = c.CodigoConta 
        WHERE t.CodigoTopico = %s
        """
        cursor.execute(query_topico, (topico_id,))
        topico = cursor.fetchone()

        if not topico:
            flash('Tópico não encontrado.', 'danger')
            return redirect('/paginaForum')

        # Buscar comentários
        query_comentarios = """
        SELECT comentario.comentario, conta.Nome
        FROM comentario
        INNER JOIN topico_comentario ON comentario.CodigoComentario = topico_comentario.CodigoComentario
        INNER JOIN conta_comentario ON comentario.CodigoComentario = conta_comentario.CodigoComentario
        INNER JOIN conta ON conta_comentario.CodigoConta = conta.CodigoConta
        WHERE topico_comentario.CodigoTopico = %s
        """
        cursor.execute(query_comentarios, (topico_id,))
        comentarios = cursor.fetchall()
    except Exception as e:
        flash(f'Erro ao buscar o tópico: {e}', 'danger')
        return redirect('/paginaForum')

    finally:
        cursor.close()
        conexao.close()

    return render_template('paginaVisualizarTopico.html', topico=topico, comentarios=comentarios)