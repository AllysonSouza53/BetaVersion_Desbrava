from Helpers import ArchiveManipulation as AM
from Controller.Controller import Controller

def PegarProtocolo(caminho):
    Protocolo = AM.LerArquivo(caminho)
    return Protocolo

print("Protocolo")
Controle = Controller(PegarProtocolo("TIDB//SET//memoria.txt"))
Controle.Separar()
Controle.Ordenar()
print("Ordenou")