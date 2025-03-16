import functions
import FreeSimpleGUI as sg
import time

import os

# Ensure todos file exists
if not os.path.exists("todos_file.txt"):
    with open("todos_file.txt", 'w') as file:
        pass

# # Load the correct image path for remove button
# complete_icon = functions.resource_path("G:\PYTHON PROJECTS\Python To-Do List App\images\complete.png")

# Define label for live clock
clock = sg.Text('', key='clock')

# Define the initial prompt
label = sg.Text("What To Do Today?")

# Define input box
input_box = sg.InputText(key="todo")

# Define buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")
exit_button = sg.Button("Exit")

# Define a list box that gets the added todo items and lists them
list_box = sg.Listbox(
    values=functions.get_todos(),
    key='todo_item',
    enable_events=True,
    size=[45, 5]
)

# Create a window with the defined elements
window = sg.Window(
    'To-Do App',
    layout=[
        [clock],
        [label],
        [input_box, add_button, edit_button],
        [list_box, remove_button],
        [exit_button]
    ],
    font=('Helvetica', 16)
)

while True:
    event, values = window.read(timeout=500)  # Display the window
    window['clock'].update(value=time.strftime("%b %d, %Y   %H:%M:%S"))  # Display the clock

    match event:
        case 'Add':
            new_todo = values['todo'].strip()
            if not new_todo: #Check if the input is empty
                sg.popup("Please type out a task to add it", font=('Helvetica', 14), title="Oops!")
            else:
                todos = functions.get_todos()
                todos.append(new_todo.title()  + "\n")
                functions.write_todos(todos)
                window['todo_item'].update(values=todos)  # Update list in real time
                window['todo'].update(value='')

        case 'Edit':
            try:
                todo_to_edit = values['todo_item'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo.title()
                functions.write_todos(todos)
                window['todo_item'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select an item first to edit", font=('Helvetica', 14), title="Oops!")

        case 'todo_item':
            window['todo'].update(value=values['todo_item'][0])

        case 'Remove':
            try:
                todo_to_remove = values['todo_item'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todo_item'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item to remove", font=('Helvetica', 14), title="Oops!")

        case 'Exit':
            break

    if event in (sg.WINDOW_CLOSED, None):
        break

window.close()
