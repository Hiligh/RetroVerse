import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mostraBanco import mostraBanco

os.environ["FLASK_ENV"] = "development"
app = Flask(__name__) #cria o site vazio

# Conexão com o BD:
conexao = mysql.connector.connect(
    host="localhost",
    database="retroversedb",
    user="root",
    password="1234",
)

if conexao.is_connected():
    print("DB Conectado!")
    cursor = conexao.cursor()

# mostraBanco(conexao)

#Rota Homepage
@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def logarConta():
    emailUsuario = request.form.get('login-email')
    senhaUsuario = request.form.get('login-senha')

    select_usuario_query = """
    SELECT * FROM conta WHERE Email = %s AND Senha = %s
    """
    dadosUsuario = (emailUsuario, senhaUsuario)
    
    try:
        with conexao.cursor() as cursor:
            cursor.execute(select_usuario_query, dadosUsuario)
            conta = cursor.fetchone()
            print(conta)
        
        # Se uma conta foi encontrada, o usuário está autenticado
        if conta:
            return redirect(('/paginaInicial'))
        if(conta == None):
            return '''
                <script>
                    alert("Usuário ou senha incorretos!");
                    window.location.href = "/";
                </script>
            '''
        else:
            return redirect('/criarConta')
        
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return "Erro ao conectar ao banco de dados", 500
    
@app.route('/paginaInicial')
def paginaInicial():
    return render_template("paginaInicial.html")

#Rota de Criação de Conta
@app.route("/criarConta")
def mostrarCadastrarUsuário():
    return render_template("criarConta.html")

@app.route('/criarConta', methods=['POST'])
def criarContaUsuario():
    nomeUsuario = request.form.get('nomeUsuario') 
    idade = request.form.get('idade')
    email = request.form.get('criar-email')
    senha = request.form.get('criar-senha')
    confirmar_senha = request.form.get('confirmar-senha')

    
    foto_perfil = "https://randomuser.me/api/portraits/men/1.jpg"
    
    insert_conta_query = """
    INSERT INTO conta (Nome, Email, Senha, FotoPerfil, Idade)
    VALUES (%s, %s, %s, %s, %s)
    """
    dadosUsuario = (nomeUsuario, email, senha, foto_perfil, idade)

    try:
        with conexao.cursor() as cursor:
            cursor.execute(insert_conta_query, dadosUsuario)
            conexao.commit()
            print('Dados salvos com sucesso!')
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        conexao.rollback()

    conexao.close()
    cursor.close()

    return redirect(url_for('autenticarUsuario', email=email))

@app.route('/autenticaçãoUsuario')
def autenticarUsuario():
    email = request.args.get('email')
    return render_template("autenticarUsuario.html", email=email)

if __name__ == "__main__":
    app.run(debug=True)