from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from datetime import datetime

def validar_data_nascimento(form, field):
    data_nascimento = field.data
    idade = (datetime.now().year - data_nascimento.year)
    if idade < 18 or idade > 150:
        raise ValidationError('A idade deve ser entre 18 e 150 anos.')

class CadastroForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired(), Length(min=2, max=50)])
    data_nascimento = DateField('Data de Nascimento', format='%Y-%m-%d', validators=[DataRequired(), validar_data_nascimento])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    confirmacao_senha = PasswordField('Confirme sua Senha', validators=[DataRequired(), EqualTo('senha', message='As senhas devem coincidir')])
    submit = SubmitField('Cadastrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Logar')

class AutenticacaoForm(FlaskForm):
    codigo_verificacao = StringField('Digite o código de verificação', 
                                     validators=[DataRequired(), Length(min=6, max=6, message="O código deve ter 6 dígitos")])
    submit = SubmitField('Confirmar')
