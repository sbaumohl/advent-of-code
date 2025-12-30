from itertools import product
from collections import deque

fi = []

with open("./example.txt", 'r') as f:
    for line in f.readlines():
        fi.append([x for x in line.strip()])

n,c = len(fi), len(fi[0])

cnt = 0
seen = set()
for i,j in product(range(n), range(c)):
    if (i, j) in seen:
        continue

    q = deque([(i, j)])
    area, prm = 0, 0
    x = fi[i][j]
    reg = set()
    
    while len(q) > 0:
        cx, cy = q.popleft()
        if (cx, cy) in seen or (cx, cy) in reg:
            continue
        seen.add((cx, cy))
        reg.add((cx, cy))
        area += 1

        for dx, dy in [
            (1, 0), (0, 1), (-1, 0), (0, -1)
        ]:
            nx, ny = cx + dx, cy + dy

            if ny < 0 or ny >= c or nx < 0 or nx >= n or fi[nx][ny] != x:
                prm += 1
                continue
            elif (nx, ny) in seen or (nx, ny) in reg:
                continue
            
            q.append((nx, ny))
    print(reg)
    cnt += area * prm
print(cnt)
