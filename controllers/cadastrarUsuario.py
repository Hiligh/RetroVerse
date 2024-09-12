from forms.forms import CadastroForm
from data.conectarBD import conectarBD
from flask import redirect, render_template, flash
import mysql.connector

def cadastrarUsuario():
    form = CadastroForm()
    if form.validate_on_submit():
        nomeUsuario = form.nome.data
        idadeUsuario = form.data_nascimento.data
        emailUsuario = form.email.data
        senhaUsuario = form.senha.data
        confirmarSenha = form.confirmacao_senha.data

        if senhaUsuario != confirmarSenha:
            #Corrijir para aparecer a mensagem de erro
            flash('As senhas não coincidem!', 'danger')
        else:
            conexao = conectarBD()
            foto_perfil = "https://randomuser.me/api/portraits/men/1.jpg"

            insert_conta_query = """
            INSERT INTO conta (Nome, Email, Senha, FotoPerfil, Idade)
            VALUES (%s, %s, %s, %s, %s)
            """
            dadosUsuario = (nomeUsuario, emailUsuario, senhaUsuario, foto_perfil, idadeUsuario)

            try:
                cursor = conexao.cursor()
                cursor.execute(insert_conta_query, dadosUsuario)
                conexao.commit()
                print('Dados salvos com sucesso!')

            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                conexao.rollback()
            finally:
                cursor.close()
                conexao.close()

            return redirect('/autenticarUsuario')

    return render_template('criarConta.html', form=form)