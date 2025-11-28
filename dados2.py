import pandas as pd

#Listas vazias para armazenar os dados
cargos = []
salarios = []

#Quantos registros o usuário vai informar
qtd = int(input("Quaantos cargos deseja cadastrar ?"))

#coleta de dados
for i in range(qtd):
    print(f"Cadastro {i+1}")
    cargo = input("Digite o cargo: ")
    salario = float(input("Digite o salário: "))

    cargos.append(cargo)
    salarios.append(salario)


#Criação de Dataframe
dados = {'cargos': cargos, 'salarios': salarios}
dados_bi = pd.DataFrame(dados)

#Exibição do Dataframe Final
print("Tabela de Cargos e salário: ")
print(dados_bi)

