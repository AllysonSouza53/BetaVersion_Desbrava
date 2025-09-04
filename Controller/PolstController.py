from Models import Polst as Po
from Helpers import TextManipulation as T

class PolstController:
    def __init__(self, protocolo):
        self.protocolo = protocolo
        self.tabela = ""
        self.rotulos = ""
        self.valores = ""
        self.definidor = ""
        self.condicao = ""
        self.Polst = Po.Polst(self.tabela, self.rotulos,self.valores,self.definidor,self.condicao)

    def Separar(self):
        try:
            self.tabela = T.LerLinha(self.protocolo, 0)
            self.rotulos = T.LerLinha(self.protocolo, 1)
            self.valores = T.LerLinha(self.protocolo, 2)
            self.definidor = T.LerLinha(self.protocolo, 3)
            self.condicao = T.LerLinha(self.protocolo, 4)

        except Exception as e:
            print(e)

    def Salvar(self):
        self.Polst.Salvar()

    def Consultar(self):
        return self.Polst.Pesquisar()

    def DeletarAluno(self):
        self.Polst.Deletar()