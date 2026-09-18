import time

list = []

for item in range(1, 6):

    list.append(item)
    time.sleep(0.5)
    print(list)


list_range = len(list)

for item in range(0, list_range, -1):
    list.pop(item)
    time.sleep(0.5)
    print(list)
