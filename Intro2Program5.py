#Ex5-6 Copyright Yifei
#Cryptographic algorithm ROT-13
plain=raw_input("Type in your string: ")

def rot13(s):
    encry=""
    for i in s:
        if ord(i)<ord("n"):
            char=chr(ord(i)+13)
        else:
            char=chr(ord(i)-13)
        encry += char
    return encry

print rot13(plain)
