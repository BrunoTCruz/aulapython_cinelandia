#r % 2 = pega o resto da divisão por 2
#exemplo
a=int(input("Digite um valor "))
r = a % 2
if r == 0:
    print(f"{a} é par")
else:
    print(f"{a} é impar")

#tabuada

v=int(input("Digite um valor => "))
for i in range(1,11):
    print(f"{v} X {i} = {v * i}")

#exercicio 26

for i in range(0,5):
    n=int(input("Digite um valor"))
    if n % 2 == 0:
        print(f"o valor {n} é par")
    else:
        print(f"o valor {n} é impar")

#Lista em python tambem pode se chamar array

frutas = ["maçã", "banana", "uva", "laranja"]
print("Minhas frutas favoritas são:")
for fruta in frutas:
     print(f"- Eu gosto de {fruta}.")

#exercício

numeros = [10,20,30,40,50]
print("Números:")
for numero in numeros:
     print(f"- Os números da listagem são {numero}.")

