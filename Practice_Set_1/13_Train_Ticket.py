distance = int(input("Enter Distance"))
age = int(input("Enter age "))
total = distance*2 - distance *2 * (0.3 if age >60 else 0.5 if age <12 else 0)
print(int(total))