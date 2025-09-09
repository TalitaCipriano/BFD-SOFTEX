#11111111111111111111111111111111111111111111111111111111111111
class Pessoa:...
class Pessoa:
    def __init__(self, nome, idade):
       self.nome= nome
       self.idade= idade

p1 = Pessoa("Laís", 23)
p2 = Pessoa("Thiago", 27)

print(f"Nome: {p1.nome}, Idade:{p1.idade}")
print(f"Nome: {p2.nome}, Idade:{p2.idade}")

#222222222222222222222222222222222222222222222222222222222222

class Pessoa:
  def __init__(self, nome, idade):
       self.nome= nome
       self.idade= idade
  def apresentar(self):
    return (f"Olá, meu nome é {p1.nome} e tenho {p1.idade} anos")
  
p1 = Pessoa("Laís", 23)
p2 = Pessoa("Thiago", 27)
  
print(p1.apresentar())

#333333333333333333333333333333333333333333333333333333333333333

class Carro:...
class Carro:
   def __init__(self, marca, modelo, ano):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano

carro1 = Carro("Toyota", "SW4", 2020)
carro2 = Carro("Fiat", "Toro", 2023)
carro3 = Carro("Chevrolet", "Onix", 2022)

print(f"Marca:{carro1.marca}\nModelo: {carro1.modelo}\nAno:{carro1.ano}")
print(f"Marca:{carro2.marca}\nModelo: {carro2.modelo}\nAno:{carro2.ano}")
print(f"Marca:{carro3.marca}\nModelo: {carro3.modelo}\nAno:{carro3.ano}")

#44444444444444444444444444444444444444444444444444444444444444444444

class Carro:...
class Carro:
   def __init__(self, marca, modelo, ano):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano

carro1 = Carro("Toyota", "SW4", 2020)
print(f"Marca:{carro1.marca}\nModelo: {carro1.modelo}\nAno:{carro1.ano}")

carro1.ano = 2023
print(f"Marca:{carro1.marca}\nModelo: {carro1.modelo}\nAno:{carro1.ano}")

#5555555555555555555555555555555555555555555555555555555555555555
class ContaBancaria:
   def __init__(self, titular, saldo):
      self.titular = titular
      self.saldo = saldo
  
