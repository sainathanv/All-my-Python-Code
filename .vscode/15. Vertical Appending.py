# We will be appedng stars '*' vertically.

t = 11
for i in range(1,t): # 1 2 3 4 5
    for j in range(i):
        N = t - i
        for k in range(t):
            print(' ', end='')
        print('*')
    print()