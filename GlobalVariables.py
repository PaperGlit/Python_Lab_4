import os


try:
    width = os.get_terminal_size().columns
except OSError:
    width = 220
height = 0
color = "\033[39m"
color_reset = "\033[0m"
shadow = "#"
text = "#"
highlight = "#"