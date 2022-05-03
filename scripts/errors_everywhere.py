message = "6374667b596f754669786564416c6c4572726f7273217d"
list_of_bytes = []
list_of_ascii = []

def decode(hex):
    ascii_str = chr(int(hex, 16))
    return ascii_str

index = 0
while index < len(message):
    byte = (message[index] + message[index + 1])
    list_of_bytes.append(byte)
    index += 2

for byte in list_of_bytes:
    ascii_char = decode(byte)
    list_of_ascii.append(ascii_char)

print("".join(list_of_ascii))
