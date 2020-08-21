import re


class Algorithm:
    def empty(password):
        return password == '' or password == ' '

    # Checks password string for a Capital Character
    def findPassLen(password):
        return len(password) >= 8

    # Checks for lowercase
    def findChar(password):
        return re.search('[a-z]', password)

    # Checks password string for a Capital Character
    def findChapChar(password):
        return re.search('[A-Z]', password)

    # Checks password string for a Number
    def findNumb(password):
        return re.search('[0-9]', password)

    # Checks password string for a Special Character
    def findSpecChar(password):
        return re.search('\W', password)

    # Checks password string for a Whitespace
    def findSpace(password):
        return re.search('\s', password)

    # Checks password string for Repeating Characters
    def findRepeats(password):
        bool = False
        for i in range(len(password) - 2):
            if password[i:i + 1] is password[i + 2:i + 3]:
                bool = True
                break
        return bool

    # Checks if first element in password string is '!' or '?'
    def findFirst(password):
        return re.match('[!?]', password)
