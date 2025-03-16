import fileinput

for line in fileinput.input("somefile.txt"):
    print(line, end="")

print("\nUsing with statement")
with open("somefile.txt") as f:
    for line in f:
        print(line, end="")
