#11111111111111111111111111111111111111111111111111111111111111111
Na classe, ContaBancaria, converta saldo para uma atributo privado. 
Crie um método setter e um getter para acessar e modificar essa atributo, seguindo uma regra lógica (Ex: saldo não pode ser negativo)

class ContaBancaria:
    def __init__(self, nome, agencia, conta, saldo)
        self.nome = nome
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo_inicial 
            if saldo_inicial >= 0 
            else 0

    def get__saldo(self):
        return self.__saldo

    def set_saldo(self, saldo):
        if valor < 0:
            print("Erro: saldo não pode ser negativo.")
        else:
            self.__saldo = valor

conta.set_saldo(500)
print(conta.get_saldo())

     

#2222222222222222222222222222222222222222222222222222222222222222222222

class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, rg):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__cpf = cpf
        self.__rg = rg

    def get__cpf(self):
        return self.__cpf
    
    def get__rg(self):
        return self.__rg

    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def set_rg(self, rg):
        self.__rg = rg

pessoa = Pessoa("Talita", "13/12/1988", "000.000.000-00", "0000000")
print(pessoa.nome)
print(pessoa.data_nascimento)
print(pessoa.get__cpf())
print(pessoa.get__rg())

pessoa.set_cpf("111.111.111-11")
pessoa.set_rg("1111111")
print(pessoa.get__cpf())  
print(pessoa.get__rg())  
