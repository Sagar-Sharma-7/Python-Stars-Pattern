# Hollow Triangle Star Pattern
n = 6
for i in  range(1, n + 1):
    for j in range(i):
        if j == 0 or j == i - 1:
            print("*", end= "")
        else:
            if i != n:
                print(' ', end="")
            else:
                print("*", end="")
    print()