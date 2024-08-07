from colorama import Fore

class PrintColors:
    def print_colors(self, colors):
        array_with_color = []
        for color in colors:
            if color == "red":
                array_with_color.append(Fore.RED + "red")
            elif color == "blue":
                array_with_color.append(Fore.BLUE + "blue")
            elif color == "green":
                array_with_color.append(Fore.GREEN + "green")
            elif color == "yellow":
                array_with_color.append(Fore.YELLOW + "yellow")
        return array_with_color
