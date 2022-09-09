user = {
    'pin': 1234,
    'balance': 100
}

def withdraw_cash():
    try:
        amount = float(input("Enter the amount of money you would like to withdraw from your current account: "))
        if amount > user['balance']:
            raise Exception

    except Exception:
        if amount > user['balance']:
            print("Insufficient balance, cannot withdraw {} GBP currently.\nPlease try again".format(amount))

    except ValueError:
        print('Please enter the correct number')
    else:
        if amount <= user['balance']:
            print('Amount accepted.')
            user['balance'] = user['balance'] - amount
            print("{} GBP has been successfully withdrawn from your current account.\n"
                  "Your remaining balance is {} GBP.".format(amount, user['balance']))

def balance_enquiry():
    print('Total balance is {} GBP'.format(user['balance']))


def pin_code():

        print('Welcome to Money ATM\n' 
              'Please insert your bank card.')
        user_pin = int(input('Enter 4 digit pin: '))
        return user_pin

def validate_pin_code():

    try:
        pin = int(pin_code())
        count = 3
        if pin != user['pin']:
            raise Exception


    except Exception:
        if pin != user['pin']:
            for i in range(3):
                count = count - 1
                if count == 2 and pin != user['pin']:
                    print('Invalid pin.')
                    print('{} attempts remaining.'.format(count))
                    pin = int(input('Enter pin: '))
                elif count == 1 and pin and pin != user['pin']:
                    print('Invalid pin.')
                    print('{} attempt remaining.'.format(count))
                    pin = int(input('Enter pin: '))
                elif count == 0 and pin != user['pin']:
                    print('Invalid pin.')
                    print('O attempts remaining.\nPlease remove your card.')
                elif pin == user['pin']:
                    print('Login successful')


    except ValueError:
        print('Invalid entry. Enter number.')

    else:
        print('Login successful\n')

def main():
        validate_pin_code()

if __name__ == '__main__':
        main()

def user_enquiries():
    try:
        print("Enter 1 to withdraw cash from your card.\n"
                      "Enter 2 for balance enquiries. \n"
                      "Enter 3 to quit the current session.\n")

        user_input = int(input("Enter the number indicating the action you wish to take:  "))
        if int(user_input) == 0 or int(user_input) > 3:
            raise Exception

    except ValueError:
        print('Unrecognised format. Please try again and enter a number between 1 and 3')

    except Exception:
        if int(user_input) == 0 or int(user_input) > 3:
            print('Invalid number. Please try again and enter a number between 1 and 3')
    else:
        if user_input == 1:
            withdraw_cash()
        elif user_input == 2:
            balance_enquiry()
        elif user_input == 3:
            print('Exit program. Please remove your card')

    # return pin

def main2():
    user_enquiries()

if __name__ == '__main__':
    main2()
