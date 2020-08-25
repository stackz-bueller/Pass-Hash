import saltAndHash as sugar
import validator as valid
import setup

color = setup.Setup.color
true = ['y', 'yes', 'YES' 'Y', '1', 'True', 'true', 'TRUE']
false = ['n', 'no', 'NO' 'N', '0', 'False', 'false', 'FALSE']


def main():
    setup.printPasswordSpecs()
    input('Press enter to continue...\n')

    return sugar.Engine.hash_password(valid.PasswordsValidator())


if __name__ == '__main__':
    hash = main()
    print('The stored hash of password is: \n\n{}'.format(hash))

    while True:
        answer = input(
            '\nDo you want to check your password properly works? y/n: ')

        if answer in true:
            possible_password = valid.get_pass()
            if sugar.Engine.verify_password(hash, possible_password):
                del possible_password
                print(color.BOLD, color.DARKCYAN, '\n\tThe password is verified!',
                      color.END)
                print(color.BOLD, color.GREEN, '\n\tScript End', color.END)
                break
            else:
                print(color.BOLD, color.YELLOW,
                      '\n\tThe password is not verified!', color.END)

        elif answer in false:
            print(color.BOLD, color.PURPLE, '\n\tScript End', color.END)
            break
