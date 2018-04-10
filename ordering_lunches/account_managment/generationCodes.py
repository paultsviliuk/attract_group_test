import random

def makeTokken():
    tokken=[]
    for i in range(1,10):
        tokken.append(random.randint(1,200))
    tokken=bytearray(tokken)
    tokken=str(tokken)[9:].replace('\\','>')
    tokken=tokken.replace('"','<')
    return tokken
