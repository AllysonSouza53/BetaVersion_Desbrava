import AlunoController as A
import CidadeController as C
import EscolaController as E
import EstadoController as ES
import PolstController as Po
import ProfissaoController as Pro
import ProssionalController as P
from Helpers import TextManipulation as T

class Controller:
    def __init__(self, protocolo):
        self.protocolo = protocolo
        self.tabela = ""
        self.rotulos = ""
        self.valores = ""
        self.definidor = ""
        self.condicao = ""
        self.controller = ""

    def Separar(self):
        try:
            self.tabela = T.LerLinha(self.protocolo, 0)
            self.rotulos = T.LerLinha(self.protocolo, 1)
            self.valores = T.LerLinha(self.protocolo, 2)
            self.definidor = T.LerLinha(self.protocolo, 3)
            self.condicao = T.LerLinha(self.protocolo, 4)

        except Exception as e:
            print(e)

    def Ordenar(self):
        if self.tabela == "alunos":
            self.controller = A.AlunoController(self.protocolo)
        elif self.tabela == "cidades":
            self.controller = C.CidadesController(self.protocolo)
        elif self.tabela == "escolas":
            self.controller = E.EscolaController(self.protocolo)
        elif self.tabela == "estados":
            self.controller = ES.EstadoController(self.protocolo)
        elif self.tabela == "polst":
            self.controller = Po.PolstController(self.protocolo)
        elif self.tabela == "profissoes":
            self.controller = Pro.ProfissaoController(self.protocolo)
        elif self.tabela == "profissionais":
            self.controller = P.ProfissionaisController(self.protocolo)
        else:
            print("Não encontado!")
