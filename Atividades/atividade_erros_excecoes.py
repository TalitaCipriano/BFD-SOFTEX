# 11111111111111111111111111111111111111111111111111111111111111111111111111111111111

# try:
#     idade = int(input("Digite sua idade: "))
# except ValueError:
#     print("Apenas números")

# 222222222222222222222222222222222222222222222222222222222222222222222222222222222222

# try:
#     num1 = int(input("Digite o primeiro número:"))
#     num2 = int(input("Digite o segundo número:"))

#     resultado = num1*num2
# except ValueError:
#     print("só informar números")

# 33333333333333333333333333333333333333333333333333333333333333333333333333333333333333

# try:
#      num1 = int(input("Digite o primeiro número:"))
#      num2 = int(input("Digite o segundo número:"))
#      resultado = num1*num2

# except ValueError:
#      print("só informar números")
# else:
#      print(resultado)

# 444444444444444444444444444444444444444444444444444444444444444444444444444444444444444

# try:
#     arquivo = open("dados.txt")
#     print("arquivo encontrado")
# except FileNotFoundError:
#     print("arquivo não encontrado")
# finally:
#     print("Encerrando programa")

# 5555555555555555555555555555555555555555555555555555555555555555555555555555555555555555
    
# def dividir (a,b):  
#     if b == 0:
#         raise ZeroDivisionError("o segundo número tem que ser maior que zero")
#     return a/b
# try:
#     a = int(input("Digite o primeiro número:"))
#     b = int(input("Digite o segundo número:"))
#     resultado = a/b
# except ZeroDivisionError as e:
#     print(e)
# print(resultado)

# 66666666666666666666666666666666666666666666666666666666666666666666666666666666666666666

# class IdadeInvalidaError(Exception):
#     pass

# def cadastrar_idade(idade):
#     if idade < 0:
#         raise IdadeInvalidaError("Idade não pode ser negativa.")
#     print(f"Idade {idade} cadastrada com sucesso.")

# try:
#     idade_input = int(input("Digite a sua idade: "))
#     cadastrar_idade(idade_input)
# except IdadeInvalidaError as e:
#     print(f"Erro: {e}")

# 777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777

# def dividir (a,b):  
#      if b == 0:
#          raise ZeroDivisionError("o segundo número tem que ser maior que zero")
#      return a/b
# try:
#     a = int(input("Digite o primeiro número:"))
#     b = int(input("Digite o segundo número:"))
#     resultado = a/b
#     print(resultado)
# except ZeroDivisionError:
#      print("o segundo número tem que ser maior que zero")
# except ValueError:
#      print("Insira número válido")

# 888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888

# try:
#     num = int(input("Digite um número inteiro: "))
# except ValueError:
#     print("Isso não é um número inteiro válido.")
# else:
#     if num % 2 == 0:
#         print(f"{num} é par.")
#     else:
#         print(f"{num} é ímpar.")
# finally:
#     print("Fim do programa.")

#99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999


# class SaldoInsuficienteError(Exception):
#     pass

# def sacar(saldo, valor):
#     if valor > saldo:
#         raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
#     return saldo - valor

# try:
#     saldo_atual = float(input("Digite o saldo da conta: R$ "))
#     valor_saque = float(input("Digite o valor do saque: R$ "))
    
#     novo_saldo = sacar(saldo_atual, valor_saque)
#     print(f"Saque realizado com sucesso! Novo saldo: R$ {novo_saldo:.2f}")
# except ValueError:
#     print("Por favor, digite valores numéricos válidos.")
# except SaldoInsuficienteError as e:
#     print(f"Erro: {e}")

