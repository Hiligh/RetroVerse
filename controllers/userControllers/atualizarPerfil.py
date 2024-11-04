from flask import request, flash, session, redirect, url_for
from data.conectarBD import conectarBD
import mysql.connector

def atualizarPerfil():
    if 'user_id' not in session:
        return redirect(url_for('loginUsuario'))
    
    user_id = session.get('user_id')
    nome = request.form.get('Nome')
    email = request.form.get('Email')
    idade = request.form.get('Idade')
    senha = request.form.get('Senha')

    conexao = conectarBD()
    
    update_query = """
    UPDATE conta 
    SET Nome = %s, Email = %s, Idade = %s, Senha = %s 
    WHERE CodigoConta = %s
    """

    try:
        cursor = conexao.cursor()
        cursor.execute(update_query, (nome, email, idade, senha, user_id))
        conexao.commit()
        
        flash("Informações atualizadas com sucesso!", "success")
        return redirect(url_for('paginaUsuario'))

    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        flash("Erro ao atualizar informações.", "danger")
        return redirect(url_for('paginaUsuario'))

    finally:
        cursor.close()
        conexao.close()
