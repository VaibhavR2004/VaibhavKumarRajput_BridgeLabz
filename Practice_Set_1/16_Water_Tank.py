n =int(input())
flow=list(map(int, input().split()))
total=0
for i,x in enumerate(flow,1):
    total += x
    if total>1000:
        print(i)
        break




# check_tank=lambda x, cap: cap>=x
# for i in range(n):
#     x=int(input())
#     if check_tank(x,cap):
#         cap -= x
#     else:
#         print(i)