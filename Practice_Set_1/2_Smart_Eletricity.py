# units=int(input("Enter units"))
# total =0
# if units <= 100 :
#     total=units*3
# elif units <= 200:
#     total = (100*3)+(units-100)*5
# else:
#     total = (100*3) + 100*5 + (units-200) *8

# if units >300:
#     total += total*0.1

# print (int(total))


# Pythonic
unit = int(input("Enter units: "))
total = (
    min(unit,100)*3 +
    max(min(unit-100,100),0)*5 +
    max(unit-200,0)*8
)
total *= 1.1 if unit >300 else 1
print(int(total))