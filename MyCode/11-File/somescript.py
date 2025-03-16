# somescript.py
import sys
# Press Ctrl + Z followed by Enter to simulate EOF
text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)