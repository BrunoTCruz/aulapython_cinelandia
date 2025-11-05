ano_nasc = int (input('Digite seu ano de nascimento: '))
genero = input('Entre com o genero: (M/F): ').upper()
#print(ano_nasc)
#print(genero)

#from datetime import datetime
# Traz o ano vigente
#ano_atual = datetime.now().year
idade = 2025-ano_nasc
if idade >= 18 and genero == 'M':
    print('Apto a se alistar')
else:
    print('Não apto a se alistar')
