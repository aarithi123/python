class Cow:
    def __init__(self, name) -> None:
        self.name = name
        self.image = None

    #getter
    def get_name(self):
        retrun (self.name)

    def get_image(self):
        retrun (self.image)

    # setter
    def set_image(self, image):
        self.image = image


