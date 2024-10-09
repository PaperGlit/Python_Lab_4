import os
import random
import string
from BLL.classes.incorrect_character_exception import IncorrectCharacterException
from BLL.classes.incorrect_font_format_exception import IncorrectFontFormatException


class Ascii:
    def __init__(self, text, width = 0, height = 0, color = "\033[39m", shadow = "#", text_s ="#", highlight ="#"):
        self.text = text
        self.shadow = shadow
        self.text_s = text_s
        self.highlight = highlight
        self.height = height
        self.width = self.__verify_width(width)
        if color == "random":
            self.color = "\033[" + str(random.randint(31, 39)) + "m"
        else:
            self.color = color
        self.color_reset = "\033[0m"
        self.font = self.__load_font()

    def print(self):
        art = self.__format_art()
        print(self.color + art +  self.color_reset)
        return art

    def __wrap_art(self):
        wrapped_text = []
        length = 0
        current_line = ""
        for char in self.text:
            if char in ["M", "W", "4"]:
                length += 8
            elif char in self.font:
                length += 7
            else:
                raise IncorrectCharacterException("The character " + char + " is not a valid character.")
            if length > self.width:
                wrapped_text.append(current_line)
                current_line = char
                length = 8 if char in ["M", "W", "4"] else 7
            else:
                current_line += char
        if current_line:
            wrapped_text.append(current_line)
        return wrapped_text

    def __format_art(self):
        wrapped_art = self.__wrap_art()
        art_lines = []
        for chunk in wrapped_art:
            unsorted_art_list = []
            for art_char in chunk:
                formatted_font_art = ""
                font_art = self.font[art_char.upper()]
                for char in font_art:
                    match char:
                        case "*":
                            char = self.highlight
                        case "#":
                            char = self.text_s
                        case "&":
                            char = self.shadow
                        case " ":
                            pass
                        case "\n":
                            pass
                        case _:
                            raise IncorrectFontFormatException("The character " + char + " is not a valid character in a font.txt.")
                    formatted_font_art += char
                split_font_art = formatted_font_art.splitlines()
                unsorted_art_list.append(split_font_art)
            art_list = ["".join(row) for row in zip(*unsorted_art_list)]
            art_lines.append("\n".join(art_list))
        art = "\n\n".join(art_lines)
        art_height = len(art.splitlines())
        height_diff = self.height - art_height
        padding = "\n" * (height_diff // 2) if height_diff > 0 else ""
        art = padding + art + padding
        return art

    @staticmethod
    def __load_font():
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
    def __verify_width(width):
        if width <= 0:
            try:
                return os.get_terminal_size().columns
            except OSError:
                return 220
        elif width > 0:
            return width
        else:
            return 220