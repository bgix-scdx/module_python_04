import sys


class Utils:
    """For colored messages/errors"""
    def error(message: str) -> None:
        print(f"\033[1;31m{message}\033[m")

    def Print(message: any, r=255, g=255, b=255, finish='\n') -> None:
        """
        Docstring for Print

        :param message: String or List to be printed
        :type message: str, list, dict
        :param r: Red value (0 - 255)
        :param g: Green value (0 - 255)
        :param b: Blue value (0 - 255)
        :param finish: Send a message
        """
        if (type(message) is dict or type(message) is list):
            for mes in message:
                print(f"\033[38;2;{r};{g};{b}m{mes}\033[0m", end=finish)
            print("")
        else:
            print(f"\033[38;2;{r};{g};{b}m{message}\033[0m", end=finish)


def ft_archive_creation() -> None:
    file = None
    Utils.Print("=== Initiating protocol SHARK ===",
                255, 0, 0)
    Utils.Print("Pen Experiment and New Isotop Security",
                125, 0, 0)
    try:
        Utils.Print(f"Opening '{sys.argv[1]}'.",
                    195, 215, 0)
        with open(sys.argv[1], "x") as file:
            count = 0
            pos = 0
            for i in sys.argv:
                if pos <= 1:
                    pos += 1
                    continue
                count += file.write(f"{i}\n")
                Utils.Print(f"Log [{pos - 1}] [{i}]",
                            0, 255, 150)
                pos += 1
            Utils.Print(f"Text writen with a total of {count} char added.",
                        0, 0, 255)
    except FileExistsError:
        Utils.error(f"File {sys.argv[1]} already exists.")
    except IndexError:
        Utils.error(f"No arguments were provided. ./{sys.argv[0]} <file> "
                    "<content to write>")
    finally:
        if file:
            file.close()
            Utils.Print(f"File {sys.argv[1]} was closed on the way out.",
                        195, 215, 0)
        Utils.Print("=== Ended protocol SHARK ===",
                    255, 0, 0)


if __name__ == "__main__":
    ft_archive_creation()
