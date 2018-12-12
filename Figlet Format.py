from pyfiglet import figlet_format
from colorama import init
from termcolor import colored

init()

def print_art(msg, color):
    valid_colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')

    if color not in valid_colors:
        color = yellow

    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)

msg = input("What would you like to say? ")
color = input("What color would you like your text to be? ")
print_art(msg, color)