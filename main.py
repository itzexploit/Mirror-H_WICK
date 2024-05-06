from requests import post
from pystyle import Colorate , Colors
from colorama import Fore , init
from os import system , name

init()

red = Fore.LIGHTRED_EX; green = Fore.LIGHTGREEN_EX; blue = Fore.LIGHTBLUE_EX; yellow = Fore.LIGHTYELLOW_EX; cyan = Fore.LIGHTCYAN_EX; white = Fore.LIGHTWHITE_EX; magenta = Fore.LIGHTMAGENTA_EX;

system('cls' if name == 'nt' else 'clear')

banner = """

            __   __   __   __                     __       
    |\/| | |__) |__) /  \ |__) __ |__|    |  | | /  ` |__/ 
    |  | | |  \ |  \ \__/ |  \    |  |    |/\| | \__, |  \ 
                                                        
            Created By John Wick Team Pytho Learn

"""

print(Colorate.Horizontal(Colors.red_to_blue , banner , 2))

def main():
    username = input(f'\n  {red}[{yellow}${red}]{cyan} Username Mirror-H   {red}:{green} ')
    defpage = input(f'\n  {red}[{yellow}${red}]{cyan} Defaced Page {red}:{green} ')
    data = {
        "user":username,
        "url":defpage,
        "ben_orosbu_cocuguyum":"1"
    }
    try:
        post('https://mirror-h.org/site-send',data=data)
        print(f'\n  {red}[{yellow}+{red}]{green} Uploaded')
    except:
        print(Colorate.Horizontal(Colors.red_to_yellow , '\n  Cant Upload !!!' , 2))
    
main()
