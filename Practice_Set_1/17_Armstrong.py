num=input()
res = lambda num : sum(int(d)**3 for d in num)
print("YES" if res(num)==int(num)  else "NO")


# digits=list(map(int,num))
# n=sum(d**3 for d in digits)
# if n==int(num):
#     print("Yes")
# else:
#     print("No")
