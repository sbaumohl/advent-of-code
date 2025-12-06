with open("day1.txt", "r+") as f:
    c = 0
    sum = 50
    for line in f.readlines():
        line.strip()

        dir = line[0]
        num = int(line[1:])
        # start = sum
        #
        # if dir == "L":
        #     sum -= num
        # else:
        #     sum += num
        #
        # if sum <= 0 and num > abs(sum):
        #     c += (abs(sum) // 100) + 1
        # elif sum >= 100:
        #     c += sum // 100
        #
        # print(dir, num, sum, c)
        #
        # sum %= 100
        d = 1 if dir == "R" else -1
        for _ in range(num):
            sum = (sum + d) % 100
            if sum == 0:
                c += 1

    print(c)
