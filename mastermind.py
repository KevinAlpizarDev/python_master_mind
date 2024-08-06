from colorama import Fore, Back, Style, init

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

        
        txt ="""
                      _          _ _               ____  _ _   _     
                     | | ___  __| (_) __   _____  / ___|(_) |_| |__  
                  _  | |/ _ \/ _` | | \ \ / / __| \___ \| | __| '_ \ 
                 | |_| |  __/ (_| | |  \ V /\__ \  ___) | | |_| | | |
                  \___/ \___|\__,_|_|   \_/ |___/ |____/|_|\__|_| |_|
                                                                                                       """
###################################################################################################################
# Definir el color de texto y el color de fondo
        text_color = Fore.WHITE
        bg_color = Back.GREEN

# Imprimir el texto con color de fondo
        print(f"{text_color}{bg_color}{txt}{Style.RESET_ALL}")
        
        
        
        
        
        
        print(f"{Fore.WHITE} Secret colors: {self.secret_colors}")
        print()
        while not win:
            user_colors = self.user_colors.get_colors()
            feedback = ["X"] * self.length

            for index, color in enumerate(user_colors):
                if color in self.secret_colors:
                    feedback[index] = "❌"
                    if self.secret_colors[index] == user_colors[index]:
                        feedback[index] = "⭐"

            array_with_color = self.print_colors.print_colors(user_colors)
            data = [[array_with_color, feedback]]

            for index, fila in enumerate(data):
                print(f"Ronda: °{index + 1}  |{' '.join(fila[0])}|  {fila[1]}")

            if all(fb == "⭐" for fb in feedback):
                win = True
                print(f"{Fore.GREEN}¡Acabas de ganar, bye!{Style.RESET_ALL}")
            if counter + 1 >= self.length:
                print(f"{Fore.RED}Ya no quedan más intentos, perdiste{Style.RESET_ALL}")
                break

            counter += 1
