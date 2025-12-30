import fileinput
import re

cnt = 0
d = {}

rules = []
updates = []

for line in fileinput.input():
    line = line.strip()
    if '|' not in line and len(line) > 0:
        updates.append(line.split(','))
    elif len(line) > 0:
        rules.append(line.split('|'))

for r in rules:
    s = d.get(r[1], set())
    s.add(r[0])
    d[r[1]] = s

wrong = []
for u in updates:
    seen = set()
    avail = set(u)
    good = True
    for x in u:
        if x in d and not d[x].intersection(avail) <= seen:
            good = False
            wrong.append(u)
            break
        seen.add(x)

    if good:
        cnt += int(u[len(u) // 2])
# print(cnt) 

# part 2
cnt = 0
for w in wrong:
    avail = set(w)
    fixed = []
    seen = set()
    

    for x in w:
        if x not in d or len(d[x].intersection(avail)) == 0:
            fixed.append(x)
            seen.add(x)

    q = set(avail.difference(seen))
    while len(q) > 0:
        for x in q:
            if d[x].intersection(avail) <= seen:
                fixed.append(x)
                seen.add(x)
            
        q = set(avail.difference(seen))

    cnt += int(fixed[len(fixed) // 2])
print(cnt)

