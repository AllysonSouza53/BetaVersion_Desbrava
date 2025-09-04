import os

def LerArquivo(CaminhoArquivo):
  arquivo = open(CaminhoArquivo, "r")
  texto = arquivo.read()
  arquivo.close()
  return texto

def EscreverArquivo(CaminhoArquivo, texto):
  arquivo = open(CaminhoArquivo, "w")
  arquivo.write(texto)
  arquivo.close()