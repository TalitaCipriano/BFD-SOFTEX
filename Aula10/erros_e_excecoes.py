# erro de sintaxe: ocorre quando o codigo possui algum erro ortografico, na escrita do codigo:
# parenteses, aspas, erros ortograficos.

# lidando com excecoes:
# try: testar erro
# except: 
# else:
# finally: quando quiser finalizar (desconectar) o contato com o banco de dados
# raise: editar a mensagem de erro (acicionar resolução do erro)

# try:
#     num1 = int(input("Informe o primeiro numero:"))
#     num2 = int(input("Informe o segundo numero:"))
#     soma = num1/num2
# except ZeroDivisionError:
#     print("O segundo numero tem que ser diferente de zero")
# except ValueError:
#     print("só informar núemros")
# except:
#     print('Algo deu errado, contate o suporte')
# else:
#     print(soma)
# finally:
#     print

# try:
#     idade = int(input("Informe a idade:"))
#     if idade <= 18:
#         raise ValueError("idade não compatível")
# except:
#     print("Apenas números")
# except Exception as erroIdade:
#     print(erroIdade)


class erroIdade (Exception):
    pass
try:
    idade = int(input("Informe a idade:"))
    if idade <= 0:
        raise Exception("idade tem que ser maior que zero")
except TypeError:
    print("Apenas números")
except erroIdade:
    print("Idade ")

