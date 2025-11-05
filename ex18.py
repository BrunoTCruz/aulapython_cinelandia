#uma loja de produtos tecnologicos te contratou para desenvolver um codigo da seguinte forma:
#Leia um produto e de acordo com o produto verifique o preço. (vide tabela abaxo)
#produtos - Preço
#mouse - 10
#teclado - 20
#memoria - 100
#e leia ainda a quantidade de produtos comprados:
#calcule:
#total = preço * quantidade
#imposto = se a quantidade for maior que 10 calcule um imposto de 5% sobre o total senão calcule 10%
#valor final = total + imposto 

produto=input("Entre com o produto: ").upper()
if (produto=="MOUSE"):
    preco=10
elif (produto=="TECLADO"):
    preco=20
elif (produto=="MEMORIA"):
    preco=100
else:
    preco=0
    print("Produto não existe !!")
qtde=int (input("Entre com a quantidade de produto: "))
vlrtotal = preco * qtde
if (qtde > 10):
    imposto = vlrtotal * 0.05
else:
    imposto = vlrtotal * 0.1
Valorfinal = vlrtotal + imposto
print(f"Produto {produto}")
print(f"Preço {preco}")
print(f"Quantodade {qtde}")
print(f"Imposto {imposto}")  
print(f"O valor final é: {Valorfinal}")