import saltAndHash as sugar
import validator as valid
import setup as Setup


def main():
    Setup.printPasswordSpecs()
    input('Press enter to continue...')
    
    return sugar.Engine.hash_password(valid.PasswordsValidator())



if __name__ == '__main__':
    print(main())
