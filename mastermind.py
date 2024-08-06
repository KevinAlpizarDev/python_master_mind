from colorama import init

from print_colors import PrintColors
from secret_colors import SecretColors
from user_colors import UserColors

init(autoreset=True)


class MasterMind:
    def __init__(self, colors, length):
        self.colors = colors
        self.length = length

        self.print_colors = PrintColors()
        self.secret_colors = SecretColors(self.colors, self.length).get_secret_colors
        self.user_colors = UserColors(self.length)

    def play(self):
        feedback = ["X"] * self.length
        win = False
        counter = 0
        txt = """
                      _          _ _               ____  _ _   _     
                     | | ___  __| (_) __   _____  / ___|(_) |_| |__  
                  _  | |/ _ \/ _` | | \ \ / / __| \___ \| | __| '_ \ 
                 | |_| |  __/ (_| | |  \ V /\__ \  ___) | | |_| | | |
                  \___/ \___|\__,_|_|   \_/ |___/ |____/|_|\__|_| |_|
                                                                                                       """
