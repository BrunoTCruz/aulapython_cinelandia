#Desenvolva um codido python que verifique se a temperatura esta frio, agradável ou calor.
#Siga a tabela abaixo:
#menor que 18 - Frio
#entre 18 e 30 - Agradável
#maior que 30 - Calor

temp=int (input("Entre com a temperatura: "))
if (temp < 18):
    print(f"Está Frio")
elif (temp > 18) and (temp <= 30):
    print(f"A temperatura está agradável ")
else: 
    print(f"Está calor") 