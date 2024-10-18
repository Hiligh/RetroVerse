from flask import render_template
from data.conectarBD import conectarBD

def mostrarJogo(jogo_id):
    conexao = conectarBD()
    cursor = conexao.cursor(dictionary=True)

    # Query para pegar os detalhes do jogo pelo ID
    cursor.execute("SELECT * FROM jogos WHERE CodigoJogo = %s", (jogo_id,))
    jogo = cursor.fetchone()  # Pega o jogo correspondente ao ID

    cursor.close()
    conexao.close()

    # Verifica se o jogo foi encontrado e renderiza o template
    if jogo:
        return render_template('paginaJogo.html', jogo=jogo)
    else:
        return "Jogo não encontrado.", 404  # Retorna um erro 404 se não encontrado