class Utils:
    """For colored messages/errors"""
    def error(message: str) -> None:
        print(f"\033[1;31m{message}\033[m")

    def Print(message: any, r=255, g=255, b=255, finish='\n', f=None) -> None:
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
                print(f"\033[38;2;{r};{g};{b}m{mes}\033[0m",
                      end=finish, file=f)
            print("")
        else:
            print(f"\033[38;2;{r};{g};{b}m{message}\033[0m",
                  end=finish, file=f)


def ft_crisis_response() -> None:
    Utils.Print("=== Absolue Bugz ===", 255, 0, 0)
    Utils.Print("Trying to open and access the file", 255, 0, 255)
    try:
        with open("Special.txt", "r+") as file:
            Utils.Print("File has been opened", 0, 255, 155)
            count = 1
            for i in file:
                Utils.Print(f"Line {count}: ", 255, 155, 255, "")
                Utils.Print(i.strip(), 0, 155, 255)
                count += 1
            if count > 1:
                Utils.Print("File Reading Ended", 255, 0, 255)
            else:
                Utils.Print("File is empty !", 255, 0, 155)
    except FileNotFoundError:
        Utils.error("Error, File could not be find.")
    except PermissionError:
        Utils.error("Error, You do not have the permission to open this file.")
    Utils.Print("==> Trying to create the file with FileExistError.", 255, 0)
    try:
        with open("ex4/Special.txt", "x") as file:
            Utils.Print("=> File was created as it did not exist.",
                        0, 255, 255)
            file.write("Hello World.\n")
    except FileExistsError:
        Utils.error("Error, The file already exist.")
    Utils.Print("=== ENDED ===", 255, 0, 0)


if __name__ == "__main__":
    ft_crisis_response()
