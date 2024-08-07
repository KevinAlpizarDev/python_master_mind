from colorama import Back, Fore, Style, init

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
        print(f"{Fore.WHITE} Secret colors: {self.secret_colors}")
        txt = """                         
                                           ██████
         ╒▄                                ███████
           ▀▄,                             ████████▄
             ▀█▄                           ████████▄▄▄▄,
                ▀▄,                         ,████████████▄
                  ▀█▄                    ,▄███████████████
                     ▀█,               ,███████████████████
                       ▀█▄           ,█████▀███████████████▌
                          ▀█,       ▄███      `▀██▀▀▀▄██████
                            ▀█▄   ▄████            ,████████▌
                               ▐████▀▀           ▄▄██████████
                             ▄████▄▄▄,,          ▀▀▀▀████████▌
                         ▄▄█████████████              ▀█▀ ████
                    ▄▄█████████████████'                  " ▐█▌
               ,▄█████████████████████▌                   j████
            ▄▄██████████████████████▀▀                    j█████
         ▄▄██████████████████████        ▄███████          █████▌
      ▄████████████████████████▀'       ▐████  ███▄  ╓     ██████▄
    ▄██████████████████████████        ,███▀▀  ▀███▄▄▐█▄  ,███████▄
        ████████████████████████▌ █▄, ▐███▀▄   ╓ ████.█████████████▄
       █████████████████████████▌ ███▌▐█████   █ ████ ██████████████▌
          `▀▀███████████████████▌ ▐██ ▐████▌   ██████ ████████████████
             ╒███████████████████ ▐██ ▐█████   █████▌ ▐████████████████
               ▀█████████████████ ▐█▌ ██████   █████▌  █████████████████⌐
                 ▀███████████████▌ █  ██████▌  ██████  ▐█████████████████⌐
                   ▀██████████████ █ █████▌   ,██████▌  ██████████████████
                         ███▀▀▀▀▀▀` ▀█████▌  ▄████▀▀▀▀  ▀▀▀████████████████
                                                                          █ █▀▀ █▀▄ █   █ █ █▀   █▀ █ ▀█▀ █ █
                                                                        █▄█ ██▄ █▄▀ █   ▀▄▀ ▄█   ▄█ █  █  █▀█                                                                                    
                                                                                                             """

        ascii_winner = """     
 ██████   █████  ███    ███ ███████      ██████  ██    ██ ███████ ██████  
██       ██   ██ ████  ████ ██          ██    ██ ██    ██ ██      ██   ██ 
██   ███ ███████ ██ ████ ██ █████       ██    ██ ██    ██ █████   ██████  
██    ██ ██   ██ ██  ██  ██ ██          ██    ██  ██  ██  ██      ██   ██ 
 ██████  ██   ██ ██      ██ ███████      ██████    ████   ███████ ██   ██ 
                                                                          
                                                                          

        
        """

        Ascii_loser = """
████████ ██   ██ ███████ 
   ██    ██   ██ ██      
   ██    ███████ █████   
   ██    ██   ██ ██      
   ██    ██   ██ ███████ 
                         

██████  ███████ ███████ ██ ███████ ████████ ███████ ███    ██  ██████ ███████ 
██   ██ ██      ██      ██ ██         ██    ██      ████   ██ ██      ██      
██████  █████   ███████ ██ ███████    ██    █████   ██ ██  ██ ██      █████   
██   ██ ██           ██ ██      ██    ██    ██      ██  ██ ██ ██      ██      
██   ██ ███████ ███████ ██ ███████    ██    ███████ ██   ████  ██████ ███████ 
                                                                              
                                                                              

███    ██ ███████ ██    ██ ███████ █████       ███████ ██    ██ ██████  ██████  ███████ ███    ██ ██████  ███████ ██████  ███████ 
████   ██ ██      ██    ██ ██      ██   ██     ██      ██    ██ ██   ██ ██   ██ ██      ████   ██ ██   ██ ██      ██   ██ ██      
██ ██  ██ █████   ██    ██ █████   ██████      ███████ ██    ██ ██████  ██████  █████   ██ ██  ██ ██   ██ █████   ██████  ███████ 
██  ██ ██ ██       ██  ██  ██      ██   ██          ██ ██    ██ ██   ██ ██   ██ ██      ██  ██ ██ ██   ██ ██      ██   ██      ██ 
██   ████ ███████   ████   ███████ ██   ██     ███████  ██████  ██   ██ ██   ██ ███████ ██   ████ ██████  ███████ ██   ██ ███████ ██ ██ ██ 
                                                                                                                                  
                                                                                                                                  
                        

        
        """

        # Definir el color de texto y el color de fondo
        text_color = Fore.BLACK
        bg_color = Back.WHITE

        # Imprimir el texto con color de fondo
        print(f"{text_color}{bg_color}{txt}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Attention, Rebels and Imperials!{Style.RESET_ALL}")
        print(
            f"{Fore.WHITE}Prepare for battle. The fate of the galaxy rests in your hands. May the Force be with you.{Style.RESET_ALL}"
        )
        print()
        print(f"{Fore.WHITE}Example: {Style.RESET_ALL}")
        print(f"{Fore.RED}red + ENTER{Style.RESET_ALL}")
        print(f"{Fore.BLUE}blue + ENTER{Style.RESET_ALL}")
        print(f"{Fore.GREEN}green + ENTER{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}yellow + ENTER{Style.RESET_ALL}")
        print("")
        print(
            f"{Fore.WHITE}Use the power of your mind and let the Force guide you...{Style.RESET_ALL}"
        )
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
                print(f"{Fore.BLUE}{Ascii_loser}{Style.RESET_ALL}")
            if counter + 1 >= self.length:
                # print(f"{Fore.RED}Ya no quedan más intentos, perdiste{Style.RESET_ALL}")
                print(f"{Fore.RED}{ascii_winner}{Style.RESET_ALL}")
                ascii_winner
                break

            counter += 1
