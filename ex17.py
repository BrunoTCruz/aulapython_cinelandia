#desenvolva um cod python que leia um cargo de funcionario, de acordo com o cargo mostre o salario  vide tabela abaixo
#caixa - 1500
#vendedor - 2400
#gerente - 4000
# de acordo com os salarios acima calcule :
# inss = 12% sobre o salario
#irrf se o salario for maior que 2000 o irrf será de 14% sobre o salario, senão será de 8%
#salario final = salario - irrf - inss

cargo=input("Entre com o cargo do funcionario: ").upper()
if (cargo=="CAIXA"):
    sal=1500
elif (cargo=="VENDEDOR"):
    sal=2400
elif (cargo=="GERENTE"):
    sal=4000
else:
    sal=0
    print("cargo não existe !!")
inss = sal * 0.12
if (sal > 2000):
    irrf = sal * 0.14
else:
    irrf = sal * 0.08
salfinal = sal - irrf - inss    
print(f"O seu salário é {sal}")
print(f"inss {inss}")
print(f"irrf {irrf}")
print(f"salario final é {salfinal}")
print(f" A compsição do seu salário se deu por {sal} - {irrf} - {inss}")