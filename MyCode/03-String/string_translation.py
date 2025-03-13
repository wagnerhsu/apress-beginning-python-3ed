# Create translation table
# Create translation table
original = "aeiou"
replacement = "12345"
trans_table = str.maketrans(original, replacement)

# Apply translation
text = "hello world"
translated = text.translate(trans_table)
print(translated)  # Output: h2ll4 w4rld