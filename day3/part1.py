input = open("input").read()
total = 0


# approach without regex
for i, character in enumerate(input):
    if character != "m":
        continue
    if input[i + 1] != "u":
        continue
    if input[i + 2] != "l":
        continue
    if input[i + 3] != "(":
        continue
    print("mul( found at", i, input[i : (i + 12)])
    sequentialdigits = 0
    digitstomultiplyleft = []
    digitstomultiplyright = []
    j = 0
    for char in input[i + 4 :]:
        j += 1
        if sequentialdigits > 3:
            digitstomultiplyleft = []
            digitstomultiplyright = []
            break
        if char.isdigit():
            digitstomultiplyleft.append(char)
            sequentialdigits += 1
        elif char == "," and sequentialdigits > 0:
            # print("found valid first multiplicant", digitstomultiplyleft)
            sequentialdigits = 0
            for charright in input[i + 4 + j :]:
                # print(charright, sequentialdigits)
                if sequentialdigits > 3:
                    digitstomultiplyleft = []
                    digitstomultiplyright = []
                    break
                if charright.isdigit():
                    digitstomultiplyright.append(charright)
                    # print("found digit", charright, digitstomultiplyright)
                    sequentialdigits += 1
                elif charright == ")" and sequentialdigits > 0:
                    # print("found valid second multiplicant", digitstomultiplyright)
                    left = int("".join(digitstomultiplyleft))
                    right = int("".join(digitstomultiplyright))
                    multiple = left * right
                    print(
                        f"found valid instruction at {i}: {input[i:i+12]} or {left}*{right} which yields {multiple}"
                    )
                    total += multiple
                    print("total now", total)
                    break
        else:
            break


print(total)
