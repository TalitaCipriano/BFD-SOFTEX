# 11111111111111111111111111111111111111111111111111111111111111

# def saudacao():
#     print("Olá, bem-vindo ao Python!")

# saudacao()

# 222222222222222222222222222222222222222222222222222222222222222

# num = int(input("Digite um número:"))

# def dobro(num):
#     print(num*2)

# dobro(num)

# 3333333333333333333333333333333333333333333333333333333333333333

# a = 10
# b = 20
# def soma(a, b):
#     return a + b

# resultado = soma(10, 20)
# print("Resultado da soma:", resultado)

# 44444444444444444444444444444444444444444444444444444444444444444

# def mensagem(nome=None):
#     if nome:
#       print(f"Olá, {nome}!")
#     else:
#       print("Olá, visitante!")
      
# mensagem("Thiago")
# mensagem(None)

# 55555555555555555555555555555555555555555555555555555555555555555

# a=int(input("digite o primeiro número:"))
# b=int(input("digite o segundo número:"))

# def operacoes(a, b):
#     soma = a+b
#     subtracao = a-b
#     multiplicacao = a*b
#     return soma, subtracao, multiplicacao

# resultado = operacoes(a, b)
# print(resultado)
# print("Soma:", resultado[0])
# print("Subtração:", resultado[1])
# print("Multiplicação:", resultado[2])

# 66666666666666666666666666666666666666666666666666666666666666666

# def media(*numeros):
#     if len(numeros) == 0:
#         return 0  # Evita divisão por zero
#     return sum(numeros) / len(numeros)

# print(media (6,8,3))
# print(media (5,12,9,11,15))
# print(media (3,4,8,16,10,13,9))

# 7777777777777777777777777777777777777777777777777777777777777777777

# def dados_pessoais(**kwargs):
#     informacoes = [f"{chave}: {valor}" for chave, valor in kwargs.items()]
#     print("\n".join(informacoes))

# dados = {"Nome": "Thiago", "Idade": 15, "Cidade": "Jaboatão"}

# dados_pessoais(**dados)

#88888888888888888888888888888888888888888888888888888888888888888888


# a=int(input("digite o primeiro número:"))
# b=int(input("digite o segundo número:"))

# def calculadora(a, b, operacao):
#     def somar(a, b):
#         return a + b

#     def subtrair(a, b):
#         return a - b

#     def multiplicar(a, b):
#         return a * b

#     def dividir(a, b):
#         if b == 0:
#             return "Erro: divisão por zero"
#         return a / b

#     if operacao == "soma":
#         return somar(a, b)
#     elif operacao == "subtracao":
#         return subtrair(a, b)
#     elif operacao == "multiplicacao":
#         return multiplicar(a, b)
#     elif operacao == "divisao":
#         return dividir(a, b)
    
# print("Soma:", calculadora(a, b, "soma"))
# print("Subtração:", calculadora(a, b, "subtracao"))
# print("Multiplicação:", calculadora(a, b, "multiplicacao"))
# print("Divisão:", calculadora(a, b, "divisao"))

#99999999999999999999999999999999999999999999999999999999999999999999999

# a=int(input("digite o primeiro número:"))
# b=int(input("digite o segundo número:"))

# def soma(a, b):
#     return a + b

# def aplicar_operacao(a, b, operacao):
#     return operacao(a, b)

# resultado = aplicar_operacao(a, b, soma)
# print("Resultado:", resultado)