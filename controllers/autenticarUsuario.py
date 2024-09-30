from forms.forms import AutenticacaoForm
from flask import redirect, render_template, flash

#Ainda não foi finalizado.
def autenticarUsuario():
    form = AutenticacaoForm()
    email = "exemplo@email.com"
    
    if form.validate_on_submit():
        codigo_verificacao = form.codigo_verificacao.data
        if codigo_verificacao == "123456":
            flash('Autenticação concluída com sucesso!', 'success')
            return redirect('/paginaInicial')
        else:
            flash('Código de verificação incorreto!', 'danger')

    return render_template('autenticarUsuario.html', form=form, email=email)