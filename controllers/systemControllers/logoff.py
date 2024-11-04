from flask import redirect, session, url_for, flash

def deslogarUsuario():

    if 'user_id' in session:

        session.pop('user_id', None)
        flash('Você foi deslogado com sucesso!', 'success')
    else:
        flash('Você não está logado!', 'warning')

    return redirect(url_for('loginUsuario'))
