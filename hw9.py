contacts = {}


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return 'Please input user name'
        except ValueError:
            return 'Please input correct phone number'
        except IndexError:
            return 'Please input name and phone number'
    return wrapper


@input_error
def add_change_number(message):
    name = ' '.join(message[:-1])
    phone = ''
    for i in filter(lambda x: x.isnumeric(), str(message[-1])):
        phone += i
    if name and phone:
        contacts[name.title()] = phone
        return f'Contact {name.title()} has been saved'
    else:
        raise IndexError


def goodbye():
    return 'Good bye!'


@input_error
def greeting(message):
    return 'How can I help you?'


@input_error
def show_all(message):
    contact = ''
    for name, phone in contacts.items():
        contact += f'{name} {phone}\n'
    return contact.rstrip('\n')


@input_error
def show_phone(message):
    name = ' '.join(message)
    return contacts[name.title()]


commands = {
    ('add', 'change'): add_change_number,
    'hello': greeting,
    'phone': show_phone,
    'show all': show_all
}


@input_error
def main():
    while True:
        text = input('>>>: ')
        command = text.lower().split()[0]
        message = text.lower().split()[1:]
        if text in ('good bye', 'close', 'exit', '.'):
            print(goodbye())
            break
        for item in commands:
            if command in item:
                print(commands[item](message))


if __name__ == "__main__":
    main()
