s = 100
h = 100

for _ in range(2, 11):
    h *= 0.5
    s += h

h *= 0.5

print(f"小球在第10次落地时，共经过{s}米\n第10次反弹{h}米")