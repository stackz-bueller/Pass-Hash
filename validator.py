import setup
from getpass import getpass
import algo

Algorithm = algo.Algorithm

# Validator
def PasswordsValidator():
    color = setup.Setup.color
    try:
        while True:
            pass1 = getpass(prompt='Please enter your password: ')

            pass2 = getpass(prompt='Please re-enter your password: ')

            if pass1 == pass2:
                if Algorithm.empty(pass2):
                    print(color.BOLD,
                          '\nPassword is empty, please input characters',
                          color.END)
                elif not Algorithm.findPassLen(pass2):
                    print(color.BOLD,
                          '\nPassword must be 8 or more characters!\n',
                          color.END)
                elif not Algorithm.findChar(pass2):
                    print(
                        color.BOLD,
                        '\nThis password is not valid, it has no letters!\n',
                        color.END)
                elif not Algorithm.findChapChar(pass2):
                    print(
                        color.BOLD,
                        '\nThis password is not valid, it lacks a capital letter!\n',
                        color.END)
                elif not Algorithm.findNumb(pass2):
                    print(
                        color.BOLD,
                        '\nThis password is not valid, it lacks a number!\n',
                        color.END)
                elif not Algorithm.findSpecChar(pass2):
                    print(
                        color.BOLD,
                        '\nThis password is not valid, it lacks a special character!\n',
                        color.END)
                elif Algorithm.findFirst(pass2):
                    print(
                        color.BOLD,
                        '\nThis password is not valid, it contains a \'!\' or \
                          \'?\' at the front of password!\n', color.END)
                elif Algorithm.findRepeats(pass2):
                    print(
                        color.BOLD,
                        '\nThis password is not valid, it contains \
                          repeating characters or numbers!\n', color.END)
                elif Algorithm.findSpace(pass2):
                    print(
                        color.BOLD,
                        '\nThis password is not valid, it contains a space!\n',
                        color.END)
                else:
                    print('\n', color.BOLD, color.DARKCYAN,
                          'This password is accepted!', color.END)
                    break
            else:
                print(color.BOLD, '\nYour passwords do not match!\n',
                      color.END)
        return pass2

    except KeyboardInterrupt:
        print('Interrupted!')