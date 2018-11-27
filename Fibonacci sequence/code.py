
def fibs(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibs(n-1) + fibs(n-2)


num = int(input("请输入数字："))
print(fibs(num))
