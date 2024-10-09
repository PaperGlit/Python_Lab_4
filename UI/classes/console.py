from BLL.classes.ascii import Ascii
import DAL.functions.upload_to_file as file_upload


class Console:
    def __init__(self):
        self.ascii = Ascii("ASCIIFY", color="random")
        self.__prompt()

    def __prompt(self):
        self.ascii.print()
        self.ascii.color = "\033[39m"
        while True:
            prompt = input("1 - Enter text\n"
                           "2 - Change font's symbols\n"
                           "3 - Change width and height\n"
                           "4 - Change color\n"
                           "Your choice: ")
            match prompt:
                case "1":
                    self.__enter_text()
                case "2":
                    self.__change_symbols()
                case "3":
                    self.__change_width_and_height()
                case "4":
                    self.__change_color()
                case _:
                    return

    def __enter_text(self):
        text = input("Enter text: ")
        self.ascii.text = text
        ftext = self.ascii.print()
        save_prompt = input("Do you want to save the text? (y/n): ").lower()
        if save_prompt == "y":
            try:
                file_upload.write(ftext)
            except IOError:
                print("The file could not be uploaded, please try again")

    def __change_symbols(self):
        while True:
            shadow_prompt = input("Enter symbol for shadows: ")
            if shadow_prompt.strip() != "" or len(shadow_prompt) == 1:
                self.ascii.shadow = shadow_prompt
            else:
                print("Please enter a valid shadows symbol (only one allowed)")
                continue
            text_prompt = input("Enter symbol for text: ")
            if text_prompt.strip() != "" or len(text_prompt) == 1:
                self.ascii.text_s = text_prompt
            else:
                print("Please enter a valid text symbol (only one allowed)")
                continue
            highlight_prompt = input("Enter symbol for highlights: ")
            if highlight_prompt.strip() != "" or len(highlight_prompt) == 1:
                self.ascii.highlight = highlight_prompt
            else:
                print("Please enter a valid highlights symbol (only one allowed)")
                continue
            break

    def __change_width_and_height(self):
        while True:
            width_prompt = input("Enter the width of an ASCII art\n"
                      "(any non-positive value will reset it to default values\n"
                      "Your choice: ")
            try:
                width = int(width_prompt)
                self.ascii.width = width
                print("Width changed successfully")
            except ValueError:
                print("Please enter an integer")
                continue
            height_prompt = input("Enter the height of an ASCII art\n"
                                  "(any non-positive value will reset it to default values\n"
                                  "Your choice: ")
            try:
                height = int(height_prompt)
                self.ascii.height = height
                print("Height changed successfully")
                break
            except ValueError:
                print("Please enter an integer")
                continue

    def __change_color(self):
        color_prompt = input("Enter the color of your ASCII art:\n"
                             "1 - Red\n"
                             "2 - Green\n"
                             "3 - Yellow\n"
                             "4 - Blue\n"
                             "5 - Magenta\n"
                             "6 - Cyan\n"
                             "7 - Light gray\n"
                             "8 - Random\n"
                             "0 - Default\n"
                             "Your choice: ")
        match color_prompt:
            case "1":
                self.ascii.color = "\033[31m"
            case "2":
                self.ascii.color = "\033[32m"
            case "3":
                self.ascii.color = "\033[33m"
            case "4":
                self.ascii.color = "\033[34m"
            case "5":
                self.ascii.color = "\033[35m"
            case "6":
                self.ascii.color = "\033[36m"
            case "7":
                self.ascii.color = "\033[37m"
            case "8":
                self.ascii.color = "random"
            case "0":
                self.ascii.color = "\033[39m"
            case _:
                print("Invalid color choice, please try again.")
                return
        print("Color changed successfully")