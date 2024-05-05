from dragon import Dragon


# create subclass of the Dragon class
class IceDragon(Dragon):
    def __init__(self, name, image):
        Dragon.__init__(self, name, image)

    # always return False
    def can_breath_fire():
        return False

