# FUNCOES
# é um bloco de código pra utilizar a qualquer momento apenas chamando a função

# CRIAR FUNÇÃO
# def nome_funcao():
#     código

# exemplo:
# def saudacao():
#     print("Olá, tudo bem?")

# CHAMANDO A FUNÇÃO

#só precisa chamar o nome da função

# exemplo:
# saudacao()

# RETURN

#usamos para guardar a funcao e utilizar posteriormente (salvando/atrelando essa função sempre a uma variavel)
# def saudacao():
#     return "olá, tudo bem?"

# print(saudacao())
# msg_saudacao = saudacao()
# print(msg_saudacao)

# def soma (nun1, num2):
#     return nun1+num2
# def multiplicacao (num1, num2):
#     return num1*num2

# adicao = soma(2,3) * soma (5,8)
# operacao = multiplicacao (soma(2,3),soma(5,8))
# print(operacao)

# def calculadora (num1, num2)

def soma (*nuns):
    resultado = 0
    for numero in nuns:
        resultado += numero
        return resultado

soma (5,6,1,9,3)
