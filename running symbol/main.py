import time

# WITH = input("Введи ширину")
# WITH = int(WITH)
# print(type(WITH))
# HEIGHT = input("Введи высоту")
# HEIGHT = int(HEIGHT)
# print(type(HEIGHT))

# SYMBOL = input("Введи символ")
# print(type(SYMBOL))


# line = print(SYMBOL * WITH)

# print(line * HEIGHT)

# box_width = 3
# box_height = 3

# line = ""

# symbol = int("#")


# grid = [[0 for _ in range(3)] for _ in range(3)]


# # for row in grid:
# #     print(row)


def table(w=50, h=12, symbol="-"):
    line = ""
    for _ in range(w):
        line += symbol

    for _ in range(h):
        print(line, end="\n")

    my_list = list(line)

    for i in range(len(my_list)):
        my_list[i] = "x"
        time.sleep(0.1)
        changed_line = "".join(my_list)
        print(changed_line, end="\r")
        # print(line)

    # print(my_list)
    # print((line + "\n") * h, end="")

    # xyi = print((line + "\n") * h, end="")
    # print(type(xyi))

    # table_list = list(line)
    # print(table_list)

    # item = table_list[0]
    # if item in table_list == "-":
    #     new_line += "#"
    # else:
    #     new_line = item

    # print(new_line)
    # return table_list


table()

# new_table = table()


# print(new_table[0], new_table[-1])


# table_w = int(input())
# table_h = int(input())
# table_symbol = input()
# table(table_w, table_h, table_symbol)
