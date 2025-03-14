import streamlit as st
import functions

todos = functions.get_todos()

def add_task():
    task = st.session_state['new_task'] + "\n"
    todos.append(task.title())
    functions.write_todos(todos)
    st.session_state['new_task'] = ""


st.title("To-Do Web App")
st.subheader("Welcome! What TO DO Today?")
st.text_input(label="", placeholder="Add a Task",
              on_change=add_task, key='new_task')


for index, task in enumerate(todos):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos) #write updated list after removing checked task
        del st.session_state[task]
        st.rerun()

# print("Yo")
# st.session_state


