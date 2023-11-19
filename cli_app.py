def main():
    while True:
        user_input = input("Enter command: ").lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            result = process_command(user_input)
            print(result)

def error_handler(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'No user with this name'
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
    return inner

def hello_handler():
    return 'Hello, how I can help you?'

def add(parameters):
    name, phone = parameters.split()
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

def change(parameters):
    phone, new_phone, name = parameters.split()
    contacts[phone] = new_phone
    return f"Contact {name} was changed to {new_phone}."

def phone(parameters):
    name, phone = parameters
    print(f"Contact {name} have number {phone}")

def show_all(parameters):
    names, phones = parameters
    print(f"There is all contacts {names} with numbers {phones}.")

def exit_handler():
    return

def process_command(user_input):
    if user_input == "hello":
        return hello_handler()
    elif user_input.startswith("add"):
        return add(user_input.split(maxsplit=1)[1])
    elif user_input.startswith("change"):
        return change(user_input.split(maxsplit=1)[1])
    elif user_input.startswith("phone"):
        return phone(user_input.split(maxsplit=1)[1])
    elif user_input == "show all":
        return show_all()
    else:
        return "Invalid command. Available commands:\n'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', 'exit'."