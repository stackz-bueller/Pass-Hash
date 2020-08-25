class Setup:
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'


def printPasswordSpecs():
    print(
        'Welcome\nPlease create a password according to the following specifications\n'
    )

    print(
        '\tThe password must have at least:', Setup.color.RED,
        '8 characters\n\n', Setup.color.END, Setup.color.GREEN,
        '\tThe password must contain at least one of the following:\n\t\t' +
        'A Letter\n\t\tA Capital Letter\n\t\tA Special Character\n',
        Setup.color.END)
    print(
        Setup.color.RED,
        '\tThe password must not contain:\n\t\tA Leading \'!\' or \'?\'' +
        '\n\t\tRepeating Characters or Numbers greater than 2\n\t\tA Whitespace\n',
        Setup.color.END)