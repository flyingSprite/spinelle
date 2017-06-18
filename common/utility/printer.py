
class PrintInColor(object):
    """Print log with color"""

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'

    @classmethod
    def red(cls, text):
        """
        Print red log.
        :param text: Need print text.
        :return: None
        """
        print(cls.RED + text + cls.END)

    @classmethod
    def green(cls, text):
        """
        Print green log.
        :param text: Need print text.
        :return: None
        """
        print(cls.GREEN + text + cls.END)

    @classmethod
    def yellow(cls, text):
        """
        Print yellow log.
        :param text: Need print text.
        :return: None
        """
        print(cls.YELLOW + text + cls.END)

    @classmethod
    def light_purple(cls, text):
        """
        Print light purple log.
        :param text: Need print text.
        :return: None
        """
        print(cls.LIGHT_PURPLE + text + cls.END)

    @classmethod
    def purple(cls, text):
        """
        Print purple log.
        :param text: Need print text.
        :return: None
        """
        print(cls.PURPLE + text + cls.END)
