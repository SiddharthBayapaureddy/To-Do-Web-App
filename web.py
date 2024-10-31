import streamlit as st 
from Functions import function

to_dos = function.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    


st.title('To-Do Web App')
st.subheader('This is my todo app')
st.write('Siddharth B')

for todo in to_dos:
    st.checkbox(todo)

st.text_input(label='Enter a To Do',
               placeholder='Add a new todo',
               key='new_todo',
               on_change=add_todo)    