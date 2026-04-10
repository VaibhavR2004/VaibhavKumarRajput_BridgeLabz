marks = list(map(int, input("Enter marks ").split()))
print("FAIL" if any(m <35 for m in marks) else"DISTINCTION" if sum(marks)/len(marks) else "PASS")
