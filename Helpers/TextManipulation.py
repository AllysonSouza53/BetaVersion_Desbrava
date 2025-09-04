def LerCaracter(texto, posicao):
  return texto[posicao]

def SubTexto(texto, inicio, fim):
  return texto[inicio:fim]

def LerLinha(texto, numLinha):
  lista = texto.split('.')
  return lista[numLinha]