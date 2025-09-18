# # criando uma classe
# class Cachorro: ...

# # adicionando atributos
# class Cachorro:
#     especie = "Canis lupus familiaris"
#     nome = "Toto"
#     raca = "caramelo"
#     idade = 2

#     auau = Cachorro()
#     print(auau)

#     print(auau.especie, auau.nome, auau.raca, auau.idade, sep="\n")

# class Cachorro:
#     dono = "Fred" #atributo que é compartilhdo por todos os objetos
#     self.nome = nome # self - exclusivo para esse objeto
#     self.raca = raca
#     self.idade = idade

    # POO - HERANÇA

    # Quando uma classe herda as informções de outra classe.
    
class Mamifero:
        def __init__(self, especie, habitat):
            self.especie = especie
            self.habitat = habitat
        
        def __str__(self):
            return f"O mamíferi da espécie {self.especie}, pode ser localizado no {self.habitat}"
        
        def movimentar(self):
            print("Caminhando")

class Cachorro(Mamifero):
    def __init__(self, especie, habitat, raca):
         super().__init__(especie, habitat)
         self.raca = raca

    def __str__(self):
         return f"O mamífero da espécie {self.especie}, da raça {self.raca}, pode ser localizado no {self.habitat}"
   #     return f"super().__str__() da raca {self.raca}"

    def correr_moto(self):
         print("O cachorro está correndo atrás da moto")

dog1 = Cachorro("Canis familiaris", "Rua Beta", "caramelo")
print(dog1)