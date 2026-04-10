num = input("Enter Number")
increase = all(num[i]<num[i+1] for i in range(len(num)-1))
print("Yes" if increase else "No")