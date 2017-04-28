
class PrintInColor(object):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHT_PURPLE = '\033[94m'
    PURPLE = '\033[95m'
    END = '\033[0m'

    @classmethod
    def red(cls, text):
        print(cls.RED + text + cls.END)

    @classmethod
    def green(cls, text):
        print(cls.GREEN + text + cls.END)

    @classmethod
    def yellow(cls, text):
        print(cls.YELLOW + text + cls.END)

    @classmethod
    def light_purple(cls, text):
        print(cls.LIGHT_PURPLE + text + cls.END)

    @classmethod
    def purple(cls, text):
        print(cls.PURPLE + text + cls.END)
