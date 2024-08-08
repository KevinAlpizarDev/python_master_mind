from colorama import Fore, Style, init

init(autoreset=True)


class UserColors:
    def __init__(self, length):
        self.length = length

    def get_colors(self):
        user_colors = []
        for _ in range(self.length):
        
            print()
            print(
                f"{Fore.WHITE}fight!{Style.RESET_ALL}"
            )
            
            print()
            
            color = input().strip().lower()
            user_colors.append(color)
        return user_colors
