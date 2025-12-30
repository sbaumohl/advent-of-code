import fileinput
import re

pat = r"XMAS"
pat_re = r"SAMX"

cnt = 0
mat = []
for line in fileinput.input():
    l = list([x for x in line.strip()])
    mat.append(l)

def check(i, j, mat):
    if mat[i][j] != 'A':
        return False

    # top-left, bottom-right
    if mat[i - 1][j - 1] == 'M' and mat[i + 1][j + 1] == 'S':
        pass
    elif mat[i - 1][j - 1] == 'S' and mat[i + 1][j + 1] == 'M':
        pass
    else:
        return False
    
    if mat[i + 1][j - 1] == 'M' and mat[i - 1][j + 1] == 'S':
        pass
    elif mat[i + 1][j - 1] == 'S' and mat[i - 1][j + 1] == 'M':
        pass
    else:
        return False

    return True

for i in range(1, len(mat) - 1):
    for j in range(1, len(mat[0]) - 1):
        cnt += 1 if check(i, j, mat) else 0
    
print(cnt)
