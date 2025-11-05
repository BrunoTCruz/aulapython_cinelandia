#codigo python que leia um valor e verifica se é positivo, negativo ou 0
num1=int (input("Entre com um numero: "))
#nome=nome1.upper()
#nome2=nome2.upper()
if (num1 > 0):
    print(f" O numero é maior que 0 ")
elif (num1 < 0):
    print(f" O numero é menor que 0 ")
else:
    print(" O numero é 0  ")