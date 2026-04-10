password = input("Enter Password")

def strong(str):
    n = len(str)
    upper =False
    num=False
    for s in str:
        if s.isupper():
            upper = True
        elif s.isnumeric():
            num =True
        else:
            continue
    if upper and num and n>=8:
        return True
    else:
        False

def strong1(pwd):
    return(
        len(pwd)>=8 and
        any(c.upper() for c in pwd) and
        any(c.islower() for c in pwd) and
        any(c.islower() for c in pwd)
    )

strength = strong1(password)
print("STRONG" if strong(password) else "WEAK")
