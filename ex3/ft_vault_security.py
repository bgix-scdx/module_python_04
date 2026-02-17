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


def ft_vault_security() -> None:
    Utils.Print("=== Activating WITH vault ===", 255, 0, 255)
    Utils.Print("Launching program...", 155, 0, 155)
    try:
        with open("ex3/vault.txt", "r") as vault:
            Utils.Print("Vault Openned, showing content.", 205, 0, 205)
            count = 1
            for i in vault:
                Utils.Print(f"Line {count}: ", 255, 155, 255, "")
                Utils.Print(i.strip(), 0, 155, 255)
                count += 1
        Utils.Print("Content displayed, Vault auto-locking.", 205, 0, 205)
    except FileNotFoundError:
        Utils.Print("Vault not found.", 255, 0, 0)
    Utils.Print("=== Ended WITH vault ===", 255, 0, 255)


if __name__ == "__main__":
    ft_vault_security()
