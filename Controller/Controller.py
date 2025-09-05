from Controller.AlunoController import AlunoController
from Controller.CidadeController import CidadesController
from Controller.EscolaController import EscolaController
from Controller.EstadoController import EstadoController
from Controller.PolstController import PolstController
from Controller.ProfissaoController import ProfissaoController
from Controller.ProfissionalController import ProfissionaisController
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
        print("Controller")

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
            self.controller = AlunoController(self.protocolo)
            print("Criou Aluno")
        elif self.tabela == "cidades":
            self.controller = CidadesController(self.protocolo)
        elif self.tabela == "escolas":
            self.controller = EscolaController(self.protocolo)
        elif self.tabela == "estados":
            self.controller = EstadoController(self.protocolo)
        elif self.tabela == "polst":
            self.controller = PolstController(self.protocolo)
        elif self.tabela == "profissoes":
            self.controller = ProfissaoController(self.protocolo)
        elif self.tabela == "profissionais":
            self.controller = ProfissionaisController(self.protocolo)
        else:
            print("Não encontado!")

        if self.definidor == 'I' or self.definidor == 'A':
            self.controller.Salvar()
        elif self.definidor == 'C':
            self.controller.Consultar()
        elif self.definidor == 'E':
            self.controller.Deletar()
