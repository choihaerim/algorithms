mod = []

for i in range(10):
    A = int(input())
    mod.append(A%42)

m = set(mod)
print(len(m))