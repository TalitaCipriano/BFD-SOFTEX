#1111111111111111111111111111111111111111111111111111111111111111
from abc import ABC, abstractmethod  
class Animal(ABC):
    @abstractmethod
    def falar(self):
        pass
        
class Cachorro(Animal):
    def falar(self):
        return "late"
    
class Gato(Animal):
    def falar(self):
        return "mia"
    
if __name__ == "__main__":
    cachorro = Cachorro()
    gato = Gato()

    #print("O cachorro", cachorro.falar())
    #print("O gato", gato.falar())

#2222222222222222222222222222222222222222222222222222

#animal = Animal()  # isso irá causar um erro pq "animal" não foi definido, pois ainda não foi definido o método falar()

#print(animal.falar())

#3333333333333333333333333333333333333333333333333333

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
if __name__ == "__main__":
    retangulo = Retangulo(8,6)
    #print("Área do retângulo:", retangulo.area())
    #print("Perímetro do retângulo:", retangulo.perimetro())

#44444444444444444444444444444444444444444444444444444444

class Transporte(ABC):
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def parar(self):
        pass

class Carro(Transporte):
    def mover(self):
        return "O carro está se movendo"

#carro = Carro()          
#print(carro.mover())

#código correto

class Carro(Transporte):
    def mover(self):
        return "O carro está em movimento"

    def parar(self):
        return "O carro está parado"
    
#carro = Carro()
#print(carro.mover())  
#print(carro.parar()) 