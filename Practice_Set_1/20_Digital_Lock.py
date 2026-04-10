# num = int(input())
# temp=num
# digit_sum=0
# while num>=10:
#     while(temp>0):
#         digit_sum += temp%10
#         temp=temp//10
#     num-=digit_sum


# print(num)

n = int(input())

# while n >= 10:
#     digit_sum = sum(int(d) for d in str(n))
#     n -= digit_sum

# print(n)
reduce_digit = lambda n: n if n < 10 else reduce_digit(n - sum(int(d) for d in str(n)))

print(reduce_digit(int(input())))