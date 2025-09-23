#11111111111111111111111111111111111111111111111111111111111111111

# class Usuario:
#     def __init__(self, nome, email):
#         self.nome = nome
#         self.email = email

# class Cliente(Usuario):
#     def __init__(self, nome, email, tipo_cliente):  
#         super().__init__(nome, email)  
#         self.tipo_cliente = tipo_cliente

# cliente1 = Cliente("Talita", "talita@talita.com", "ouro")

# print(f"Nome: {cliente1.nome}, E-mail: {cliente1.email}, Cliente: {cliente1.tipo_cliente}")

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
