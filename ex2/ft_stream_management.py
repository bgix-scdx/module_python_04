import sys


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


def ft_strean_management() -> None:
    stderr = sys.stderr
    stdout = sys.stdout
    try:
        while True:
            id = input("\033[38;2;255;0;80m==> Enter your Creditential: "
                       "\033[m")
            status = input("\033[38;2;255;0;80m==> Enter your Status: \033[m")
            confirm = input("\033[38;2;0;255mDo you confirm your id and"
                            " status: "
                            f"{id}, {status} <yes/no>\n\033[0m")
            while confirm.lower() != "yes" and confirm.lower() != "no":
                Utils.Print("/!\\ Incorrect value, please respond.",
                            255, 0, 0, None, stderr)
                confirm = input("\033[38;2;0;255mDo you confirm your id "
                                "and status: "f"{id}, {status} <yes/no>\n"
                                "\033[0m")
            if confirm.lower() == "no":
                Utils.Print("Access revoke, please try again...",
                            255, 0, 0, None, stderr)
                continue
            else:
                Utils.Print(f" -> Sending request as {id}",
                            0, 0, 255, None, stdout)
                Utils.Print("Connection Established !",
                            0, 255, 0, None, stdout)
                Utils.Print("Sending...",
                            0, 0, 255, None, stdout)
                Utils.Print(f"User: {id}\nReport Status: {status}",
                            0, 0, 255, None, stdout)
                Utils.Print("Report updated.",
                            255, 0, 0, None, stdout)
                Utils.Print("Mission remain undone, proceed.",
                            255, 0, 0, None, stderr)
                break
    except KeyboardInterrupt:
        Utils.Print("\nStopping Process.",
                    255, 0, 0, None, stderr)


if __name__ == "__main__":
    ft_strean_management()
