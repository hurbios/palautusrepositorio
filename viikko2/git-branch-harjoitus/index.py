# tehdään alussa importit

from logger import logger
from summa import summa
from erotus import erotus

logger("aloitetaan")

x = int(input("luku 1: ")) # bugikorjaus
y = int(input("luku 2: ")) # bugokorjeus
print(f"{summa(x, y)}")
print(f"{erotus(x, y)}")

logger("lopetetaan")
print("goodbye!") # lisäys bugikorjaus-branchissa
