import random as r
import string as s

#making a random 3 letter word
p="".join(r.choices(s.ascii_letters,k=3))
q="".join(r.choices(s.ascii_letters,k=3))

#creating a greeting function#
def greet(fx):
    def mfx():
        print("hello WELCOME TO OUR CODE\n here you will be able to make your message encrypted.")
        fx()
        print("bye bye , see you next time")
    return mfx
    
@greet
#creating function to create a code language and to decode#
def code_language():
    a=input("want to code or decode? :")
    if a=="code":
        c=[]
        b=input("enter sentence to make into code language:")
        b=b.split(" ")
        for i in b:
            if len(i)>2:
                s=p+i[1:]+i[0]+q
                c.append(s)
            else:
                z=i[::-1]
                c.append(z)

        c=" ".join(c)
        print(c)         
    elif a=="decode":
        c=[]
        b=input("enter sentence to make into code language:")
        b=b.split(" ")
        for i in b:
            if len(i)>2:
                s=i[-4]+i[3:-4]
                c.append(s)
            else:
                z=i[::-1]
                c.append(z)
        c=" ".join(c)
        print(c)
    else:
        raise ValueError("what a shit you have written")

#calling a function
code_language()
