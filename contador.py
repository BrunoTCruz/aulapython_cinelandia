#Crie uma função que receba uma palavra (string) e retorne o número de vogais que ela contém.
vogais ="aeiouAEIO"
def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

l = contar_vogais(vogais)

# Interação com o usuário
palavra_digitada = input("Digite uma palavra: ")

# Chamada da função e exibição do resultado
num_vogais = contar_vogais(palavra_digitada)
print(f"A palavra '{palavra_digitada}' tem {num_vogais} vogais.")


#vogais ="aeiouAEIO"
#def contar_vogais(palavra):
#    contador = 0
#    for letra in palavra:
#        if letra in vogais:
#            contador += 1
#    return contador

#l = contar_vogais(vogais)
#print(f"A palavra {vogais} tel {l} Letras ")