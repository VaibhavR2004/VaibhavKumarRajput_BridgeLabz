# vowel = {'a','e','i','o','u'}
# count = sum(1 for s in string if s in vowel)


string = input("Enter string ").lower()
count = lambda string : sum(1 for s in string if s in "aeiou")
print(count(string))