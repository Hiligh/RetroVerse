from forms.forms import AutenticacaoForm
from flask import redirect, render_template, flash, session
import pyotp
import smtplib
import email.message

chaveMestre = '7DUXJK66S72Q23HTK64V4K5QMZO5VEXY'

def enviarEmail(emailUsuario, nomeUsuario, codigoAutenticacao):

    corpoEmail = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Autenticação de Código</title>
        <style>
            body {{
                width: 600px;
                height: 600px;
                background-color: #000000; /* Fundo preto */
                color: white;
                font-family: 'Arial', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
            }}

            .container {{
                background-color: #ffffff;
                text-align: center;
                padding: 20px;
                border-radius: 8px;
            }}

            .logo {{
                margin-bottom: 20px;
            }}

            h1 {{
                font-size: 28px;
                margin-bottom: 15px;
                color: #000000;
            }}

            .textoEmail{{
                color: #000000;
            }}

            .codigo {{
                font-size: 40px;
                color: white;
                background-color: #112240; /* Botão azul escuro */
                padding: 10px 20px;
                border-radius: 8px;
                display: inline-block;
                margin-top: 20px;
            }}

            p {{
                font-size: 18px;
                margin-bottom: 10px;
            }}

            .highlight {{
                font-weight: bold;
                color: #4bc0e6;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Olá <span class="highlight">{nomeUsuario}</span>!</h1>
            <p class="textoEmail">Segue o seu código de autenticação abaixo:</p>
            <div class="codigo">{codigoAutenticacao}</div>
        </div>
    </body>
    </html>
    """

    mensagem = email.message.Message()
    mensagem['Subject'] = "Email de Verificação do Usuário!"
    mensagem['From'] = 'retroverse2001@gmail.com'
    mensagem['To'] = emailUsuario
    passwordGoogle = 'obwa kwij yyjv ymbg'
    mensagem.add_header('Content-Type', 'text/html')
    mensagem.set_payload(corpoEmail)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(mensagem['From'], passwordGoogle)
    s.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
    print('Email Enviado com sucesso!')
    
def autenticarUsuario():
    emailUser = session.get('email_usuario')
    nomeUser = session.get('nome_usuario')
    codigoAutenticador = pyotp.TOTP(chaveMestre)
    print(codigoAutenticador.now())
    form = AutenticacaoForm()
    
    autenticacaoAtivada = session.get('two_factor_enabled')
    print(autenticacaoAtivada)

    if form.validate_on_submit():
        codigo_verificacao = form.codigo_verificacao.data
        print(codigo_verificacao)
        if codigoAutenticador.verify(codigo_verificacao, valid_window=2):
            flash('Autenticação concluída com sucesso!', 'success')
            if(autenticacaoAtivada == 1):
                return redirect('/paginaInicial')
            
            return redirect('/')
        else:
            print('Deu errado no código meu amigo')
            flash('Código de verificação incorreto ou expirado!. Tente novamente', 'danger')
    return render_template('autenticarUsuario.html', form=form, emailUsuario=emailUser)