import os
import random
import string
import GlobalVariables as Global


class Ascii:
    def __init__(self, text, width = Global.width, height = Global.height, color = Global.color):
        self.text = text
        self.font = self.__load_font()
        self.width = width
        self.height = height
        if color == "random":
            self.color = "\033[" + str(random.randint(31, 39)) + "m"
        else:
            self.color = color

    def print(self):
        art = self.format_art()
        print(self.color + art + Global.color_reset)
        return art

    def wrap_art(self):
        wrapped_text = []
        length = 0
        current_line = ""
        for char in self.text:
            if char in ["M", "W", "4"]:
                length += 8
            else:
                length += 7
            if length > self.width:
                wrapped_text.append(current_line)
                current_line = char
                length = 8 if char in ["M", "W", "4"] else 7
            else:
                current_line += char
        if current_line:
            wrapped_text.append(current_line)
        return wrapped_text

    def format_art(self):
        wrapped_art = self.wrap_art()
        art_lines = []
        for chunk in wrapped_art:
            unsorted_art_list = [self.font[char.upper()].splitlines() for char in chunk]
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