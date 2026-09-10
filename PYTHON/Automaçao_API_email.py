import requests

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

print("\nArquivo usuarios.txt criado com sucesso!")