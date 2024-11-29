# **RetroVerse**

Esse projeto é feito com o intuito de aprender as técnicas da disciplina de gerência de projetos.

## Como usar

### Configurando os pacotes:
- Após baixar o zip e extrair o arquivo no disco C: (O zip deve ser extraido em alguma pasta do disco C:) execute o arquivo ScriptDeInstalação para baixar todas as dependências.

- O processo de localizar o arquivo dump pode demorar um pouco.

- Agora, após o término da instalação do script, na pasta data no arquivo conectarDB.py:
  
  ![image](https://github.com/user-attachments/assets/0c96cd8c-f554-4dce-91a2-3a55bfdaf714)

- na parte password, altere a senha "1234" para a senha que o seu root do MySQL possui:
  
  ![image](https://github.com/user-attachments/assets/9d7c4a07-fcd2-4743-a496-bc5a474bb132)



### Rodando o programa
- No terminal, para rodar o programa, se utiliza o comando:
~~~python
flask --app server run --debug
~~~

- Após executar o comando, no link disponibilizado após o running, segure ctrl e aperte em cima do link:
  - ![image](https://github.com/user-attachments/assets/632bce13-a1f3-4eb0-acb6-f423a7997e85)


- Ou apenas vá no arquivo server.py e rode o programa normalmente(usando o vscode com a extensão do python instalada).
  - ![image](https://github.com/user-attachments/assets/591f0fde-3217-4659-88e6-f3efe6aac7cd)

  - OBS: Caso dê erros executando o sistema utilizando a extensão do python, é problema da própria extensão. Apenas utilize o comando:
  ~~~python
  flask --app server run --debug
  ~~~

## Caso o ScriptDeInstação não funcione, faça os seguintes passos:

### Lista de dependências:
- Certifique-se se o python está instalado no seu computador, indo no terminal e usando um dos comandos:
~~~python
python --version

Ou

py --version
~~~
- Caso não apareça, instale manualmente o python com a versão mais recente, pelo site:
  - https://www.python.org/downloads/

- Use o comando pip install para instalar as dependências:
~~~python
pip install dependência
~~~

- Instale as seguintes dependências manualmente:
  
  - ﻿blinker==1.8.2
  - certifi==2024.8.30
  - charset-normalizer==3.3.2
  - click==8.1.7
  - colorama==0.4.6
  - dnspython==2.6.1
  - email_validator==2.2.0
  - Flask==3.0.3
  - Flask-WTF==1.2.1
  - idna==3.8
  - itsdangerous==2.2.0
  - Jinja2==3.1.4
  - MarkupSafe==2.1.5
  - mysql-connector-python==9.0.0
  - pyotp==2.9.0
  - requests==2.32.3
  - urllib3==2.2.3
  - Werkzeug==3.0.4
  - WTForms==3.1.2

- Crie o banco de dados no MySQL com o nome retroversedb usando o usuário root
- Após isso, pegue o arquivo Dump.sql que está dentro do zip, e restaure ele no banco criado.
- Imagem de demonstração:
  - ![image](https://github.com/user-attachments/assets/e2c35fbc-2f15-4774-a8a6-9af3c9813e3b)
    
  - Link do tutorial:
    - https://phoenixnap.com/kb/how-to-backup-restore-a-mysql-database

- Agora, após o término da instalação do script, na pasta data no arquivo conectarDB.py:
  
  ![image](https://github.com/user-attachments/assets/0c96cd8c-f554-4dce-91a2-3a55bfdaf714)

- na parte password, altere a senha "1234" para a senha que o seu root do MySQL possui:
  
  ![image](https://github.com/user-attachments/assets/9d7c4a07-fcd2-4743-a496-bc5a474bb132)


### Rodando o programa
- No terminal, para rodar o programa, se utiliza o comando:
~~~python
flask --app server run --debug
~~~

- Ou apenas vá no arquivo server.py e rode o programa normalmente(usando o vscode com a extensão do python instalada).
