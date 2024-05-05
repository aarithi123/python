import sys
from cow import Cow
from dragon import Dragon
from heifer_generator import HeiferGenerator
from ice_dragon import IceDragon


# list cows
def list_cows():
    cows = HeiferGenerator.get_cows()
    return cows


# check if cow name is in cow list
def find_cow(name, cows):
    for cow in cows:
        if cow.name == name:
            return cow


def main():
    cows = list_cows()
    # output the available cows
    if sys.argv[1] == '-l':
        print(f"Cows available: {' '.join([cow.name for cow in cows])}")

    # output user entered message and cow if it is available
    elif sys.argv[1] == '-n':
        cow_name = sys.argv[2]
        cow_message = sys.argv[3:]
        correct_cow = find_cow(cow_name, list_cows())
        if correct_cow:
            print(' '.join(cow_message))
            print(correct_cow.image)
            # check if cow name is ice dragon and if method returns True or False
            if isinstance(correct_cow, IceDragon):
                print("This dragon cannot breathe fire.")
            # check if cow name is dragon and if method returns True or False
            elif isinstance(correct_cow, Dragon):
                print("This dragon can breathe fire.")
        else:
            print(f"Could not find {cow_name} cow!")

    # output user entered message with default cow
    else:
        message = sys.argv[1:]
        print(' '.join(message))
        print(cows[0].image)


if __name__ == "__main__":
    main()
