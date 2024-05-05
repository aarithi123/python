#convert a hexadecimal character to a decimal
def hex_char_decode(digit):
    decimal_char = ""
    char = digit.lower()
    if char <= '0' or char <= '9':
        decimal_char = char
    elif char == 'a':
        decimal_char = 10
    elif char == 'b':
        decimal_char = 11
    elif char == 'c':
        decimal_char = 12
    elif char == 'd':
        decimal_char = 13
    elif char == 'e':
        decimal_char = 14
    elif char == 'f':
        decimal_char = 15
    return int(decimal_char)

#convert a hexadecimal string to a decimal value
def hex_string_decode(hex):
    if hex[0:2] == "0x":
        new_hex = hex[2:len(hex)]
    else:
        new_hex = hex
    dec_value = 0
    for i in range(0, len(new_hex)):
        j = len(new_hex) - (i + 1)
        dec_value = dec_value + (int(hex_char_decode(new_hex[i])) * 16 ** j)
    return dec_value

#convert a binary string to a decimal value
def binary_string_decode(binary):
    if binary[0:2] == "0b":
        new_binary = binary[2:len(binary)]
    else:
        new_binary = binary
    dec_value = 0
    for i in range(0, len(new_binary)):
        j = len(new_binary) - (i + 1)
        dec_value = dec_value + (int(hex_char_decode(new_binary[i])) * 2 ** j)
    return dec_value

#convert a binary string to decimal then to hexadecimal
def binary_to_hex(binary):
    remainder = 0
    quotient = 1
    hex_str = ''
    num = binary_string_decode(binary)

    while quotient > 0:
        quotient = num // 16
        remainder = num % 16
        num = quotient
        if 0 <= remainder <= 9:
            r = remainder
        elif remainder == 10:
            r = 'a'
        elif remainder == 11:
            r = 'b'
        elif remainder == 12:
            r = 'c'
        elif remainder == 13:
            r = 'd'
        elif remainder == 14:
            r = 'e'
        elif remainder == 15:
            r = 'f'
        hex_str += str(r)
    return hex_str[::-1]


def main():
    menu_option = 1
#diplay menu options until user exits
    while menu_option != 4:
        print("Decoding Menu")
        print("-" * 13)
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            hex_string = input("Please enter the numeric string to convert: ")
            dec_string = hex_string_decode(hex_string)
            print(f'Result: {dec_string}')
            print()
        elif menu_option == 2:
            binary_string = input("Please enter the numeric string to convert: ")
            binary_string = binary_string_decode(binary_string)
            print(f'Result: {binary_string}')
            print()
        elif menu_option == 3:
            binary_str = input("Please enter the numeric string to convert: ")
            bin_to_hex = binary_to_hex(binary_str)
            print(f'Result: {bin_to_hex}')
            print()
        else:
            print("Goodbye!")
            exit()

if __name__ == "__main__":
    main()