input = open("input").read().splitlines()

safe_reports = 0

for report in input:
    levels = report.split(" ")
    safe = True
    ascending = "unknown"

    for i, level in enumerate(levels):
        if i > 0:
            if int(levels[i - 1]) > int(level):
                if ascending == "true":
                    safe = False
                ascending = "false"
            elif int(levels[i - 1]) < int(level):
                if ascending == "false":
                    safe = False
                ascending = "true"
            difference = abs(int(levels[i - 1]) - int(level))
            if difference > 3 or difference < 1:
                safe = False
    if safe:
        safe_reports += 1
        # print(report)

print(safe_reports)
