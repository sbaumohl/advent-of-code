import fileinput
import re

pat = r"XMAS"
pat_re = r"SAMX"

cnt = 0
mat = []
for line in fileinput.input():
    l = list([x for x in line.strip()])
    mat.append(l)

mat_trans = [['0'] * len(mat) for _ in range(len(mat[0]))]


Xs = []
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 'X':
            Xs.append((i, j))
        mat_trans[j][i] = mat[i][j]


# hor
for row in mat:
    cnt += len(re.findall(pat, ''.join(row)))
    cnt += len(re.findall(pat_re, ''.join(row)))

for row in mat_trans:
    cnt += len(re.findall(pat, ''.join(row)))
    cnt += len(re.findall(pat_re, ''.join(row)))

r, c = len(mat), len(mat[0])
for i,j in Xs:
    # top right
    if i > 2 and j < c - 3:
        cnt += 1 if mat[i - 1][j + 1] == 'M' and mat[i - 2][j + 2] == 'A' and mat[i - 3][j + 3] == 'S' else 0 

    # bottom right
    if i < r - 3 and j < c - 3:
        cnt += 1 if mat[i + 1][j + 1] == 'M' and mat[i + 2][j + 2] == 'A' and mat[i + 3][j + 3] == 'S' else 0 

    # top left
    if i > 2 and j > 2:
        cnt += 1 if mat[i - 1][j - 1] == 'M' and mat[i - 2][j - 2] == 'A' and mat[i - 3][j - 3] == 'S' else 0 


    # bottom left
    if i < r - 3 and j > 2:
        cnt += 1 if mat[i + 1][j - 1] == 'M' and mat[i + 2][j - 2] == 'A' and mat[i + 3][j - 3] == 'S' else 0 



print(cnt)
