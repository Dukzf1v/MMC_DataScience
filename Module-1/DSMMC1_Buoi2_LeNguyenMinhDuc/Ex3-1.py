for i in range (1,9):
    for j in range (1,i):
        print("*", end=" ")
    print()
print("\n")
for i in range(8, 0, -1):
    for j in range (0, j):
        print("*", end=" ")
    print()
print("\n")
for i in range(8, 0, -1):
    for j in range (0, 8 - i):
        print(" ", end=" ")
    for k in range (0,i):
        print("*", end=" ")
    print()
print("\n")
for i in range(8, 0, -1):
    for k in range (0,i):
        print(" ", end=" ")
    for j in range (0, 8 - i):
        print("*", end=" ")
    print()
    