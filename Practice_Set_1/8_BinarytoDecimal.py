binary = input("Enter binary Number ")
# for digit in reversed(binary):
#     decimal += int(digit)*(2**i)
#     i +=1
# print(decimal)


# decimal =sum(int(digit)*(2**i) for i, digit in enumerate(binary[::-1]))
decimal = lambda binary : sum(int(digit)*(2**i)for i,digit in enumerate(binary[::-1]))
print(decimal(binary))
