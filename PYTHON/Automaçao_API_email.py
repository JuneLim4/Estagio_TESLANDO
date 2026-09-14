import requests
import smtplib

from email.message import EmailMessage
from getpass import getpass


# API

def conectar_api():

    url = "https://reqres.in/api/users"

    try:

        resposta = requests.get(url, timeout=10)

        if resposta.status_code == 200:

            print("Conexão realizada com sucesso!")

            dados = resposta.json()

            usuarios = dados["data"]

            return usuarios

        else:

            print("Não foi possível acessar a API.")
            print("Código do erro:", resposta.status_code)

            return None

    except requests.exceptions.Timeout:

        print("A API demorou muito para responder.")

        return None

    except requests.exceptions.RequestException:

        print("Erro ao tentar conectar com a API.")

        return None


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

if usuarios:

    for usuario in usuarios:

        print("\n------------------------")
        print("Pessoa", usuario["id"])
        print("------------------------")
        print("Nome:", usuario["first_name"])
        print("Sobrenome:", usuario["last_name"])
        print("E-mail:", usuario["email"])

    salvar_usuarios(usuarios)

    print("\nArquivo usuarios.txt criado com sucesso!\n")

else:

    print("\nNão foi possível continuar porque a API não retornou os usuários.")


# Email

def verificar_email(email):

    if "@" in email and "." in email and " " not in email:

        return True

    else:

        return False


def enviar_email():

    while True:

        remetente = input("\nDigite o e-mail que vai enviar:\n")

        while not verificar_email(remetente):

            print("\nE-mail inválido! Digite um e-mail válido.")

            remetente = input("Digite o e-mail que vai enviar:\n")

        senha = getpass(
            "\nDigite a senha de app\n"
            "(digite sem espaço a senha!):\n "
        )

        destinatario = input(
            "\nDigite o e-mail que vai receber:\n"
        )

        while not verificar_email(destinatario):

            print("\nE-mail inválido! Digite um e-mail válido.")

            destinatario = input(
                "Digite o e-mail que vai receber:\n"
            )

        mensagem = EmailMessage()

        mensagem["From"] = remetente
        mensagem["To"] = destinatario
        mensagem["Subject"] = "Lista de usuários da API"

        mensagem.set_content(
            "Olá! Segue em anexo a lista de usuários obtida pela API."
        )

        with open("PYTHON/usuarios.txt", "rb") as arquivo:

            conteudo = arquivo.read()

        mensagem.add_attachment(
            conteudo,
            maintype="text",
            subtype="plain",
            filename="usuarios.txt"
        )

        try:

            with smtplib.SMTP("smtp.gmail.com", 587) as servidor:

                servidor.starttls()

                servidor.login(remetente, senha)

                servidor.send_message(mensagem)

            print("\nE-mail enviado com sucesso!")

            break

        except smtplib.SMTPAuthenticationError:

            print("\nNão foi possível entrar no e-mail.")
            print("Verifique o e-mail e a senha de app e tente novamente.")

        except smtplib.SMTPException:

            print("\nOcorreu um erro ao tentar enviar o e-mail.")
            print("Tente novamente.")


if usuarios:

    enviar_email()