from Models import Cidade as C
from Helpers import TextManipulation as T

class CidadesController:
    def __init__(self, protocolo):
        self.protocolo = protocolo
        self.tabela = ""
        self.rotulos = ""
        self.valores = ""
        self.definidor = ""
        self.condicao = ""
        self.Cidade = C.Cidade(self.tabela, self.rotulos,self.valores,self.definidor,self.condicao)

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
        self.Cidade.Salvar()

    def Consultar(self):
        return self.Cidade.Pesquisar()

    def Deletar(self):
        self.Cidade.Deletar()