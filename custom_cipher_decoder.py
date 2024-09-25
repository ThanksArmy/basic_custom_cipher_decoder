def decode_cipher(input_string):
    numbers = [int(n) for n in input_string.split()]
    decoded_message = ''

    for num in numbers:
        if num < 0:
            decoded_message += chr(-num)
        else:
            octal_value = format(num, 'o')
            decoded_message += chr(int(octal_value, 8))

    return decoded_message

input_string = "57 73 73 64 26 -108 79 -99 71 26 73 72 26 81 73 79 76 26 -109 69 64 78 65 76 -109 27"
decoded_message = decode_cipher(input_string)
print("Decoded Message:", decoded_message)



