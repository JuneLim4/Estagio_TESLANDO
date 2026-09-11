import requests

import smtplib
from email.message import EmailMessage
from getpass import getpass

#API

def conectar_api():

    url = "https://reqres.in/api/users"

    try:
        resposta = requests.get(url)

        if resposta.status_code == 200:
            print("Conexão realizada com sucesso!")

            dados = resposta.json()
            usuarios = dados["data"]

            return usuarios

        else:
            print("Não foi possível acessar a API.")

    except:
        print("Erro ao tentar conectar com a API.")

def salvar_usuarios(usuarios):

    with open("PYTHON/usuarios.txt", "w", encoding="utf-8") as arquivo:

        for usuario in usuarios:

            arquivo.write("------------------------\n")
            arquivo.write(f"Pessoa {usuario['id']}\n")
            arquivo.write("------------------------\n")

            arquivo.write(f"Nome: {usuario['first_name']}\n")
            arquivo.write(f"Sobrenome: {usuario['last_name']}\n")
            arquivo.write(f"E-mail: {usuario['email']}\n\n")


usuarios = conectar_api()

for usuario in usuarios:

    print("\n------------------------")
    print("Pessoa", usuario["id"])
    print("------------------------")

    print("Nome:", usuario["first_name"])
    print("Sobrenome:", usuario["last_name"])
    print("E-mail:", usuario["email"])

salvar_usuarios(usuarios)

print("\nArquivo usuarios.txt criado com sucesso!\n")

#Email

def verificar_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

def enviar_email():

    remetente = input("\nDigite o e-mail que vai enviar:\n")

    while not verificar_email(remetente):
        print("\nE-mail inválido! Digite um e-mail válido.")
        remetente = input("Digite o e-mail que vai enviar:\n")

    senha = getpass(
        "\nDigite a senha de app\n(digite sem espaço a senha!):\n "
    )

    destinatario = input("\nDigite o e-mail que vai receber:\n")

    while not verificar_email(destinatario):
        print("\nE-mail inválido! Digite um e-mail válido.")
        destinatario = input("Digite o e-mail que vai receber:\n")

    mensagem = EmailMessage()

    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = "Lista de usuários da API"

    mensagem.set_content("Olá! Segue em anexo a lista de usuários obtida pela API.")

    with open("PYTHON/usuarios.txt", "rb") as arquivo:
        conteudo = arquivo.read()

    mensagem.add_attachment(
        conteudo,
        maintype="text",
        subtype="plain",
        filename="usuarios.txt"
    )

    while True:
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
                servidor.starttls()
                servidor.login(remetente, senha)
                servidor.send_message(mensagem)

            print("\nE-mail enviado com sucesso!")
            break

        except:
            print("\nNão foi possível enviar o e-mail.")
            print("Verifique o e-mail e a senha de app e tente novamente.\n")

enviar_email()