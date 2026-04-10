n = int(input())
cap=40
total = 0
for _ in range(n):
    x = int(input())
    total += x
    if total < cap:
        print("CONFIRMED")
    else:
        print("WAITLISTED")
