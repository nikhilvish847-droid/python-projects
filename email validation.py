sign=["_",".","@"]
k=0
email=input("Enter your email address: ")
if len(email)>=6:
    if email[0].isalpha():
        if email.count("@")==1: 
            if email[-3]=="." or email[-4]==".":
                for i in email:
                    if i.isspace():
                        print("invalid 2 email")
                        break
                    elif i in sign or i.isdigit():
                        continue
                    elif i.isalpha():
                        if i==i.upper():
                            print("invalid email:email has some uppercase letter.")
                            break
                        else:
                            continue
                    else:
                        print("invalid email: this email has some irrelevent operator.")
                        break 
                else:
                    print("right email")                 
            else:
                print("invalid email:email should end with .com or .in .")
        else:
            print("invalid email:email has some irrelevent operator.")
    else:
        print("invalid email:first letter is not a alphabet.")
else:
    print("invalid email:minimum character should be 6.")