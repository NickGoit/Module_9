
CONTACTS: dict = {}


def input_error(func):
    def wrapper():
        try:
            func()
        except KeyError:
            print('This contact is not found. Please try again')
        except ValueError:
            print('Please enter your data correctly and try again ')
        except IndexError:
            print('Please check arguments')
    return wrapper


@input_error
def greetings_fun():
    print('Greeting, How can I help you?')


@input_error
def adding_fun():
    name, phone = input('Please add your name and phone. Use space between them ').split()
    CONTACTS[name] = phone
    print(f'Contact {name} and {phone} was successfully added')


@input_error
def change_fun():
    name = input('Please type the name contact: ')
    while True:
        choice = input(f'Contact {name} has a phone {CONTACTS[name]}, Would you like to change? (Yes/No): ')
        if choice == 'Yes':
            new_phone = input('Please type a new phone')
            CONTACTS[name] = new_phone
            print(f'Contact {name} has changed phone number on {new_phone}')
            break
        elif choice == 'No':
            print('Your request was cancelled')
            break
        else:
            print('You command isn\'t recognised. Please try again')


@input_error
def find_fun():
    name = input('Please type are looking name: ')
    print(f'Under the {name} contact is recorded phone {CONTACTS[name]}')


@input_error
def show_all_fun():
    if CONTACTS:
        for name, phone in CONTACTS.items():
            print(f'|{name}   |   {phone}|')
    else:
        print('Contacts database is empty')


@input_error
def goodbay_fun():
    print('Thank you for applying our Bot-assist. Have a nice day')
    quit()


COMMANDS = {
    'hello': greetings_fun,
    'add': adding_fun,
    'change': change_fun,
    'phone': find_fun,
    'show all': show_all_fun,
    'good bye': goodbay_fun,
    'close': goodbay_fun,
    'exit': goodbay_fun
}


def main():
    while True:
        request = input('Please type command: ').casefold()
        if request in COMMANDS:
            COMMANDS[request]()
        else:
            print('Unknown command. Please try again: ')


if __name__ == '__main__':
    main()
