from pakudex import Pakudex


def main():
    menu = True

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    max_capacity = input("Enter max capacity of the Pakudex: ")

    # repeat until valid max_capacity input
    capacity = True
    # check if input is numeric
    while capacity:
        if max_capacity.isnumeric():
            break
        else:
            print("Please enter a valid size.")
            max_capacity = input("Enter max capacity of the Pakudex: ")

    # check if input is positive
    while int(max_capacity) < 0:
        print("Please enter a valid size.")
        max_capacity = input("Enter max capacity of the Pakudex: ")

    pakudex = Pakudex(max_capacity)
    print(f"The Pakudex can hold {max_capacity} species of Pakuri.")

    # print menu each time
    while menu:
        print()
        print("Pakudex Main Menu")
        print("-" * 17)
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")
        print()

        menu_option = input("What would you like to do? ")

        # display pakuri in pakudex in the order contained
        if menu_option == '1':
            pakuri_list = pakudex.get_species_array()
            if pakuri_list:
                print("Pakuri In Pakudex:")
                for i in range(0, len(pakuri_list)):
                    print(f"{i + 1}. {pakuri_list[i]}")
            else:
                print("No Pakuri in Pakudex yet!")

        # prompt for a species and display its respective stats
        elif menu_option == '2':
            display_species = input("Enter the name of the species to display: ")
            species_type = pakudex.get_stats(display_species)
            if species_type:
                print(f"Species: {display_species}")
                print(f"Attack: {species_type[0]}")
                print(f"Defense: {species_type[1]}")
                print(f"Speed: {species_type[2]}")
            else:
                print("Error: No such Pakuri!")

        # add pakuri to pakudex list until its full or a duplicate
        elif menu_option == '3':
            if int(pakudex.get_size()) == int(pakudex.get_capacity()):
                print("Error: Pakudex is full!")
            else:
                add_species = input("Enter the name of the species to add: ")
                species_to_add = pakudex.add_pakuri(add_species)
                if species_to_add:
                    print(f"Pakuri species {add_species} successfully added!")
                else:
                    print("Error: Pakudex already contains this species!")

        # prompt for a species to evolve
        elif menu_option == '4':
            evolve_species = input("Enter the name of the species to evolve: ")
            species_to_evolve = pakudex.evolve_species(evolve_species)
            if species_to_evolve:
                print(f"{evolve_species} has evolved!")
            else:
                print("Error: No such Pakuri!")

        # sort pakuri in pakudex list lexicographically
        elif menu_option == '5':
            pakudex.sort_pakuri()
            print("Pakuri   have    been    sorted!")

        # quit and exit the loop
        elif menu_option == '6':
            print("Thanks for using Pakudex! Bye!")
            menu = False

        # invalid input
        else:
            print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()
