# from colorama import Fore, Style, init

# init(autoreset=True)

# class UserColors:
#     def __init__(self, length):
#         self.length = length

#     def get_colors(self):
#         user_colors = []
#         for _ in range(self.length):
#             # saludo = input("Hola cual es tu nombre:  ")
#             # print("  saludo = input("Hola cual es tu nombre:  ")")
#             print(user_colors)
#             print(f"{Fore.GREEN}[red, green, blue, yellow] decida el orden de colores disponibles:{Style.RESET_ALL}")
#             color = input().strip().lower()
#             user_colors.append(color)
#         return user_colors
















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
            print(user_colors)
            print(f"{Fore.MAGENTA}[red, green, blue, yellow] decida el orden de colores disponibles:{Style.RESET_ALL}")
            color = input().strip().lower()
            user_colors.append(color)
        return user_colors

