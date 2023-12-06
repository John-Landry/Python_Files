

x = [i for i in range(10)]

print(x)

x = [[] for i in range(10)]

print(x)

x = [[j for j in range(4) if i % 2 == 0] for i in range(7)]

print(x)

x = [i for i in range(10) if i % 2 == 0]

print(x)

x = [[j for j in range(4)] for i in range(7)]

print(x)

x = [[j for j in range(4) if i % 2 == 0] for i in range(7)]

print(x)
