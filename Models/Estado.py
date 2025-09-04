import Banco as B

class Estado:
    def __init__(self,tabela,rotulos,valores,definidor,condicao):
        self.tabela = tabela
        self.rotulos = rotulos
        self.valores = valores
        self.definidor = definidor
        self.condicao = condicao

    def Salvar(self):
        try:
            if self.definidor == "I":
                B.Banco.conectar()
                B.Banco.inserir(self.tabela,self.rotulos,self.valores)
            else:
                B.Banco.conectar()
                B.Banco.editar(self.tabela,self.valores,self.condicao)
        except Exception as e:
            print(e)

    def Pesquisar(self):
        try:
            B.Banco.conectar()
            resultado = B.Banco.consultar(self.rotulos,self.tabela,self.condicao)
            return resultado
        except Exception as e:
            print(e)

    def Deletar(self):
        try:
            B.Banco.conectar()
            B.Banco.excluir(self.tabela, self.condicao)
        except Exception as e:
            print(e)



