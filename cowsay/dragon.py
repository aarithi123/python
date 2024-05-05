from cow import Cow


# create subclass of the parent Cow class
class Dragon(Cow):
    def __init__(self, name, image):
        Cow.__init__(self, name)
        Cow.set_image(self, image)

    # always return True
    def can_breath_fire():
        return True
