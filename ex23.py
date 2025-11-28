#Desenvolva um código python com while
#em que o usuário digita um número
#e irá mostrar a tabuada deste número
#'''
v=int(input("Digite um número"))
i = 1
while i <= 10:
    print(f"{v} X {i} = {v * i}")
    i += 1