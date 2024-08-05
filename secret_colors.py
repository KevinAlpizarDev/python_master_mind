import random

class SecretColors:
    def __init__(self, colors, length):
        self.colors = colors
        self.length = length
        self.secret_colors = random.sample(self.colors, self.length)

    @property
    def get_secret_colors(self):
        # return  self.secret_colors
        print( self.secret_colors)

