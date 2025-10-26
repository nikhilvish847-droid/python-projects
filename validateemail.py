
email=input("Enter your email address: ")
if len(email)>=6:
    if email[0].isalpha():
        if email.count("@")==1:
            if email.isspace():
                print("invalid email")
            else:
                if email[-3]=="." ^ email[-4]==".":
                    pass
                else:
                    print("invalid email")
        else:
            print("invalid email")
    else:
        print("invalid email")

else:
    print("invalid email")