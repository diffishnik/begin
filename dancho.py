s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
s = a*b*c
p = 2*(a*b+b*c+a*c)
print(f"{int(p)} {int(s)}")