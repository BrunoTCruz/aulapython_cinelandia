#Peça dois numeros e yma operação. Use try-except-else-finally para tratar erros
#como divisão por zero e operação inválida.
#utilize a estrutura match case para decidir com os caracteres abaixo suas respectivas operações
#+ adição
#- subtração
#x miltiplicação
#/divisão

#Leia duas notas, calcule a média e trate erros de entrada (valo invalido ou divisão incorreta) .
def calculadora():
#Interação com o usuário
    try:
        a = float(input("Digite a primeiro numero: "))
        b = float(input("Digite a segundo numero: "))
        op = input("Digite a operação (+, -, *, /):")

        match op:
            case '+':
                resultado = a + b
            case '-':
                resultado = a - b
            case '*':
                resultado = a * b
            case '/':
                resultado = a / b
            case _:
                raise ValueError ("Operação Inválida")
    
    except ZeroDivisionError:
        print("Erro: divisão por zero !")
    except ValueError as e:
        print(f"{e}")
    else:
        print(f"resultado: {resultado}")
    finally:
        print("cálculo encerrado.")
calculadora()
