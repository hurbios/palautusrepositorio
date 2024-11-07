# tehdään alussa importit, ja muutosta mainissa

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan") # muutos

x = int(input("luku 1: ")) # muutosss ja bugikorjaus
y = int(input("luku 2: ")) # mmuutso ja bugokorjeus
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
print("goodbye!") # lisäys bugikorjaus-branchissa
