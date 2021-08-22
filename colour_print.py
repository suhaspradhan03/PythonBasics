RED = '\u001b[31m'
BLUE = '\u001b[34m'
CYAN = '\u001b[36m'
RESET = '\u001b[0m'

# print(RED, "this will be in red")
# print("and so is this")
# print(BLUE, "this will be in blue")
# print("and so is this")
# print(CYAN, "this will be in CYAN")
# print("this will also be in CYAN")
# print(RESET, "this is normal")


def color_print(text: str ,effect: str) -> None:
    """
    print `text` using the ANSI sequences to change the color, etc.

    :param text: The text to print.
    :param effect: The effect we want. One of the constants
        defined at the start of this module
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


color_print("this will be in red", RED)
color_print("and so is this")
color_print("this will be in blue", BLUE)
color_print("and so is this")
color_print("this will be in CYAN", CYAN)
color_print("this will also be in CYAN")
color_print("this is normal", RESET)