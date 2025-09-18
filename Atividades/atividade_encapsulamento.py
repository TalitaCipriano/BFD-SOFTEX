#11111111111111111111111111111111111111111111111111111111111111111

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email, tipo_cliente):  
        super().__init__(nome, email)  
        self.tipo_cliente = tipo_cliente

cliente1 = Cliente("Talita", "talita@talita.com", "ouro")

print(f"Nome: {cliente1.nome}, E-mail: {cliente1.email}, Cliente: {cliente1.tipo_cliente}")

#2222222222222222222222222222222222222222222222222222222222222222222222