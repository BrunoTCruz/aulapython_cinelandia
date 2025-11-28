for i in range(1,11):
    print(i)
 
#imprimir um nome digitado 20 vezes na tela   
nome=input("Digite seu nome")
for i in range(0,20):
    print(nome)

soma=0
for i in range(1,11):
    #soma = soma + i
    soma += i
    print(soma)

soma = soma + i #é o mesmo que soma += i
#+= quer dizer que a variável recebe ela mesmo
#mais outro valor no caso mais o conteúdo de i

m=0
for i in range(0,5):
    x=int(input("Digite um valor "))
    m += x
    #m = m + x 
print(f"A soma dos números é {m}")
