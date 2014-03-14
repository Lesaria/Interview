# -*- coding: cp936 -*-
#Ex9-6 Copyright Yifei
#Queries for a criteria and sorts the "persons.dat” in ascending natural order using that criteria.
print '''Select the criteria to sort the file by:
1. Name
2. Age
3. Weight
4. Height'''
n=input("Sort by what criteria: ")
dic={1:"name", 2:"age", 3:"weight", 4:"height"}
print "Sorted by",dic[n]

#read and write the file
f=open("persons.dat","r")
lFile=[]
#convert file to a list
line=f.readline()
while line !="":
    l=line.split(",")
    lFile.append(tuple(l))
    line=f.readline()
f.close()

#sort the list
newList=sorted(lFile,key=lambda x:x[n-1])#x:x[n]
print newList

#clean the file
f1=open("persons.dat","w")
f1.write("")
f1.close()

#write list back to file
f2=open("persons.dat","a")
for i in newList:
    f2.write(str(i))
f2.close()
