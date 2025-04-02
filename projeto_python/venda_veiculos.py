print("""
CADASTRAR Veículo: O usuário pode inserir um novo veículo informando os detalhes necessários (modelo, ano, preço, etc.).

LISTAS Veículos: Exibe todos os veículos disponíveis no catálogo.

COMPRAR Veículo: Remove um veículo da lista, simulando a compra.

""")


veiculos = []  # Lista para armazenar os veículos
id_veiculo = 1  # Inicializa o ID dos veículos

# Função para cadastrar um novo veículo
def cadastrar_veiculo():
    global id_veiculo  # Acessa a variável global id_veiculo
    print("Cadastro de Veículo")
    marca = input("Digite a marca do veículo: ")
    modelo = input("Digite o modelo do veículo: ")
    ano = int(input("Digite o ano do veículo: "))
    preco = float(input("Digite o preço do veículo: "))

    # Cria o dicionário para o novo veículo
    veiculo = {"id": id_veiculo, "marca": marca, "modelo": modelo, "ano": ano, "preco": preco}

    veiculos.append(veiculo)  # Adiciona o veículo na lista usando append()
    print(f"Veículo cadastrado com sucesso! ID: {id_veiculo}\n")
    
    id_veiculo += 1  # Incrementa o ID para o próximo veículo

# Função para listar os veículos disponíveis
def listar_veiculos():
    print("Lista de Veículos Disponíveis")
    if not veiculos:
        print("Nenhum veículo cadastrado.\n")
    else:
        for v in veiculos:
            print(f"ID: {v['id']} | Marca: {v['marca']} | Modelo: {v['modelo']} | Ano: {v['ano']} | Preço: {v['preco']}")
        print()

# Função para vender um veículo
def vender_veiculo():
    listar_veiculos()
    if veiculos:
        id_veiculo = int(input("Digite o ID do veículo que deseja vender: "))

        # Verifica se o veículo existe
        for v in veiculos:
            if v['id'] == id_veiculo:
                veiculos.remove(v)  # Remove o veículo vendido da lista
                print("Veículo vendido com sucesso!\n")
                return  # Sai da função depois de vender o veículo

        print("Veículo não encontrado.\n")

# Exemplo de veículos cadastrados inicialmente
veiculos.append({"id": id_veiculo, "marca": "Ford", "modelo": "Mustang", "ano": 2022, "preco": 300000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "Chevrolet", "modelo": "Camaro", "ano": 2021, "preco": 280000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "Toyota", "modelo": "Corolla", "ano": 2023, "preco": 120000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "Honda", "modelo": "Civic", "ano": 2022, "preco": 130000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "Volkswagen", "modelo": "Golf", "ano": 2020, "preco": 110000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "BMW", "modelo": "M3", "ano": 2023, "preco": 400000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "Mercedes", "modelo": "C-Class", "ano": 2021, "preco": 350000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "Audi", "modelo": "A4", "ano": 2022, "preco": 320000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "Nissan", "modelo": "GT-R", "ano": 2019, "preco": 500000})
id_veiculo += 1
veiculos.append({"id": id_veiculo, "marca": "Hyundai", "modelo": "Elantra", "ano": 2020, "preco": 90000})
id_veiculo += 1

# Menu principal
while True:
    print("Sistema de Venda de Veículos")
    print("1 - Cadastrar Veículo")
    print("2 - Listar Veículos")
    print("3 - Vender Veículo")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_veiculo()
    elif opcao == "2":
        listar_veiculos()
    elif opcao == "3":
        vender_veiculo()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
