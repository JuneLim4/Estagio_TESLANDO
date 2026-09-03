import os

# ls

pasta = input("Digite o caminho da pasta:\n ")

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


comando_cat()