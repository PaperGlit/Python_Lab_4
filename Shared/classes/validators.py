import os
from DAL.functions.upload_to_file import write


class Validators:
    @staticmethod
    def validate_main_prompt(prompt, console):
        match prompt:
            case "1":
                console.enter_text()
            case "2":
                console.change_symbols()
            case "3":
                console.change_width_and_height()
            case "4":
                console.change_color()
            case "5":
                console.justify()
            case _:
                return

    @staticmethod
    def save_file_prompt(prompt, text):
        if prompt == "y":
            try:
                write(text)
            except IOError:
                print("The file could not be uploaded, please try again")

    @staticmethod
    def validate_shading(prompt, console, type):
        while True:
            if prompt.strip() != "" or len(prompt) == 1:
                match type:
                    case 1:
                        console.ascii.shadow = prompt
                    case 2:
                        console.ascii.text_s = prompt
                    case 3:
                        console.ascii.highlight = prompt
                    case _:
                        raise ValueError("Wrong type detected")
                return
            else:
                print("Please enter a valid shading symbol (only one allowed)")

    @staticmethod
    def validate_dimensions(prompt, console):
        while True:
            try:
                width = int(prompt)
                console.ascii.width = width
                print("Width changed successfully")
                return
            except ValueError:
                print("Please enter an integer")

    @staticmethod
    def validate_color(prompt, console):
        match prompt:
            case "1":
                console.ascii.color = "\033[31m"
            case "2":
                console.ascii.color = "\033[32m"
            case "3":
                console.ascii.color = "\033[33m"
            case "4":
                console.ascii.color = "\033[34m"
            case "5":
                console.ascii.color = "\033[35m"
            case "6":
                console.ascii.color = "\033[36m"
            case "7":
                console.ascii.color = "\033[37m"
            case "8":
                console.ascii.color = "random"
            case "0":
                console.ascii.color = "\033[39m"
            case _:
                print("Invalid color choice, please try again.")
                return
        print("Color changed successfully")
        return

    @staticmethod
    def validate_justify(prompt, console):
        match prompt:
            case "1":
                console.ascii.justify = "left"
            case "2":
                console.ascii.justify = "center"
            case "3":
                console.ascii.justify = "right"
            case "_":
                print("Invalid orientation choice, please try again.")
                return
        print("Orientation changed successfully")
        return

    @staticmethod
    def verify_width(width):
        if width > 0:
            return width
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 200