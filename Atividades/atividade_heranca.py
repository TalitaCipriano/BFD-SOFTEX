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

#666666666666666666666  e  777777777777777777777777777

class Autenticacao:
    def login(self, usuario, senha):
        if usuario == "admin" and senha == "1234":
            print("Login bem-sucedido!")
            return True
        else:
            print("Falha no login!")
            return False

    def status(self):
        print("Status de Autenticacao")

class Permissao:
    def verificar_permissao(self, usuario):
        if usuario == "admin":
            print("Permissão concedida.")
            return True
        else:
            print("Permissão negada.")
            return False

    def status(self):
        print("Status de Permissao")

class Administrador(Autenticacao, Permissao):
    pass

admin = Administrador()
admin.status()  # Vai chamar qual?

print(Administrador.__mro__)

