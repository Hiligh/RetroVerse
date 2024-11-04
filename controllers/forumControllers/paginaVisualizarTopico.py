from flask import render_template, request, flash, redirect, session
from data.conectarBD import conectarBD

def visualizarTopico(topico_id):
    
    if not topico_id:
        flash('ID do tópico não foi fornecido.', 'danger')
        return redirect('/')

    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    try:
        # Query para buscar os detalhes do tópico
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

        # Query para buscar os comentários, incluindo a FotoPerfil
        query_comentarios = """
        SELECT comentario.comentario, conta.Nome, conta.FotoPerfil
        FROM comentario
        INNER JOIN topico_comentario ON comentario.CodigoComentario = topico_comentario.CodigoComentario
        INNER JOIN conta_comentario ON comentario.CodigoComentario = conta_comentario.CodigoComentario
        INNER JOIN conta ON conta_comentario.CodigoConta = conta.CodigoConta
        WHERE topico_comentario.CodigoTopico = %s
        """
        cursor.execute(query_comentarios, (topico_id,))
        comentarios = cursor.fetchall()

        # Verificar se o usuário atual curtiu o tópico
        usuario_curtiu = False
        if 'user_id' in session:
            user_id = session['user_id']

            query_usuario_curtiu = """
            SELECT 1 FROM avaliacao_topico 
            WHERE CodigoTopico = %s AND CodigoConta = %s
            LIMIT 1
            """
            cursor.execute(query_usuario_curtiu, (topico_id, user_id))
            usuario_curtiu = cursor.fetchone() is not None

        # Buscar informações do usuário logado
        select_usuario_query = """
        SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1
        """
        cursor.execute(select_usuario_query, (user_id,))
        conta = cursor.fetchone()

    except Exception as e:
        flash(f'Erro ao buscar o tópico: {e}', 'danger')
        return redirect('/paginaForum')

    finally:
        cursor.close()
        conexao.close()

    return render_template(
        'paginaVisualizarTopico.html',
        topico=topico, 
        comentarios=comentarios, 
        usuario_curtiu=usuario_curtiu,
        dadosUser=conta
    )
