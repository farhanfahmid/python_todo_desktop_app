from contextlib import nullcontext

import functions

import FreeSimpleGUI as sg
import time
now = time.strftime("%b %d, %Y   %H:%M:%S")
label = sg.Text("What To Do Today?")
date = sg.Text(now)

input_box = sg.InputText(key="todo")

#define buttons
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
remove_button = sg.Button("Remove")
exit_button = sg.Button("Exit")

#define a list box that gets the added todo items and lists them
list_box = sg.Listbox(values = functions.get_todos(), key='todo_item',
                      enable_events=True, size=[45, 10])

#create a window with the defined elements
window = sg.Window('My To-Do App',
                   layout=[[date],
                            [label],
                           [input_box, add_button],
                           [list_box, edit_button, remove_button],
                           [exit_button]],

                   font=('Helvetica', 16))

while True:
    event, values = window.read() #displays the window
    print("event: ", event)
    print("values: ", values)

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo.title())
            functions.write_todos(todos)
            window['todo_item'].update(values=todos)  #give the instance of updated to-do list in real time and update values with new todos
            window['todo'].update(value='')

        case 'Edit':
            try:
                todo_to_edit = values['todo_item'][0]
                new_todo = values['todo']

                todos = functions.get_todos() #get current todos
                index = todos.index(todo_to_edit) #get index of the todo to replace
                todos[index] = new_todo.title() #replace existing todo with new todo
                functions.write_todos(todos) #write new updated list
                window['todo_item'].update(values=todos) #give the instance of updated to-do list in real time and update values with new todos
                window['todo'].update(value='')

            except IndexError:
                sg.popup("Please select an item first to edit")

        case 'todo_item':
            window['todo'].update(value = values['todo_item'][0]) #when clicking on a todo item, make the input box's todo text into that clicked to_do item

        case 'Remove':

            try:
                todo_to_remove = values['todo_item'][0]
                index = todos.index(todo_to_remove)
                todos.pop(index)
                functions.write_todos(todos)
                window['todo_item'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item to remove")

        case sg.WINDOW_CLOSED: break
        case 'Exit': break

window.close()