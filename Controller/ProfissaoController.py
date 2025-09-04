from Models import Profissao as Pro
from Helpers import TextManipulation as T

class ProfissaoController:
    def __init__(self, protocolo):
        self.protocolo = protocolo
        self.tabela = ""
        self.rotulos = ""
        self.valores = ""
        self.definidor = ""
        self.condicao = ""
        self.Profissao = Pro.Profissao(self.tabela, self.rotulos,self.valores,self.definidor,self.condicao)

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
        self.Profissao.Salvar()

    def Consultar(self):
        return self.Profissao.Pesquisar()

    def DeletarAluno(self):
        self.Profissao.Deletar()