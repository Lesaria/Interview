#Ex8-6 Copyright Yifei
#Program that queries for numbers A and B, and outputs LCM and store in dictionary where A,B are keys and LCM is value.
def gcd(a,b):
    r=a%b
    if r:
        return gcd(b,r)
    else:
        return b
    
def lcm(c,d):
    return c*d/gcd(c,d)

a=input("Give A: ")
b=input("Give B: ")
lcmList={}
while a*b!=0:
    index=(min(a,b), max(a,b))
    if index in lcmList:
        print "Found in dictionary!"
    else:
        lcmList[index]=lcm(a,b)
        print "Not found in dictionary!"
        print "LCM for A and B is ", lcmList[index]
    a=input("Give A: ")
    b=input("Give B: ")

print "Bye!"
#useful for complex calculation
