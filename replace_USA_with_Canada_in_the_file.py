lines = []
with open("test.txt", "r") as f:
    for line in f:
        lines.append(line)
print(lines)

file = open("test.txt", "w")
for line in lines:
    newLine = line.replace("USA", "Canada")
    file.write(newLine)
file.close()
