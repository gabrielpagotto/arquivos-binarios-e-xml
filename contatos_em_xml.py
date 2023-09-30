import xml.etree.ElementTree as ET

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    root = ET.Element("contato")
    nome_element = ET.SubElement(root, "nome")
    nome_element.text = nome
    telefone_element = ET.SubElement(root, "telefone")
    telefone_element.text = telefone
    email_element = ET.SubElement(root, "email")
    email_element.text = email

    tree = ET.ElementTree(root)

    try:
        with open("contatos.xml", "rb") as arquivo:
            root = ET.fromstring(arquivo.read())
    except FileNotFoundError:
        root = ET.Element("contatos")

    root.append(tree.getroot())

    with open("contatos.xml", "wb") as arquivo:
        arquivo.write(ET.tostring(root))

    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    try:
        tree = ET.parse("contatos.xml")
        root = tree.getroot()

        print("\nLista de Contatos:")
        for contato in root:
            nome = contato.find("nome").text
            telefone = contato.find("telefone").text
            email = contato.find("email").text

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
