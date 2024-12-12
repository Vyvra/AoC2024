input = open("input").read().splitlines()

HOR = [0, 1]
VER = [1, 0]
DIAG = [1, 1]
REVHOR = [-1, 0]
REVVER = [0, -1]
REVDIAG = [-1, -1]
OTHERREVDIAG = [1, -1]
OTHEROTHERREVDIAG = [-1, 1]


def find_crosmas(x, y):
    count = 0
    directions = [
        DIAG,
        REVDIAG,
        OTHERREVDIAG,
        OTHEROTHERREVDIAG,
    ]
    # check that A is diagonally connected to M.
    current_x = x
    current_y = y
    crosscount = 0
    for direction in directions:
        tochecky = current_y + direction[0]
        tocheckx = current_x + direction[1]
        tocheckyneg = current_y - direction[0]
        tocheckxneg = current_x - direction[1]
        if tochecky < len(input) and tochecky >= 0:
            if tocheckx < len(input[0]) and tocheckx >= 0:
                if tocheckyneg < len(input) and tocheckyneg >= 0:
                    if tocheckxneg < len(input[0]) and tocheckxneg >= 0:
                        if (
                            input[current_y + direction[0]][current_x + direction[1]]
                            == "M"
                        ):
                            if (
                                input[current_y - direction[0]][
                                    current_x - direction[1]
                                ]
                                == "S"
                            ):
                                crosscount += 1
    if crosscount > 1:
        return 1
    else:
        return 0


total = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char == "A":
            total += find_crosmas(x, y)
print(total)
