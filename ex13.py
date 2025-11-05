#Desenviolva um codigo python que leia 3 valores e mostre qual o maior
num1=int (input("Entre com o primeiro numero: "))
num2=int (input("Entre com o segundo numero: "))
num3=int (input("Entre com o terceiro numero: "))
#nome=nome1.upper()
#nome2=nome2.upper()
if (num1 > num2 and num1 > num3):
    print(f" O numero maior é o primeiro: {num1} ")
elif (num2 > num1 and num2 > num3):
    print(f" O numero maior é o segundo: {num2} ")
else:
    print(f" O numero maior é o terceiro: {num3} ")