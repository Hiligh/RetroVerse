from flask import Flask
from controllers.logarUsuario import logarUsuario
from controllers.cadastrarUsuario import cadastrarUsuario
from controllers.homePage import homePage
from controllers.autenticarUsuario import autenticarUsuario

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
    autenticarUsuario()

if __name__ == '__main__':
    app.run(debug=True)