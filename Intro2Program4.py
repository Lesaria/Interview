#Ex4-6 Copyright Yifei
#Check whether the number is a prime number or not.

n=input("Enter a number: ")
prime=False

if n<=1:
    prime=False

for i in range(2,n-1):
    if n%i==0:
        prime=False
        break
    else:
        i=i+1
    prime=True

if prime:
    print n," is a prime number"
else:
    print n," is NOT a prime number"
