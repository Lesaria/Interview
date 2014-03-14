#Ex 3-6 Copyright Yifei
#This program is aiming to convert 4 bits bi to decimal.
#Get bi
b=raw_input("Give a 4-bit binary string: ")
if len(b)==4:
    n= int(b[3])*1 + int(b[2])*2 + int(b[1])*4 + int(b[0])*8
    print b," is ",n," as decimal number."
else:
    print "ERROR!!!"
