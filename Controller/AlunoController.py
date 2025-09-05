from Models import Aluno as A
from Helpers import TextManipulation as T

class AlunoController:
    def __init__(self, protocolo):
        self.protocolo = protocolo
        self.tabela = ""
        self.rotulos = ""
        self.valores = ""
        self.definidor = ""
        self.condicao = ""
        print("AlunoController")

    def Separar(self):
        try:
            self.tabela = T.LerLinha(self.protocolo, 0)
            self.rotulos = T.LerLinha(self.protocolo, 1)
            self.valores = T.LerLinha(self.protocolo, 2)
            self.definidor = T.LerLinha(self.protocolo, 3)
            self.condicao = T.LerLinha(self.protocolo, 4)
            self.Aluno = A.Aluno(self.tabela, self.rotulos, self.valores, self.definidor, self.condicao)

        except Exception as e:
            print(e)

    def Salvar(self):
        self.Aluno.Salvar()

    def Consultar(self):
        return self.Aluno.Pesquisar()

    def Deletar(self):
        self.Aluno.Deletar()