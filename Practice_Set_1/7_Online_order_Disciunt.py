amount = int(input())
discount = lambda amount : 0.2 if amount >=5000 else 0.1 if amount>=3000 else 0.05 if amount>=1000 else 0

print(int(amount - amount*discount(amount)))