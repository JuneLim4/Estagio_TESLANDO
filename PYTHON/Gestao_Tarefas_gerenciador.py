import mysql.connector
from getpass import getpass

senha = getpass("Digite a senha do MySQL:\n")

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=senha,
    database="gerenciador_tarefas"
)

cursor = conexao.cursor()


# CREATE 

def criar_tarefa():
    print("\n----- CRIAR TAREFA -----")

    titulo = input("Título:\n")
    descricao = input("Descrição:\n")
    data_conclusao = input("Data de conclusão (AAAA-MM-DD HH:MM:SS):\n")
    usuario_id = input("ID do usuário:\n")

    sql = """
    INSERT INTO tarefas
    (titulo, descricao, data_criacao, data_conclusao, usuario_id)
    VALUES (%s, %s, NOW(), %s, %s)
    """

    cursor.execute(sql, (titulo, descricao, data_conclusao, usuario_id))
    conexao.commit()

    print("Tarefa criada com sucesso!")

# READ 

def visualizar_tarefas():
    print("\n----- TAREFAS -----")

    sql = """
    SELECT tarefas.id,
           tarefas.titulo,
           tarefas.descricao,
           tarefas.data_criacao,
           tarefas.data_conclusao,
           usuarios.nome
    FROM tarefas
    INNER JOIN usuarios
    ON tarefas.usuario_id = usuarios.id
    """

    cursor.execute(sql)

    tarefas = cursor.fetchall()

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        for tarefa in tarefas:
            print("-------------------------")
            print("ID:", tarefa[0])
            print("Título:", tarefa[1])
            print("Descrição:", tarefa[2])
            print("Data de criação:", tarefa[3])
            print("Data de conclusão:", tarefa[4])
            print("Usuário:", tarefa[5])

# UPDATE 

def atualizar_tarefa():
    print("\n----- ATUALIZAR TAREFA -----")

    id_tarefa = input("Digite o ID da tarefa:\n")
    novo_titulo = input("Novo título:\n")
    nova_descricao = input("Nova descrição:\n")
    nova_data = input("Nova data de conclusão (AAAA-MM-DD HH:MM:SS):\n")


    sql = """
    UPDATE tarefas
    SET titulo = %s,
        descricao = %s,
        data_conclusao = %s
    WHERE id = %s
    """

    cursor.execute(
        sql,
        (novo_titulo, nova_descricao, nova_data, id_tarefa)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Tarefa atualizada com sucesso!")
    else:
        print("Tarefa não encontrada.")

# DELETE 

def excluir_tarefa():
    print("\n----- EXCLUIR TAREFA -----")

    id_tarefa = input("Digite o ID da tarefa: ")

    sql = "DELETE FROM tarefas WHERE id = %s"

    cursor.execute(sql, (id_tarefa,))
    conexao.commit()

    if cursor.rowcount > 0:
        print("Tarefa excluída com sucesso!")
    else:
        print("Tarefa não encontrada.")

# Menu

while True:
    print("\n----- GERENCIADOR DE TAREFAS -----")
    print("1 - Criar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Excluir tarefa")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_tarefa()

    elif opcao == "2":
        visualizar_tarefas()

    elif opcao == "3":
        atualizar_tarefa()

    elif opcao == "4":
        excluir_tarefa()

    elif opcao == "5":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")


cursor.close()
conexao.close()