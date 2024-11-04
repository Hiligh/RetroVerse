from flask import redirect, render_template, session, url_for
from data.conectarBD import conectarBD

def perfilUsuario():
    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))

    user_id = session.get('user_id')

    cursor.execute("SELECT * FROM conta WHERE CodigoConta = %s LIMIT 1", (user_id,))
    conta = cursor.fetchone()

    cursor.execute("""
        SELECT COUNT(lj.CodigoJogo) as total_jogos
        FROM lista l
        INNER JOIN lista_jogos lj ON l.CodigoLista = lj.CodigoLista
        WHERE l.CodigoConta = %s
    """, (user_id,))
    total_jogos = cursor.fetchone()['total_jogos']

    cursor.execute("""
        SELECT COUNT(*) as total_comentarios
        FROM conta_comentario
        WHERE CodigoConta = %s
    """, (user_id,))
    total_comentarios = cursor.fetchone()['total_comentarios']

    cursor.execute("""
        SELECT COUNT(DISTINCT CodigoJogo) as total_jogos_avaliados
        FROM avaliacao_jogo
        WHERE CodigoConta = %s
    """, (user_id,))
    total_jogos_avaliados = cursor.fetchone()['total_jogos_avaliados']

    cursor.close()
    conexao.close()

    return render_template('perfilUsuario.html', dadosUser=conta, total_jogos=total_jogos, total_comentarios=total_comentarios, total_jogos_avaliados=total_jogos_avaliados)