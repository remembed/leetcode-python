num = input()
[a, b] = num.split(' ')
if int(a) % int(b) == 0:
    print("YES")
else:
    print("NO")
