n = input()
palindrome = lambda n : n==n[::-1]
print("PALINDROME" if palindrome(n) else "NOT PALINDROME")
