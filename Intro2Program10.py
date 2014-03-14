#Ex10-5 Copyright Yifei Ren
#Function generateGroup(sizeOfGroup) reads all names and generates a random list of strings with sizeOfGroup.
from random import choice
def generateGroup(sizeOfGroup):
    f=open("persons.dat","r")
    line=f.readline()
    name=[]
    while line!="":
        new=line[:line.find(",")]
        if new not in name:
            name.append(new)
        else:
            pass
        line=f.readline()
    f.close()
    
    chosenName=[]
    for i in range(0,sizeOfGroup):
        chosenName.append(choice(name))
    return chosenName

#random.sample()
