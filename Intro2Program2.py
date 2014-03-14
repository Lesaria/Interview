#Intro2Program 2_6 Copyright Lesaria
#This program is aiming to find index of String B twice occurring in A. This is based on given B occured several times in A.
#Ask user for string A
aString = raw_input("Give the string A: ")
#Ask user for string B
bString = raw_input("Give the string B: ")
#Find 1st time's index
index = aString.find(bString)
#Generate 2nd time's index
nextIndex = aString.find(bString, (index+len(bString)))
#Print
print "The index of the 2nd occurrence of B in A is ", nextIndex
