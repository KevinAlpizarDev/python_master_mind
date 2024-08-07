from colorama import Fore, Style, init

init(autoreset=True)


class UserColors:
    def __init__(self, length):
        self.length = length

    def get_colors(self):
        user_colors = []
        for _ in range(self.length):
            # saludo = input("Hola cual es tu nombre:  ")
            # print("  saludo = input("Hola cual es tu nombre:  ")")
            # print(f"{Fore.WHITE}acontinuacion un ejemplo de una jugada{Style.RESET_ALL}")
            # print(f"{Fore.WHITE}Ejemplo: {Style.RESET_ALL}")
            # print(f"{Fore.RED}red + ENTER{Style.RESET_ALL}")
            # print(f"{Fore.GREEN}green + ENTER{Style.RESET_ALL}")
            # print(f"{Fore.BLUE}blue + ENTER{Style.RESET_ALL}")
            # print(f"{Fore.YELLOW}yellow + ENTER{Style.RESET_ALL}")
            print()
            print(f"{Fore.WHITE}COMIENZA A JUGAR!{Style.RESET_ALL}")
            print()
            color = input().strip().lower()
            user_colors.append(color)
        return user_colors
