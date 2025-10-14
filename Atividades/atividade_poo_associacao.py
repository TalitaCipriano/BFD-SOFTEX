#111111111111111111111111111111111111111111111111111111111

class Livro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    
    def anotar_atividade(self, livro: Livro):
        print(f"{self.nome}, esta lendo o livro {livro.titulo} de {livro.autor}")

pessoa1 = Pessoa("Talita")
livro1 = Livro("Anjos e Demônios", "Dan Brown")

pessoa1.anotar_atividade(livro1)

#2222222222222222222222222222222222222222222222222222222222222222

class Onibus:
    def __init__(self, linha, nome_linha):
        self.linha = linha  
        self.nome_linha = nome_linha  

    def __str__(self):
        return f"{self.linha}/{self.nome_linha}"
    
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        
    def pegar_onibus(self, onibus):
        print(f"{self.nome} utiliza o ônibus da linha {onibus} para ir ao curso.")

onibus1 = Onibus(linha=243, nome_linha="Dois Carneiros")
aluno1 = Aluno(nome="Talita")

aluno1.pegar_onibus(onibus1)

#3333333333333333333333333333333333333333333333333333333333333
