a = []
while True:
    n = int(input("you want to add new number press 1 or press 0  to exit "))
    if 1 == n:
        new = int(input("insert a new value  ="))
        a.append(new)
    else:
        break
print("\narray =",a)
