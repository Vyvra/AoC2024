input = open("input").read().splitlines()

directions = ["^", ">", "V", "<"]


def get_starting_position(input):
    for i, line in enumerate(input):
        for j, column in enumerate(line):
            if column in directions:
                return [i, j, column]
    return [0, 0, "^"]


def walk_the_guard():
    guardcoord = get_starting_position(input)
    guardpath = []
    guard_has_left = False
    while not guard_has_left:
        if is_distinct(guardcoord, guardpath):
            guardpath.append(guardcoord)

        if is_exting(guardcoord):
            guard_has_left = True
            break

        desired_step = get_direction(guardcoord[2])
        next_position = [
            guardcoord[0] + desired_step[0],
            guardcoord[1] + desired_step[1],
        ]
        if input[next_position[0]][next_position[1]] == "#":
            guardcoord = turn_the_guard(guardcoord)
            desired_step = get_direction(guardcoord[2])
        guardcoord = advance_the_guard(desired_step, guardcoord)
    print(guardpath)
    return guardpath


def is_distinct(coord_to_check, coordlist):
    for coord in coordlist:
        if coord_to_check[0] == coord[0] and coord_to_check[1] == coord[1]:
            return False
    return True


def advance_the_guard(desired_step, guardcoord):
    newguardcoord = [
        guardcoord[0] + desired_step[0],
        guardcoord[1] + desired_step[1],
        guardcoord[2],
    ]
    return newguardcoord


def turn_the_guard(guardcoord):
    direction = (directions.index(guardcoord[2]) + 1) % (len(directions))
    return [guardcoord[0], guardcoord[1], directions[direction]]


def get_direction(char):
    if char == "^":
        return [-1, 0]
    elif char == ">":
        return [0, 1]
    elif char == "V":
        return [1, 0]
    elif char == "<":
        return [0, -1]
    return [0, 0]


def is_exting(coord):
    exiting_cirumstances = [
        [0, "*", "^"],
        [len(input) - 1, "*", "V"],
        ["*", len(input[0]) - 1, ">"],
        ["*", "0", "<"],
    ]
    for circumstance in exiting_cirumstances:
        if (coord[0] == circumstance[0] or coord[1] == circumstance[1]) and coord[
            2
        ] == circumstance[2]:
            return True
    return False


print(len(walk_the_guard()))
