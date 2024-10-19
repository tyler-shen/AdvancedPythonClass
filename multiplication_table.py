print("mutliplication table:")

for row in range(1, 10):
    for col in range(1, row+1):
        print(f"{col}x{row}={row*col:2d}", end='  ')
    print()
