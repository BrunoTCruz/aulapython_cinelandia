#EXERCICIO DE FUNÇÃO
def somar (a,b):
    return a+b

def subtrair(a,b):
    return a-b

def multi(a,b):
    return a*b

def divi(a,b):
    if b != 0:
       return a/b
    else:
        print("Valor inválido")

escolha = ""
while escolha !="0":
    escolha = input("Digite uma opção 0 - para paprr 1 - somar, 2 - subtrair. 3 - Multiplica. 4 - dividir ")
    num1= int(input("Digite o primeiro numero: "))
    num2= int(input("Digite o segundo numero: "))

    if escolha =="1":
        x=somar(num1,num2)
    elif escolha == "2":
        x=subtrair(num1,num2)
    elif escolha == "3":
        x=multi(num1,num2)
    elif escolha == "4":
        x=divi(num1,num2)    
    else:
        break

    print(f"resultado da operação: {x}")