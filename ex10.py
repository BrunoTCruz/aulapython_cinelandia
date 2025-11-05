#codigo python que verifica se um valor é maior que o outro
#o usuário deve digitar os dois valores

num1=int (input("Entre com o primeiro numero: "))
num2=int (input("Entre com o segundo numero: "))
#nome=nome1.upper()
#nome2=nome2.upper()
if (num1 > num2):
    print(f" O numero maior é {num1} ")
elif (num2 > num1):
    print(f" O numero maior é {num2} ")
else:
    print(" São Iguais ")