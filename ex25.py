#''' Desenvolva um código python usando while
#que digite um nome e imprima , só para o 
#programa ao digitar sair em maiusculo
#!= diferente
nome=""
while nome != "SAIR":
    nome=input("Digite um nome ").upper()
    if nome == "SAIR":
        break #sai do laço while
    print(f"Olá {nome}")
