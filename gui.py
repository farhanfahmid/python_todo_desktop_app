import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do Item")

input_box = sg.InputText()

add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]]) #create a window with the defined elements
window.read() #displays the window
window.close()