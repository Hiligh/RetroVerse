from forms.forms import LoginForm
from data.conectarBD import conectarBD
from flask import redirect, render_template, flash
import mysql.connector

def logarUsuario():
    form = LoginForm()
    if form.validate_on_submit():
        conexao = conectarBD()
        emailUsuario = form.email.data
        senhaUsuario = form.senha.data

        select_usuario_query = """
        SELECT * FROM conta WHERE Email = %s AND Senha = %s
        """
        dadosUsuario = (emailUsuario, senhaUsuario)
        
        try:
            cursor = conexao.cursor()
            cursor.execute(select_usuario_query, dadosUsuario)
            conta = cursor.fetchall()

            if conta:
                cursor.close()
                conexao.close()
                return redirect('/paginaInicial')

            else:
                #Corrijir para aparecer a mensagem de erro
                flash('Usuário ou senha incorretos!', 'danger')
                

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao conectar ao banco de dados", 500
        
        finally:
            cursor.close()
            conexao.close()

    return render_template('index.html', form=form)