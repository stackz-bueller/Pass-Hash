import saltAndHash as sugar
import validator as valid
import setup
import time

color = setup.Setup.color
true = ['y', 'yes', 'YES' 'Y', '1', 'True', 'true', 'TRUE']
false = ['n', 'no', 'NO' 'N', '0', 'False', 'false', 'FALSE']

def checker():
    possible_password = valid.get_pass()

    if sugar.Engine.verify_password(hash, possible_password):
        del possible_password
        print(color.BOLD, color.DARKCYAN,'\n\tThe password is verified!',color.END)
        print(color.BOLD, color.GREEN, '\n\tScript End', color.END)
        return True

    else:
        print(color.BOLD, color.YELLOW,
              '\n\tThe password is not verified!\n', color.END)
        return False

def main():
    setup.printPasswordSpecs()
    input('Press enter to continue...\n')
    valid_ = valid.PasswordsValidator()
    return (sugar.Engine.hash_password(valid_))


if __name__ == '__main__':
    hash = main()
    time.sleep(1)
    print('The stored hash of password is: \n\n{}'.format(hash))
    time.sleep(1)
    try:
        while True:
            answer = input(
                '\nDo you want to check your password properly works? y/n: ')

            if answer in true:
                if checker():
                    break   

            elif answer in false:
                print(color.BOLD, color.PURPLE, '\n\tScript End', color.END)
                break
          

    except KeyboardInterrupt:
        time.sleep(0.5)
        print(color.RED,'\n\n\tProgram Interrupted',color.END)
