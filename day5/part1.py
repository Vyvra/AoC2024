input = open("input").read().splitlines()


# Parse input
page_ordering = []
updates = []
for i, line in enumerate(input):
    if line == "":
        for otherline in input[i + 1 :]:
            updates.append(otherline.split(","))
        break
    order = line.split("|")
    page_ordering.append(order)


def verify_updates():
    total = 0
    for i, update in enumerate(updates):
        # check if there are any instructions:
        if check_update(update):
            print(f"line {i},")
            total += int(get_middle(update))
    print(total)


def check_update(update):
    correct = True
    for instruction in update:
        # find order
        for order in page_ordering:
            if instruction in order:
                if not check_order_is_correct(order, update):
                    correct = False
                    break
        if not correct:
            break
    return correct


def check_order_is_correct(order, update):
    first = order[0]
    second = order[1]
    if not (first in update and second in update):
        return True
    firstfound = False
    for element in update:
        if element == first:
            firstfound = True
        if element == second and not firstfound:
            return False
    return True


def get_middle(array):
    length = len(array)
    return array[length // 2]


verify_updates()
