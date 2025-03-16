import process
f = open(r"somefile.txt")
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()

print("\nUsing with statement")
with open(r"somefile.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        process.process(line.strip('\n'))