from functions import get_todos, write_todos #importing functions from functions.py file

import time
now = time.strftime("%b %d, %Y   %H:%M:%S")
print("It is", now)

prompt = "Type add, show, edit, remove, or exit list: "

# todos = []

while True:
    user_action = input(prompt)
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n" #extracts the part of the text after 'add'

        todos = get_todos() # calls the function that opens and reads file, with input as the filepath to the todos_file.txt

        todos.append(todo.title())

        write_todos(todos) # calls function that opens file and writes in it

    elif user_action.startswith('show'):
        todos = get_todos('todos_file.txt')

        for i, item in enumerate(todos):
            print(i+1, item.strip("\n")) # print items without extra vertical lines between items

    elif user_action.startswith('edit'):

        #error handling if user types 'edit string instead of integer'
        try:

            number = int(user_action[5:])
            index = number-1

            todos = get_todos()

            edited_todo = input("Replace todo: ")
            todos[index] = edited_todo.title() +'\n'

            write_todos(todos)

        except ValueError:
            print("Your command is invalid")
            user_action = input(prompt)
            continue # ignore the bottom codes and restart the loop


    elif user_action.startswith('remove'):

        try:

            todos = get_todos()

            number = int(user_action[7:])
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Item '{todo_to_remove}' was completed! "
            print(message)

        except IndexError:
            print("There is no item with that number ")

            continue
        except ValueError:
            print("Your command is invalid ")

            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Hey, you entered an unknown variable")

print("Bye bye!")

