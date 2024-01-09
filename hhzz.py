i = int(input())
r = 1
while True:
    if i >= 2**r:
        r =  r + 1
    else:
        break
r = r - 1
print(r)