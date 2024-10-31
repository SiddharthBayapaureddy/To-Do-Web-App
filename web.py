import streamlit as st 
from Functions import function

to_dos = function.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    if todo.strip() == '':
        print('.')
    else:
        to_dos.append(todo)
        function.write_todos(to_dos)
        st.session_state['new_todo'] = ''
        



st.title('To-Do Web App')
st.subheader('This is my todo app')
st.write('Siddharth B')

to_dos = function.get_todos()

for indix,todo in enumerate(to_dos):
    checkbox = st.checkbox(todo,key=indix)
    if checkbox:
        to_dos.pop(indix)
        function.write_todos(to_dos)
        st.rerun()


st.text_input(label='Enter a To Do',
               placeholder='Add a new todo...',
               key='new_todo',
               on_change=add_todo)    