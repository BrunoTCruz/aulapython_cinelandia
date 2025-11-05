#Desenvolva um codigo python que verifique se digitou m ou f, masculino para m e feminino para f, caso seja diferente de um dos dois, diga indefinido. 
genero=input("Digite seu genero (m ou f)").upper()
#nome=nome1.upper()
#nome2=nome2.upper()
if (genero=="M"):
    print("Seu genero é Masculino")
elif(genero=="F"):
    print("Seu genero é Feminino")
else:
    print("Seu genero é Indefinido")
