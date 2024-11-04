from forms.forms import LoginForm
from data.conectarBD import conectarBD
from flask import redirect, render_template, flash, session, url_for
import mysql.connector

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
                session['email_usuario'] = emailUsuario
                session['nome_usuario'] = conta['Nome']
                session['two_factor_enabled'] = conta.get('Autenticacao') == 1

                if session['two_factor_enabled']:
                    return redirect(url_for('autenticarConta'))

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

