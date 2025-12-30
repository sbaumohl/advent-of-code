from functools import cache
fi = []

with open("./example.txt", 'r') as f:
    for line in f.readlines():
        fi.extend(map(int, line.split(' ')))
o = fi[::]

@cache
def func(x: int, i = 200):
    if i == 0:
        return 1

    if x == 0:
        return func(1, i - 1)   
    elif len(str(x)) % 2 == 0:
        s = str(x)
        return func(int(s[:len(s) // 2]), i - 1) + func(int(s[len(s) // 2:]), i - 1)
    else:
        return func(2024 * x, i - 1)


cnt = 0
for x in o:
    cnt += func(x)

print(cnt)

