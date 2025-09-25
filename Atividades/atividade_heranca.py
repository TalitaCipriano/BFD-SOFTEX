#111111111111 2222222222222 333333333333 4444444444444
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, E-mail: {self.email}"
    
    def saudacao(self):
        return f"Olá, usuário"

class Cliente(Usuario):
    def __init__(self, nome, email, tipo_cliente, saldo):  
        super().__init__(nome, email)  
        self.tipo_cliente = tipo_cliente
        self.saldo = saldo

    def saudacao(self):
        return f"Olá, cliente"

cliente1 = Cliente("Talita", "talita@talita.com", "ouro", 1500.00)

print(cliente1.saudacao())
print(cliente1.exibir_informacoes())
print(f"Tipo de cliente: {cliente1.tipo_cliente}, Saldo: R${cliente1.saldo:.2f}")

#555555555555555555555555555555555555555555555555555555555555

class Usuário:
    def __init__(self, nome, email, id):
        self.nome = nome
        self.email = email
        self.id = id

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, E-mail: {self.email}, ID: {self.id}"

class Funcionário(Usuário):
    def __init__(self, nome, email, id, cargo, salario):  
        super().__init__(nome, email, id)
        self.cargo = cargo
        self.salario = salario

    def exibir_informacoes(self):
        info_base = super().exibir_informacoes()
        return f"{info_base}, Cargo: {self.cargo}, Salário: R${self.salario:.2f}"

class Gerente(Funcionário):
    def __init__(self, nome, email, id, cargo, salario, departamento):  
        super().__init__(nome, email, id, cargo, salario)
        self.departamento = departamento

    def exibir_informacoes(self):
        info_funcionario = super().exibir_informacoes()
        return f"{info_funcionario}, Departamento: {self.departamento}"
    
gerente1 = Gerente("Talita", "talita@talita.com", "9273", "Gerente de TI", 14000, "Tecnologia da Informação")

print(gerente1.exibir_informacoes())
print(f"Nome: {gerente1.nome}")
print(f"Departamento: {gerente1.departamento}")

#666666666666666666666666666666666666666666666666666666666666666666
# Crie uma classe Autenticacao com um método login(). 
# Crie outra classe Permissao com um método verificar_permissao(). 
# Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?

class Autenticacao:
    def login(self, usuario, senha)
    self.usuario = usuario
    self.senha = senha

class Permissao:
    def __init__(self, verificar_permissao):
    self.verificar_permissao = verificar_permissao

class Administrador:
    def __init__(self,):
    super().__init__(login, verifcar_permissao)
        