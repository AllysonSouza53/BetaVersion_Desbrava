import os as s
import time as t
import subprocess as sp


def monitorador(stop_event):
    Pasta = s.path.dirname(s.path.abspath(__file__))
    Pasta_vazia = set(f for f in s.listdir(Pasta) if f.endswith(".txt"))

    while not stop_event.is_set():
        t.sleep(2)
        Pasta_Atual = set(f for f in s.listdir(Pasta) if f.endswith(".txt"))
        novos = Pasta_Atual - Pasta_vazia
        for txt in novos:
            sp.run(["python", ".py"])
            s.remove(s.path.join(Pasta, txt))
        Pasta_vazia = Pasta_Atual