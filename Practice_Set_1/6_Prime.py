# def it_Prime(n):
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# for i in range(a,b+1):
#     if it_Prime(i):
#         count +=1

# count =len([
#     n for n in range(a, b+1)
#     if n>1 and all(n%i !=0 for i in range(2, int(n**0.5)+1))
# ])


a=int(input("Start "))
b=int(input("End "))

its_Prime = lambda n: n>1 and all(n%i !=0 for i in range(2,int(n**0.5)+1))
count = lambda a, b: sum(1 for n in range(a,b+1)if its_Prime(n))

print(count(a,b))