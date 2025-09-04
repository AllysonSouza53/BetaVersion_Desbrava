from Helpers import TextManipulation as T
from Helpers import ArchiveManipulation as A

def separador(dados):
  texto = ""
  dados = dados.replace("(", "")
  dados = dados.replace("'", "")
  dados = dados.replace(",", ".")
  dados = dados.replace(")", "")
  dados = dados.replace("[", "")
  dados = dados.replace("]", "")
  dados = dados + '.'
  linhas = SepararLinhas(dados)
  for i, linha in enumerate(linhas, 1):
    texto += linha + '\n'
    A.EscreverArquivo("BancoInterno/Buscar/memoria.txt", texto)

def SepararLinhas(texto):
    # Divide o texto por ponto final
    linhas = texto.split('.')
    # Remove espaços desnecessários e linhas vazias
    linhas = [linha.strip() for linha in linhas if linha.strip()]
    return linhas