import random
import textwrap
import GlobalVariables as Global
from BLL.classes.ascii import Ascii
from pyfiglet import FigletFont, figlet_format
import DAL.functions.upload_to_file as file_upload


class Console:
    @staticmethod
    def prompt():
        Ascii.print("ASCIIFY", True)
        while True:
            prompt = input("1 - Enter text\n"
                           "2 - Select font automatically\n"
                           "3 - Change font\n"
                           "4 - Current font\n"
                           "5 - Change width and height\n"
                           "6 - Change color\n"
                           "Your choice: ")
            match prompt:
                case "1":
                    Console.enter_text()
                case "2":
                    Console.auto_font()
                case "3":
                    Console.change_font()
                case "4":
                    print("Current font: " + Global.font)
                case "5":
                    Console.change_width_and_height()
                case "6":
                    Console.change_color()
                case _:
                    return

    @staticmethod
    def enter_text():
        text = input("Enter text: ")
        ftext = Ascii.print(text)
        save_prompt = input("Do you want to save the text? (y/n): ").lower()
        if save_prompt == "y":
            while True:
                file_name = input("Enter file name: ")
                if file_name.strip() != "":
                    if not file_name.endswith(".txt"):
                        file_name += ".txt"
                    try:
                        file_upload.write(ftext, file_name)
                        print("The art was uploaded successfully")
                        break
                    except IOError:
                        print("An error occurred during file upload, please try again")
                else:
                    print("Please enter a valid file name")

    @staticmethod
    def auto_font():
        text = input("Enter text: ")
        symbols = input("Enter a set of characters that should be in the ASCII art: ")
        font_symbols = set(symbols) | {" ", "\n"}
        fonts = FigletFont.getFonts()
        random.shuffle(fonts)
        for font in fonts:
            random_art = figlet_format(text, font=font, width=Global.width)
            random_art_chars = set(random_art)
            if sorted(random_art_chars) ==  sorted([" ", "\n"]):
                continue
            elif sorted(random_art_chars) == sorted(font_symbols):
                print("Found font:" + font)
                Global.font = font
                Ascii.print(text)
                return
        print("No fonts were found, please try again with a narrower set of characters")

    @staticmethod
    def change_font():
        new_font = input("Enter the new font you want to choose\n"
                         "You can also use 'font' to see all fonts available or 'random' to choose a random font\n"
                         "Your choice: ")
        if new_font in FigletFont.getFonts():
            Global.font = new_font
            print("Font changed successfully")
        elif new_font.lower() == "font":
            print("Available fonts:\n" + textwrap.fill(", ".join(FigletFont.getFonts()), width=Global.width))
        elif new_font.lower() == "random":
            Global.font = random.choice(FigletFont.getFonts())
            print("Randomly selected font: " + Global.font)
        else:
            print("Invalid font")

    @staticmethod
    def change_width_and_height():
        while True:
            width_prompt = input("Enter the width of an ASCII art\n"
                      "(any non-positive value will reset it to default values\n"
                      "Your choice: ")
            try:
                width = int(width_prompt)
                Global.width = Ascii.verify_width(width)
                print("Width changed successfully")
            except ValueError:
                print("Please enter an integer")
                continue
            height_prompt = input("Enter the height of an ASCII art\n"
                                  "(any non-positive value will reset it to default values\n"
                                  "Your choice: ")
            try:
                height = int(height_prompt)
                Global.height = height
                print("Height changed successfully")
                break
            except ValueError:
                print("Please enter an integer")
                continue

    @staticmethod
    def change_color():
        color_prompt = input("Enter the color of your ASCII art:\n"
                             "1 - Red\n"
                             "2 - Green\n"
                             "3 - Yellow\n"
                             "4 - Blue\n"
                             "5 - Magenta\n"
                             "6 - Cyan\n"
                             "7 - Light gray\n"
                             "0 - Default\n"
                             "Your choice: ")
        match color_prompt:
            case "1":
                Global.color = "\033[31m"
            case "2":
                Global.color = "\033[32m"
            case "3":
                Global.color = "\033[33m"
            case "4":
                Global.color = "\033[34m"
            case "5":
                Global.color = "\033[35m"
            case "6":
                Global.color = "\033[36m"
            case "7":
                Global.color = "\033[37m"
            case "0":
                Global.color = "\033[39m"
            case _:
                print("Invalid color choice, please try again.")
                return
        print("Color changed successfully")