from forms.forms import CadastroForm
from data.conectarBD import conectarBD
from flask import redirect, render_template, flash, session
import mysql.connector

def cadastrarUsuario():
    form = CadastroForm()
    
    if form.validate_on_submit():
        nomeUsuario = form.nome.data
        idadeUsuario = form.data_nascimento.data
        emailUsuario = form.email.data
        senhaUsuario = form.senha.data
        confirmarSenha = form.confirmacao_senha.data
        
        conexao = conectarBD()

        selectEmail = """
        SELECT * FROM conta WHERE Email = %s
        """
        try:
            cursor = conexao.cursor(dictionary=True)
            cursor.execute(selectEmail, (emailUsuario,))
            conta = cursor.fetchone()

            if conta:
                flash('Email já usado! Escolha outro.', 'danger')
                return render_template('criarConta.html', form=form)

            if senhaUsuario != confirmarSenha:
                flash('As senhas não coincidem!', 'danger')
                return render_template('criarConta.html', form=form)

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            conexao.rollback()
            flash('Erro ao acessar o banco de dados.', 'danger')
            return render_template('criarConta.html', form=form)

        try:
            foto_perfil = "https://randomuser.me/api/portraits/men/1.jpg"
            insert_conta_query = """
            INSERT INTO conta (Nome, Email, Senha, FotoPerfil, Idade, Autenticacao)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            dadosUsuario = (nomeUsuario, emailUsuario, senhaUsuario, foto_perfil, idadeUsuario, False)
            
            cursor = conexao.cursor()
            cursor.execute(insert_conta_query, dadosUsuario)
            conexao.commit()
            flash('Conta criada com sucesso!', 'success')

            codigoConta = cursor.lastrowid

            criar_listas_usuario = """
            INSERT INTO lista (Tipolista, CodigoConta)
            VALUES (%s, %s)
            """
            tipos_lista = ["Jogos", "Jogando Atualmente", "Jogos Zerados"]
            for tipo in tipos_lista:
                cursor.execute(criar_listas_usuario, (tipo, codigoConta))
            conexao.commit()

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            conexao.rollback()
            flash('Erro ao criar a conta. Tente novamente.', 'danger')
            return render_template('criarConta.html', form=form)

        finally:
            cursor.close()
            conexao.close()
        session['nome_usuario'] = nomeUsuario
        session['email_usuario'] = emailUsuario
        return redirect('/autenticarUsuario')
    return render_template('criarConta.html', form=form)
