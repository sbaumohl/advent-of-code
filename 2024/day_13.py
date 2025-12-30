import re
import numpy as np
from numpy.core.multiarray import dtype
import scipy as sp
from mpmath import mp, matrix, lu_solve 
mp.dps = 25
mp.pretty = True

fi = []
with open("./in.txt", 'r') as f:
    for line in f.readlines():
        fi.append(line.strip())

cnt = 0
i = 0
f = 1
while i < len(fi):

    a_move = re.match("Button A: X\\+(\\d+), Y\\+(\\d+)", fi[i]).groups()
    a_move = [int(a_move[0]) / f, int(a_move[1]) / f]

    b_move = re.match("Button B: X\\+(\\d+), Y\\+(\\d+)", fi[i + 1]).groups()
    b_move = [int(b_move[0]) / f, int(b_move[1]) / f]

    goal = re.match("Prize: X=(\\d+), Y=(\\d+)", fi[i + 2]).groups()
    goal = [int(goal[0]) + 10000000000000, int(goal[1]) + 10000000000000]
    goal = [goal[0] / f, goal[1] / f]
   
    ins = matrix([[a_move[0], b_move[0]], [a_move[1], b_move[1]]])
    out = matrix(goal)

    # sols = sp.linalg.solve(ins, out)
    sols = lu_solve(ins, out)
    
    # print(sols[0], sols[1]) 
    if str(sols[0]).endswith('.0') and str(sols[1]).endswith('.0'):
        cnt += 3 * sols[0] + sols[1]

    i += 4
    # print(a_move, b_move, goal, sols, cnt)

print(cnt)

