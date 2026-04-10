intial_amount=int(input())
n=int(input())
for i in range(n):
    with_amount=int(input("Enter Withdrawal Amount"))
    if(with_amount%10==0 and (intial_amount-with_amount)>=0):
        print("SUCCESS")
        intial_amount-= with_amount
    else:
        print("FAILED")
print(intial_amount)

