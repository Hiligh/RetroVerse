from flask import Flask
from controllers.logarUsuario import logarUsuario
from controllers.cadastrarUsuario import cadastrarUsuario
from controllers.homePage import homePage
from controllers.autenticarUsuario import autenticarUsuario
from controllers.catalogo import mostrarCatalogo
from controllers.reviewsUsuario import reviewsUsuario
from controllers.gamesUsuario import gamesUsuario
from controllers.perfilUsuario import perfilUsuario
from controllers.excluirContaUsuario import excluirConta
from controllers.paginaForum import Forum
from controllers.paginaJogo import mostrarJogo
from controllers.paginaTopico import criarTopico
from controllers.paginaVisualizarTopico import visualizarTopico
from controllers.criarComentario import adicionarComentario

#Teste Requisições!
#CHAVE API STEAM: 8BF1A490FA51FF973B976E66061F55CE
app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def loginUsuario():
    return logarUsuario()

@app.route('/criarConta', methods=['GET', 'POST'])
def criarUsuario():
    return cadastrarUsuario()

@app.route('/paginaInicial')
def paginaInicial():
    return homePage()

@app.route('/autenticarUsuario', methods=['GET', 'POST'])
def autenticarConta():
    return autenticarUsuario()

@app.route('/paginaCatalogo', methods=['GET', 'POST'])
def paginaCatalogo():
    return mostrarCatalogo()

@app.route('/paginaReviews')
def paginaReviews():
    return reviewsUsuario()

@app.route('/paginaGames')
def paginaGames():
    return gamesUsuario()

@app.route('/perfilUsuario')
def paginaUsuario():
    return perfilUsuario()

@app.route('/topico', methods=['POST', 'GET'])
def paginaTopico():
    return criarTopico() 

@app.route('/paginaForum')
def paginaForum():
    return Forum()

@app.route('/excluirConta', methods=['POST'])
def excluirContaUsuario():
    return excluirConta()

@app.route('/paginaJogo/<int:jogo_id>')
def paginaJogo(jogo_id):
    return mostrarJogo(jogo_id)

@app.route('/paginaVisualizarTopico/<int:topico_id>', methods=['GET'])
def paginaVisualizarTopico(topico_id):
    return visualizarTopico(topico_id)

@app.route('/adicionarComentario/<int:topico_id>', methods=['POST'])
def criarComentario(topico_id):
    return adicionarComentario(topico_id)

if __name__ == '__main__':
    app.run(debug=True)