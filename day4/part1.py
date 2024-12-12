input = open("input").read().splitlines()

HOR = [0, 1]
VER = [1, 0]
DIAG = [1, 1]
REVHOR = [-1, 0]
REVVER = [0, -1]
REVDIAG = [-1, -1]
OTHERREVDIAG = [1, -1]
OTHEROTHERREVDIAG = [-1, 1]


def find_xmas(x, y):
    count = 0
    directions = [
        HOR,
        VER,
        DIAG,
        REVHOR,
        REVVER,
        REVDIAG,
        OTHERREVDIAG,
        OTHEROTHERREVDIAG,
    ]
    for direction in directions:
        xdir = direction[0]
        ydir = direction[1]
        current_x = x
        current_y = y
        for char in "XMAS":
            current_char = input[current_y][current_x]
            if current_char == char:
                if char == "S":
                    count += 1
                    print(f"XMAS found from {y},{x} to {current_y},{current_x}")
                if (current_x + xdir) <= len(
                    input[current_y]
                ) - 1 and current_x + xdir >= 0:
                    current_x += xdir
                else:
                    break
                if (current_y + ydir) <= len(input) - 1 and (current_y + ydir) >= 0:
                    current_y += ydir
                else:
                    break
            else:
                break
    return count


total = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "X":
            total += find_xmas(x, y)
print(total)
