#111111111111111111111111111111111111111111111111
from abc import ABC, abstractmethod  

class Pagamento(ABC):
    @abstractmethod
    def processar (self, valor):
        pass

class CartaoCredito(Pagamento):
    def processar (self, valor):
        print(f"Processando o pagamento no valor de R${valor:.2f} no cartão de crédito.")

class Boleto(Pagamento):
    
    def processar(self, valor):
        print(f"Gerando boleto no valor de R${valor:.2f}.")

if __name__ == "__main__":
    pagamento1 = CartaoCredito()
    pagamento2 = Boleto()

    pagamento1.processar(78.00)  
    pagamento2.processar(125.00)

#2222222222222222222222222222222222222222222222222

class Ligavel(ABC):
    @abstractmethod
    def ligar (self, ligar):
        pass

class Desligavel(ABC):
    @abstractmethod
    def desligar(self, desligar):
        pass

class Computador(Ligavel, Desligavel):
    def ligar(self):
        print("O computador está ligando")

    def desligar(self):
        print("O computador está desligando")

if __name__ == "__main__":
    computador = Computador()
    computador.ligar()
    computador.desligar()

#333333333333333333333333333333333333333333333333

class Imprimivel(ABC):
    @abstractmethod
    def imprimir (self):
        pass

class Exportavel (ABC):
    @abstractmethod
    def exportar(self):
        pass

class Relatorio(Imprimivel, Exportavel):
    def imprimir(self):
        print("O relatório está sendo impresso")

    def exportar(self):
        print("O relatório está sendo exportado")

if __name__ == "__main__":
    relatorio = Relatorio()
    relatorio.imprimir()
    relatorio.exportar()

#44444444444444444444444444444444444444444444444

class Repositorio (ABC):
    @abstractmethod
    def salvar(self, objeto):
        pass

    @abstractmethod
    def buscar (self, id):
        pass

#lass RepositorioMemoria(Repositorio):
    #def salvar (self, objeto):
       #print(f"Objeto {objeto} salvo na memória.")
      
#positorio = RepositorioMemoria()

# a classe filha precisa herdar todos os métodos da interface "Repositorio"
#código corrigido

class RepositorioMemoria(Repositorio):
    def __init__(self):
        self.dados = {}

    def salvar(self, objeto):
        self.dados[objeto["id"]] = objeto
        print(f"Objeto {objeto} salvo na memória.")

    def buscar(self, id):
        return self.dados.get(id, "Objeto não encontrado.")
    
repositorio = RepositorioMemoria()
repositorio.salvar({"id": 34, "nome": "CRUD"})
print(repositorio.buscar(34))