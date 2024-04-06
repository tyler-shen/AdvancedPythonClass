lines = []
with open("test.txt", "r") as f:
    for line in f:
        lines.append(line)
print(lines)

file = open("test2.txt", "w")
for line in lines:
    if "\n" in line:
        # line1, line2
        newLine = line[0:len(line)-1] + ";\n"
    else:
        # line3
        newLine = line + ";"
    file.write(newLine)
file.close()
