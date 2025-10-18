import random
a=["rock","paper","scissor"]
print("WELCOME TO PLAY ROCK PAPER AND SCISSOR ".center(430))
b="yes"
while(b=="yes"):
    comp=random.randint(0,2)
    print("for rock input 0 \nfor paper input  1\nfor scissor input 2 ")
    user=int(input("enter your option:"))
    print(f"your input is {user} .ie-{a[user]}\ncomputer input is {comp} i.e-{a[comp]}")
    if int(comp)==user:
        print("match is tie.")
    elif comp==0 and user==1:
        print("congrats you win.")
    elif comp==1 and user==2:
        print("congrats you win.")
    elif comp==2 and user==0:
        print("congrats you win.")
    else:
        print("unfortunately you loose .")
    print("want to continue \nif yes then input yes\nif no then input any integer.")
    b=input("enter :")
print("thank you.")