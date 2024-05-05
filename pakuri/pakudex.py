from pakuri import Pakuri


class Pakudex:
    # initialize pakudex list, capacity, and size
    def __init__(self, capacity=20):
        self.my_pakudex = []
        self.capacity = capacity
        self.size = 0

    # getter methods for size and capacity
    def get_size(self):
        return len(self.my_pakudex)

    def get_capacity(self):
        return self.capacity

    # add pakuri to list except if duplicate or full
    def add_pakuri(self, species):
        if self.size == self.capacity:
            return False

        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species:
                return False

        self.my_pakudex.append(Pakuri(species))
        self.size += 1
        return True

    # append pakuri to a list and display
    def get_species_array(self):
        species_list = []
        if len(self.my_pakudex) == 0:
            return None
        else:
            for each_pakuri in self.my_pakudex:
                species_list.append(Pakuri.get_species(each_pakuri))
            return species_list

    # display stats of a given pakuri
    def get_stats(self, species):
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species:
                return [each_pakuri.attack, each_pakuri.defense, each_pakuri.speed]
        return None

    # sort each species name lexicographically
    def sort_pakuri(self):
        self.my_pakudex.sort(key=lambda pakuri: pakuri.get_species())
        '''for each_pakuri in self.my_pakudex:
            print(each_pakuri.get_species())'''

    # evolve a species if it is in the pakudex list
    def evolve_species(self, species):
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species:
                Pakuri.evolve(each_pakuri)
                return True
        return False


