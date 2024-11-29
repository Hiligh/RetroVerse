@echo off

echo Instalando os pacotes Python necessários...

py --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python não foi encontrado. Por favor, instale o Python antes de executar este script.
    pause
    exit /b
)

echo Atualizando o pip...
py -m pip install --upgrade pip

echo Instalando pacotes...
py -m pip install blinker==1.8.2 certifi==2024.8.30 charset-normalizer==3.3.2 click==8.1.7 colorama==0.4.6 dnspython==2.6.1 email_validator==2.2.0 Flask==3.0.3 Flask-WTF==1.2.1 idna==3.8 itsdangerous==2.2.0 Jinja2==3.1.4 MarkupSafe==2.1.5 mysql-connector-python==9.0.0 pyotp==2.9.0 requests==2.32.3 urllib3==2.2.3 Werkzeug==3.0.4 WTForms==3.1.2

if %errorlevel% neq 0 (
    echo Ocorreu um erro durante a instalação dos pacotes.
    pause
    exit /b
)

echo Todos os pacotes foram instalados com sucesso!

cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"

echo Insira a senha do root MySql para a criação do banco retroverse:
mysql.exe -uroot -p -e "CREATE DATABASE IF NOT EXISTS retroversedb;"

echo Procurando pelo arquivo de dump...

set "dump_file="
for /f "delims=" %%f in ('dir C:\Dump*.sql /s /b /a-d 2^>nul') do (
    set "dump_file=%%f"
    goto :found_dump
)

echo Arquivo de dump não encontrado no sistema.
pause
exit /b

:found_dump
echo Arquivo de dump localizado: %dump_file%

echo Insira a senha do root do MySQL para a restauração no banco retroverse:
mysql.exe -uroot -p retroversedb < "%dump_file%"

pause

