senha_correta = "python123"
tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
    tentativa = input(f"Digite a senha (Tentativa {tentativas + 1}/{max_tentativas}): ")
    if tentativa == senha_correta:
        print("Acesso concedido! Bem-vindo.")
        break 
    else:
        print("Senha incorreta.")
        tentativas += 1
        
else: 
    print("Você excedeu o número máximo de tentativas. Acesso bloqueado.")

#tratamento de exceção com try

nota = 0
while nota >= 0 and nota <= 10:
    try:
        nota = int(input("Digite uma nota entre 0 e 10: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
print(f"Nota válida registrada: {nota}")
