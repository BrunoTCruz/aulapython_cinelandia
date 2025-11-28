def dividir(a,b):
    try:
        #TESTE
        resultado = a / b
    except ZeroDivisionError:
        #ERRO
        print("Erro: Divisão por zero não é permitida!")
    except ValueError:
        print("Erro: Valor inválido Informado!")
    else:
        # EXECUTAR QUANDO NÃO HOUVER ERRO
        print(f"Resultado da Divisão: {resultado}")
    finally:
        #EXECUTAR SEMPRE
        print("Operação finalizada (com ou sem erro).")

    # Programação principal
    try:
        num1 = float(input("Digite um numeador> "))
        num2 =float(input("Digite o denominador: "))
        dividir(num1, num2)
    except ValueError:
        print("Voce deve digitar apenas números!")