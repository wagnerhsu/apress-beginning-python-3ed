import process
filename = "somefile.txt"
with open(filename) as f:
    char = f.read(1)
    while char:
        process.process(char)
        char = f.read(1)

with open(filename) as f:
    while True:
        char = f.read(1)
        if not char:
            break
        process.process(char)
# The loop_over_char.py script reads a file one character at a time and processes each character using the process module.      