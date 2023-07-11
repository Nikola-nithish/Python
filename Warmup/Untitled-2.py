def x(n):
    for i in range(n):
        if l[i] == 1:
            print(i)
            for x in range(1, n):
                if i+x < len(l):
                    l.remove(1)
                    print(i+x)

l = [1, 1, 2, 3, 4, 1, 5, 1, 6, 1]
a = len(l)
x(a)
