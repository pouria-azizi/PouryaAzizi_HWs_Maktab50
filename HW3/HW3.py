def password_validate(password):
    val = True

    if len(password) < 6:
        print('length should be at least 6')
        val = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in "~!@#$%^&*()-+" for char in password):
        print('Password should have at least one of the symbols ~!@#$%^&*()-+')
        val = False
    if val:
        return val


def main():
    password = input("Enter the Password: ")
    if password_validate(password):
        print("Password is valid")
    else:
        print("Password is invalid!!")


if __name__ == '__main__':
    main()
