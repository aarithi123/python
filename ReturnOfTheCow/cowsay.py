# Lab 8: The Cow strikes back
import sys

import file_cow
from dragon import Dragon
from heifer_generator import HeiferGenerator
from file_cow import FileCow


def list_cows():
    cows = HeiferGenerator.get_cows()
    return cows


def list_file_cows():
    file_cows = HeiferGenerator.get_file_cows()
    return file_cows


def find_cow(name, cows):
    for cow in cows:
        if cow.name == name:
            print(name)
            return cow


def find_file_cow(name, file_cows):
    for cow in file_cows:
        if cow.name == name:
            print(name)
            return cow


# Define Global variables

def main():
    args = sys.argv
    print(args[0])
    print(args[1])
    cows = list_cows()
    file_cows = list_file_cows()

    if len(sys.argv) == 1:
        "Format nor supported"
        return

    if args[1] == '-l':
        print(f'Cows available: {" ".join([cow.name for cow in cows])}')
        print(f'File cows available: {" ".join([cow.name for cow in file_cows])}')
    elif args[1] == '-n':
        cow = find_cow(args[2], cows)
        if cow:
            print()
            message = ' '.join(args[3:])
            print(message)
            print(cow.image)
            print(cow.name)

            if isinstance(cow, Dragon):
                if cow.can_Breathe_fire():
                    print("This dragon can breathe fire")
                else:
                    print("This dragon cannot breathe fire")
        else:
            print(f'Could not find {args[2]} cow!')
    elif args[1] == '-f':
        cow = find_file_cow(args[2], file_cows)
        if cow:
            print()
            message = ' '.join(args[3:])
            print(message)
            print(cow.image)
            print(cow.name)
        else:
            print(f'Could not find {args[2]} cow!')

    else:
        print()
        message = ' '.join(args[1:])
        print(message)
        print(cows[0].image)


'''
    # if no argument provided
    if len(sys.argv) == 1:
        "Format nor supported"
        return

    # when list of cows is printed
    if sys.argv[1] == "-l":
        print("cows avaialble: ", end=' ')
        for cow in cows:
            print(cow.get_name(), end=' ')
        return
'''

if __name__ == '__main__':
    main()
