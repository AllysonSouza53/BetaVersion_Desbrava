from Helpers import ArchiveManipulation as AM
from Controller import Controller as C

def PegarProtocolo(caminho):
    Protocolo = AM.LerArquivo(caminho)
    return Protocolo

C.Controller(PegarProtocolo(""))