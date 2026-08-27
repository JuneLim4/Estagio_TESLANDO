while True:
    try:
        inicio = int(input("Digite o número inicial: "))
        fim = int(input("Digite o número final: "))
        intervalo = int(input("Digite o intervalo (não pode ser 0): "))

        if intervalo == 0:
            print("O intervalo não pode ser zero!")
            continue

        print("\nResultado da contagem:")

        if inicio <= fim:

            if intervalo < 0:
                intervalo = -intervalo

            for numero in range(inicio, fim + 1, intervalo):
                print(numero)

        else:
            print("OBS: o o início é maior que o fim, o intervalo será invertido para negativo.")

            if intervalo > 0:
                intervalo = -intervalo

            for numero in range(inicio, fim - 1, intervalo):
                print(numero)

    except ValueError: #caso o usuário digite algo que não seja um número inteiro
        print("Digite apenas números inteiros!")

    print()
