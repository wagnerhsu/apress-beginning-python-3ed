# Converting bytes to bytearray
byte_data = bytes("hello", "utf-8")

byte_array = bytearray(byte_data)
print("Bytearray from Bytes:", byte_array)  # Output: bytearray(b'hello')

# Converting bytearray to bytes
new_byte_data = bytes(byte_array)
print("Bytes from Bytearray:", new_byte_data)  # Output: b'hello'