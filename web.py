import streamlit as st 
from Functions import function

to_dos = function.get_todos()

st.title('To-Do Web App')
st.subheader('This is my todo app')
st.write('Siddharth B')

for todo in to_dos:
    st.checkbox(todo)

st.text_input(label='Enter a To Do', placeholder='Add a new todo')    