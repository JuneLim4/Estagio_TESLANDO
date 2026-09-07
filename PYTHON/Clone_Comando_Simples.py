import os

# ls

def comando_ls():

    pasta = input("\nDigite o caminho da pasta:\n(Digite . caso queira ver quais pastas já existem!)\n")

    if os.path.isdir(pasta):

        print("\nArquivos encontrados:\n")

        arquivos = os.listdir(pasta)

        for arquivo in arquivos:

            if os.path.isdir(os.path.join(pasta, arquivo)):
                print(arquivo, "-> pasta")

            else:
                print(arquivo, "-> arquivo")

        escolha = input("\nDigite a pasta que deseja abrir:\n")

        nova_pasta = os.path.join(pasta, escolha)

        if os.path.isdir(nova_pasta):

            print("\nConteúdo da pasta:\n")

            arquivos = os.listdir(nova_pasta)

            for arquivo in arquivos:

                if os.path.isdir(os.path.join(nova_pasta, arquivo)):
                    print(arquivo, "-> pasta")

                else:
                    print(arquivo, "-> arquivo")

        else:
            print("\nPasta não encontrada.\n")

    else:
        print("\nPasta não encontrada.\n")


# cat

def comando_cat():

    arquivo = input("\nDigite o nome do arquivo:\n")

    if os.path.isfile(arquivo):

        try:

            with open(arquivo, "r") as arquivo_aberto:

                conteudo = arquivo_aberto.read()

                print("\nConteúdo do arquivo:\n")

                print(conteudo)

        except:

            print("\nErro ao ler o arquivo.\n")

    else:
        print("\nArquivo não encontrado.\n")


# tee

def comando_tee():

    print("\nO que você deseja criar?")

    print("1 - Arquivo")
    print("2 - Pasta")
    print("0 - Voltar")

    escolha = input("\nEscolha uma opção: ")

    if escolha == "0":
        return

    elif escolha == "1":

        # Arquivo

        while True:

            print("\nDigite o caminho da pasta onde deseja criar o arquivo.")
            print("(Digite 0 para voltar)")

            local = input("\nCaminho: ")

            if local == "0":
                return

            if os.path.isdir(local):
                break

            print("\nPasta não encontrada. Tente novamente.\n")

        nome = input("\nQual será o nome do arquivo que deseja criar?\n")

        caminho = os.path.join(local, nome)

        conteudo = input("\nDigite o conteúdo a ser escrito no arquivo:\n")

        try:

            with open(caminho, "w") as arquivo_aberto:

                arquivo_aberto.write(conteudo)

            print("\nArquivo criado com sucesso.\n")

        except:

            print("\nNão foi possível criar o arquivo.\n")

    elif escolha == "2":

        # Pasta

        nome = input("\nQual será o nome da nova pasta que deseja criar?\n")

        try:

            os.mkdir(nome)

            print("\nPasta criada com sucesso.\n")

        except:

            print("\nNão foi possível criar a pasta. Ela pode já existir.\n")

    else:

        print("\nOpção inválida.\n")


# rm

def comando_rm():

    arquivo = input("\nDigite o caminho do arquivo que deseja remover:\n")

    if os.path.isfile(arquivo):

        confirmacao = input("\nTem certeza que deseja remover o arquivo? (s/n): ")

        if confirmacao.lower() == "s":

            try:

                os.remove(arquivo)

                print("\nArquivo removido com sucesso.\n")

            except:

                print("\nNão foi possível remover o arquivo.\n")

        else:

            print("\nRemoção cancelada.\n")

    else:

        print("\nArquivo não encontrado.\n")


# Menu

while True:

    print("\n------------------------")
    print("       MEU TERMINAL")
    print("------------------------")

    print("1 - ls   -> listar arquivos e pastas")
    print("2 - cat  -> ler um arquivo")
    print("3 - tee  -> criar/escrever em um arquivo")
    print("4 - rm   -> remover um arquivo")
    print("5 - sair")

    escolha = input("\nEscolha um comando: ")

    if escolha == "1":

        comando_ls()

    elif escolha == "2":

        comando_cat()

    elif escolha == "3":

        comando_tee()

    elif escolha == "4":

        comando_rm()

    elif escolha == "5":

        print("\nPrograma encerrado.")

        break

    else:

        print("\nOpção inválida.\n")