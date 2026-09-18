line = "ebal-kopal"

new_line = list(line.split("-"))

new_line[0], new_line[1] = new_line[1], new_line[0]

# new_line = reversed()

result = "-".join(new_line)
print(result)
