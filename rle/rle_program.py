# import ConsoleGfx
from console_gfx import ConsoleGfx


# translate RLE or raw data into a hex string
def to_hex_string(data):
    hex_value = ''
    for i in range(0, len(data)):
        if data[i] == 10:
            hex_value += 'a'
        elif data[i] == 11:
            hex_value += 'b'
        elif data[i] == 12:
            hex_value += 'c'
        elif data[i] == 13:
            hex_value += 'd'
        elif data[i] == 14:
            hex_value += 'e'
        elif data[i] == 15:
            hex_value += 'f'
        else:
            hex_value += str(data[i])
    return str(hex_value)


# return number of runs of data in an image data set
def count_runs(flat_data):
    number_of_runs = 0
    current_char = ""
    same_char_count = 0

    for n in range(0, len(flat_data)):
        if current_char == "":
            current_char = flat_data[n]
            number_of_runs = number_of_runs + 1
            same_char_count = same_char_count + 1
        else:
            if flat_data[n] != current_char:
                current_char = flat_data[n]

                if same_char_count > 15:
                    quotient = same_char_count // 15
                    remainder = same_char_count % 15
                    number_of_runs = number_of_runs + quotient
                    if remainder > 0:
                        number_of_runs = number_of_runs + 1
                else:
                    number_of_runs = number_of_runs + 1

                same_char_count = 1
            else:
                same_char_count = same_char_count + 1

    if same_char_count > 15:
        quotient = same_char_count // 15
        remainder = same_char_count % 15
        number_of_runs = number_of_runs + quotient
        if remainder > 0:
            number_of_runs = number_of_runs + 1
    else:
        number_of_runs = number_of_runs + 1

    return int(number_of_runs - 1)


# returns encoding in RLE of the raw data passed in
def encode_rle(flat_data):
    previous_num = 0
    repeat = 0
    rle = []
    first_num = 0
    for i in flat_data:
        j = i
        if first_num == 0:
            previous_num = j
            repeat = 1
            first_num = 1
        else:
            if previous_num == j:
                repeat += 1
            else:
                # check if the same number is repeated more than 15 times
                if repeat > 15:
                    quotient = repeat // 15
                    remainder = repeat % 15

                    for i in range(0, quotient):
                        rle += 15, previous_num

                    if remainder > 0:
                        rle += remainder, previous_num

                    repeat = 1
                    previous_num = j
                else:
                    rle += repeat, previous_num
                    repeat = 1
                    previous_num = j
    # append the last set of terms
    if repeat > 15:
        quotient = repeat // 15
        remainder = repeat % 15
        for i in range(0, quotient):
            rle += 15, previous_num
        if remainder > 0:
            rle += remainder, previous_num
    else:
        rle += repeat, previous_num

    return rle


# returns decompressed size RLE data
def get_decoded_length(rle_data):
    even_index = 0
    for i in range(0, len(rle_data)):
        if i % 2 == 0:
            even_index += int(rle_data[i])
    return even_index


# returns the decoded data set from RLE encoded data
def decode_rle(rle_data):
    rle_list = []
    counter = 0
    for i in range(0, len(rle_data)):
        if i % 2 == 0:
            for j in range(0, int(rle_data[i])):
                if counter == 0:
                    k = i + 1
                    rle_list.append(int(rle_data[k]))
                    counter += 1
                else:
                    rle_list.append(int(rle_data[k]))
            counter = 0
    return rle_list


# translates a string in hex into byte data
def string_to_data(data_string):
    rle_data = []
    for i in range(0, len(data_string)):
        j = data_string[i].lower()
        if j == 'a':
            x = 10
        elif j == 'b':
            x = 11
        elif j == 'c':
            x = 12
        elif j == 'd':
            x = 13
        elif j == 'e':
            x = 14
        elif j == 'f':
            x = 15
        else:
            x = j
        rle_data.append(int(x))
    return rle_data


# translates RLE data into a human-readable representation
def to_rle_string(rle_data):
    rle_string = ''
    length = len(rle_data)
    for i in range(0, len(rle_data)):
        if i % 2 == 0:
            rle_string += str(rle_data[i])
        else:
            rle = to_hex_string([rle_data[i]])
            length -= 2
            if length >= 2:
                rle_string += rle + ':'
            else:
                rle_string += rle
    return rle_string


# translates a string in human-readable RLE format into RLE byte data
def string_to_rle(rle_string):
    hold_rle = []
    repetition = ''
    string_rle = rle_string.split(':')
    for item in string_rle:
        last_char = item[len(item) - 1]
        convert_char = string_to_data(last_char)
        for i in range(0, len(item) - 1):
            repetition += item[i]
        hold_rle.append(int(repetition))
        repetition = ''
        hold_rle += convert_char

    return hold_rle


def main():
    # Define variables
    menu_option = 1
    previous_option = 0

    print("Welcome to the RLE image encoder!")
    print("Displaying Spectrum Image:")
    # display test rainbow from ConsoleGfx
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    # print menu until user inputs 0
    while menu_option != 0:
        print()
        print("RLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")
        print()

        menu_option = int(input("Select a Menu Option: "))
        # load user file
        if menu_option == 1:
            image_file = input("Enter name of file to load: ")
            ConsoleGfx.load_file(image_file)

        # load test image
        elif menu_option == 2:
            ConsoleGfx.test_image
            print("Test image data loaded.")

        # read RLE data in decimal notation with delimiters
        elif menu_option == 3:
            read_rle = input("Enter an RLE string to be decoded: ")

        # read RLE data in hex notation without delimiters
        elif menu_option == 4:
            read_hex = input("Enter the hex string holding RLE data: ")

        # read flat data in hex notation
        elif menu_option == 5:
            read_flat_data = input("Enter the hex string holding flat data: ")

        # display test image
        elif menu_option == 6:
            print("Displaying image...")
            ConsoleGfx.display_image(ConsoleGfx.test_image)

        # convert current data into human-readable RLE representation
        elif menu_option == 7:
            if previous_option == 3:
                print("RLE representation: " + read_rle.lower())
            elif previous_option == 4:
                result_1 = string_to_data(read_hex)
                result_2 = to_rle_string(result_1)
                print("RLE representation: " + result_2)
            elif previous_option == 5:
                result_1 = encode_rle(read_flat_data)
                result_2 = to_rle_string(result_1)
                print("RLE representation: " + result_2)

        # convert current data into RLE hex representation
        elif menu_option == 8:
            if previous_option == 3:
                result_1 = string_to_rle(read_rle)
                result_2 = to_hex_string(result_1)
                print("RLE hex values: " + result_2)
            elif previous_option == 4:
                print("RLE hex values: " + read_hex.lower())
            elif previous_option == 5:
                result_1 = encode_rle(read_flat_data)
                result_2 = to_hex_string(result_1)
                print("RLE hex values: " + result_2)

        # display current flat data in hex representation
        elif menu_option == 9:
            if previous_option == 3:
                result_1 = string_to_rle(read_rle)
                result_2 = decode_rle(result_1)
                result_3 = to_hex_string(result_2)
                print("Flat hex values: " + result_3)
            elif previous_option == 4:
                result_1 = string_to_data(read_hex)
                result_2 = decode_rle(result_1)
                result_3 = to_hex_string(result_2)
                print("Flat hex values: " + result_3)
            elif previous_option == 5:
                print("Flat hex values: " + read_flat_data)

        # exit the loop
        elif menu_option == 0:
            menu_option == 0

        previous_option = menu_option


if __name__ == "__main__":
    main()
