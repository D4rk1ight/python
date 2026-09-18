import time

line = "-" * 10
progress_bar = list(line)

for i in range(len(progress_bar)):
    progress_bar[i] = "█"
    result = "".join(progress_bar)
    time.sleep(0.25)
    print(result, end="\r")


# changed_line = "".join(progress_bar)
# print(changed_line)
# for i in range
