import random

print 'This contents makeface function'
a = 5

def makeFace():
    face = ['(x_x)','(O_O) ','(-_-#)','(>_<)','(^o^)','=^Y^= ','(`_^)']
    numFace = len(face)
    index = random.randint(0, numFace - 1)
    return face[index]

print makeFace()
