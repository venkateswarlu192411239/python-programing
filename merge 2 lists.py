a=[3,5,7,536,25,547,75,64]
b=[253,5475,75,64,3545,43645,346,366,463]
a.sort()
print(a)
b.sort()
print(b)
d=sorted(a+b)
print("meged of 2 lists is:",d)
h=set(d)
print(h)