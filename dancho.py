s = input().split()
a = int(s[0])
b = int(s[1])
c = int(s[2])
if a+b > c and a+c > b and b+c > a:
    print("YES")
else:
    print("NO")