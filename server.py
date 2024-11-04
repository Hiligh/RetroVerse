from flask import Flask
from controllers.systemControllers.logarUsuario import logarUsuario
from controllers.systemControllers.cadastrarUsuario import cadastrarUsuario
from controllers.systemControllers.homePage import homePage
from controllers.systemControllers.autenticarUsuario import autenticarUsuario
from controllers.catalogoControllers.catalogo import mostrarCatalogo
from controllers.systemControllers.gamesUsuario import gamesUsuario
from controllers.systemControllers.perfilUsuario import perfilUsuario
from controllers.systemControllers.excluirContaUsuario import excluirConta
from controllers.forumControllers.paginaForum import Forum
from controllers.gameControllers.paginaJogo import mostrarJogo
from controllers.forumControllers.paginaTopico import criarTopico
from controllers.forumControllers.paginaVisualizarTopico import visualizarTopico
from controllers.userControllers.criarComentario import adicionarComentario
from controllers.userControllers.atualizarPerfil import atualizarPerfil
from controllers.userControllers.curtirTopico import curtirTopico
from controllers.userControllers.avaliarJogo import avaliarJogo
from controllers.catalogoControllers.dropDCatalogo import dropdownCatalogo
from controllers.userControllers.descurtirTopico import descurtirTopico
from controllers.gameControllers.adicionarJogosLista import adicionarJogos
from controllers.systemControllers.logoff import deslogarUsuario
from controllers.systemControllers.historicoUsuario import mostrarHistorico
from controllers.systemControllers.autenticacaoDoisFatores import ativarAutenticacao

#Teste Requisições!
#CHAVE API STEAM: 8BF1A490FA51FF973B976E66061F55CE
app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def loginUsuario():
    return logarUsuario()

@app.route('/logoff', methods=['GET'])
def logoffUsuario():
    return deslogarUsuario()


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

@app.route('/atualizarPerfil', methods=['POST'])
def atualizarInformaçõesPerfil():
    return atualizarPerfil()

@app.route('/curtir/<int:topico_id>', methods=['POST'])
def curtidasTopico(topico_id):
    return curtirTopico(topico_id)

@app.route('/avaliarJogo', methods=['POST'])
def avaliar_jogo():
    return avaliarJogo()

@app.route('/dropdownCatalogo', methods=['POST'])
def buscar_sugestoes():
    return dropdownCatalogo()

@app.route('/descurtir/<int:topico_id>', methods=['POST'])
def descurtirTopicoRoute(topico_id):
    return descurtirTopico(topico_id)

@app.route('/adicionarJogosLista', methods=['POST'])
def adicionarJogosLista():
    return adicionarJogos()

@app.route('/historicoUsuario', methods=['GET'])
def historicoUsuario():
    return mostrarHistorico()

@app.route('/ativarAutenticacao', methods=['POST'])
def autenticacaoDoisFatores():
    return ativarAutenticacao()

if __name__ == '__main__':
    app.run(debug=True)