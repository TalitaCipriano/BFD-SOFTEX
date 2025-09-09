# criando uma classe
class Cachorro: ...

# adicionando atributos
class Cachorro:
    especie = "Canis lupus familiaris"
    nome = "Toto"
    raca = "caramelo"
    idade = 2

    auau = Cachorro()
    print(auau)

    print(auau.especie, auau.nome, auau.raca, auau.idade, sep="\n")

class Cachorro:
    dono = "Fred" #atributo que é compartilhdo por todos os objetos
    self.nome = nome # self - exclusivo para esse objeto
    self.raca = raca
    self.idade = idade