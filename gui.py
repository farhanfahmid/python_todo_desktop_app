import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do Item")

input_box = sg.InputText(key="todo")

add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 16)) #create a window with the defined elements

while True:
    event, values = window.read() #displays the window
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] +"\n"
            todos.append(new_todo.title())
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED: break

window.close()