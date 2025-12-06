import sys

path = sys.argv[1]


def is_invalid(x: str) -> bool:
    if len(x) % 2 == 1:
        return False
    m = len(x) // 2
    return x[:m] == x[m:]


def is_invalid_part2(x: str) -> bool:
    for l in range(1, len(x)):
        if len(x) % l != 0:
            continue

        part = x[:l]
        rep = len(x) // l

        if rep * part == x:
            return True

    return False


with open(path, "r+") as f:
    s = 0

    ranges = f.readlines()[0].split(",")
    for r in ranges:
        spl = r.split("-")
        start, end = int(spl[0]), int(spl[1])

        for c in range(start, end + 1):
            if is_invalid_part2(str(c)):
                s += c

    print(s)
