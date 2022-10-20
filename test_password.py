import task02

def main():
    password = input("Please enter your password: ")


    result = task02.check_password(password)

    msg =f"Your password is {result}" if isinstance(result, str) else "User data invalid"

    print(msg)

if __name__ == "__main__":
    main()
