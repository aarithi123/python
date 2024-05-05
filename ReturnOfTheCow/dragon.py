import cow
from cow import Cow
class Dragon(Cow):
    def __init__(self, name, image):
        Cow.__init__(self, name)
        Cow.set_image(self, image)

    def can_Breathe_fire(self):
        return True
