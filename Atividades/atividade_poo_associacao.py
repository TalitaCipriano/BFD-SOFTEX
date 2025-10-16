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

class Funcionario:
    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo

    def __str__(self):
        return f"[{self.id}] {self.nome} - {self.cargo}"


class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.funcionarios.append(funcionario)
        else:
            raise TypeError("Apenas instâncias de Funcionario podem ser adicionadas.")

    def listar_funcionarios(self):
        print(f"Funcionários do departamento {self.nome}:")
        for funcionario in self.funcionarios:
            print(f" - {funcionario}")


f1 = Funcionario(1, "Thiago", "Engenheiro")
f2 = Funcionario(2, "Laís", "Analista")

dep_ti = Departamento("TI")

dep_ti.adicionar_funcionario(f1)
dep_ti.adicionar_funcionario(f2)

dep_ti.listar_funcionarios()

#44444444444444444444444444444444444444444444444444444444444444