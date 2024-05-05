import cow
import os

from cow import Cow


class FileCow:

    def __init__(self, name, filename):
        self.name = name
        self.filename = filename

        try:
            f = open(filename, "r")
            lines = f.readlines()
        except RuntimeError as e:
            print("MOOOOO!!!!!!")
            raise

        image = ""
        for line in lines:
            image += line

        self.set_image(image)

    def set_image(self, image):
        try:
            self.image = image
        except RuntimeError as e:
            print("Cannot reset FileCow Image")
            raise
