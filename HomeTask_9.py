
CONTACTS: dict = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact is not found. Please try again'
        except ValueError:
            return 'Please enter your data correctly and try again'
        except IndexError:
            return 'Please check arguments'
        except TypeError:
            return 'Please enter correct data with space'
    return wrapper


@input_error
def greetings_fun():
    return 'Greeting, How can I help you?'


@input_error
def adding_fun(name, phone):
    CONTACTS[name] = phone
    return f'Contact {name} and {phone} was successfully added'


@input_error
def change_fun(name, new_phone):
    CONTACTS[name] = new_phone
    return f'Contact {name} has changed phone number on {new_phone}'


@input_error
def find_fun(name):
    return f'Under the {name} contact is recorded phone {CONTACTS[name]}'


@input_error
def show_all_fun():
    database = ''
    if CONTACTS:
        for name, phone in CONTACTS.items():
            database += f'|{name}   :   {phone}|\n'
        return database
    else:
        return 'Contacts database is empty'


@input_error
def goodbay_fun():
    return 'Thank you for applying our Bot-assist. Have a nice day'


def reaction(user_command, *data):
    if user_command in COMMANDS:
        return COMMANDS[user_command](*data)
    else:
        return 'Wrong command'


def data_analytic(data):
    if data == 'show all':
        user_command = 'show all'
        arguments = tuple()
        return reaction(user_command, *arguments)

    if data == 'good bye':
        user_command = 'good bye'
        arguments = tuple()
        return reaction(user_command, *arguments)

    (user_command, *arguments) = data.casefold().split()
    return reaction(user_command, *arguments)


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
        result = data_analytic(request)
        print(result)
        if result == 'Thank you for applying our Bot-assist. Have a nice day':
            break


if __name__ == '__main__':
    main()
