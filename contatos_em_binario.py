import pickle

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    try:
        with open("contatos.bin", "rb") as arquivo:
            contatos = pickle.load(arquivo)
    except FileNotFoundError:
        contatos = []

    contatos.append(contato)

    with open("contatos.bin", "wb") as arquivo:
        pickle.dump(contatos, arquivo)

    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    try:
        with open("contatos.bin", "rb") as arquivo:
            contatos = pickle.load(arquivo)

        print("\nLista de Contatos:")
        for contato in contatos:
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]

            print(f"Nome: {nome}")
            print(f"Telefone: {telefone}")
            print(f"E-mail: {email}")
            print("-" * 20)
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

while True:
    print("\nMenu:")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        print("Saindo da aplicação.")
        break
    else:
        print("Opção inválida. Tente novamente.")
