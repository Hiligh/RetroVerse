from forms.forms import LoginForm
from data.conectarBD import conectarBD
from flask import redirect, render_template, flash, session
import mysql.connector

#Após logar o usuário, salva as informações em uma session para usos futuros dos dados do usuário.
def logarUsuario():
    form = LoginForm()
    if form.validate_on_submit():
        conexao = conectarBD()
        emailUsuario = form.email.data
        senhaUsuario = form.senha.data

        select_usuario_query = """
        SELECT * FROM conta WHERE Email = %s AND Senha = %s LIMIT 1
        """
        dadosUsuario = (emailUsuario, senhaUsuario)
        
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(select_usuario_query, dadosUsuario)
            conta = cursor.fetchone()

            if conta:
                session['user_id'] = conta['CodigoConta']
                cursor.close()
                conexao.close()
                return redirect('/paginaInicial')
            else:
                flash('Usuário ou senha incorretos!', 'danger')

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return "Erro ao conectar ao banco de dados", 500
        
        finally:
            cursor.close()
            conexao.close()

    return render_template('index.html', form=form)
