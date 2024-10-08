import os
import math
import random
import string

import GlobalVariables as Global
from pyfiglet import figlet_format, FigletFont


class Ascii:
    @staticmethod
    def load_font():
        keys = list(string.ascii_uppercase) + list(string.digits) + [".", ",", ";", "'", '"', "!", "?", " "]
        font = {}
        i = 0
        with open("Sources/font.txt", "r") as file:
            for line in file:
                if line.strip() == "$":
                    i+= 1
                elif i < len(keys):
                    key = keys[i]
                    if key not in font:
                        font[key] = line
                    else:
                        font[key] += line
        return font


    @staticmethod
    def verify_width(width):
        if width <= 0:
            try:
                return os.get_terminal_size().columns
            except OSError:
                return 220
        elif width > 0:
            return width
        else:
            return 220

    @staticmethod
    def print(text, random_color = False):
        font = Ascii.load_font()
        unsorted_art_list = []
        art_list = []
        for char in text.upper():
            unsorted_art_list.append(font[char].splitlines())
        for col in range(len(unsorted_art_list[0])):
            for row in unsorted_art_list:
                art_list.append(row[col])
            art_list.append("\n")
        art = "".join(art_list)
        if random_color:
            color = "\033[" + str(random.randint(31, 39)) + "m"
        else:
            color = Global.color
        art_height = len(art.splitlines())
        if Global.height > art_height:
            height = Global.height - art_height
        else:
            height = 0
        print(color + "\n" * math.ceil(height / 2) + art + "\n" * math.floor(height / 2) + Global.color_reset)
        return art