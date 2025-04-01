import os

def clear_screen():
    os.system('clear')

def new_lines(num: int) -> None:
    for x in range(num):
        if x <= num:
            print('\n')
