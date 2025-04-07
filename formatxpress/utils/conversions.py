from os import makedirs


class Conversions:
    def __init__(self, path, name):
        self.path = path
        self.name = name
        makedirs(self.path, exist_ok=True)
