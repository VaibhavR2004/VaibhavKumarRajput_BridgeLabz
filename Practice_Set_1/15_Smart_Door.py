correct_pin=int(input("Enter Correct Pin: "))

attemp = lambda x:x==correct_pin

for _ in range(3):
    if(attemp(int(input()))):
        print("ACESS GRANTED")
        break
    else:
        print("LOCKED")
