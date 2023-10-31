n = 0

for i in range(2000, 2501, 4):
    if i % 100 != 0 or i % 400 == 0:
        print(i, end=" ")
        n = n + 1
        if n == 16:
            print("")
            n = 0
