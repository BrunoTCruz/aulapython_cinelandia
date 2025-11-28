#Leia duas notas, calcule a média e trate erros de entrada (valo invalido ou divisão incorreta) .
def calcular_media(nota1, nota2):
#Interação com o usuário
    try:
        nota1 = float(input("Digite a primeira nota1: "))
        nota2 = float(input("Digite a segunda nota2: "))
        media = (nota1 + nota2 ) / 2
    except ValueError:
        print("Erro: Digite apenas números válidos! ")
    else:
        print(f"média calculada: {media:.2f}")
    finally:
        print("Fim do cálculo de média.")
calcular_media()