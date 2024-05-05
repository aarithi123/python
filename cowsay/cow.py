# create a cow class
class Cow:
    # initialize name and image
    def __init__(self, name) -> None:
        self.name = name
        self.image = None

    # get name
    def get_name(self):
        return self.name

    # get image
    def get_image(self):
        return self.image

    # set image
    def set_image(self, image):
        self.image = image




