import streamlit as st

# Initialize the session state for todo_list if it doesn't exist
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []

# Function to add a task to the todo list
def add_task():
    task = st.text_input('Please enter your task', key='new_task')
    if task:
        st.session_state.todo_list.append(task)

# Function to remove a completed task from the todo list
def complete_task(index):
    st.session_state.todo_list.pop(index)

# Header for the app
st.header('Todo App')

# Input field for adding a new task
add_task()

# Display the todo list
for i, task in enumerate(st.session_state.todo_list):
    is_completed = st.checkbox(f'{i+1}. {task}', key=f'task_{i}')
    if is_completed:
        complete_task(i)
        st.experimental_rerun()  # Rerun the app to update the UI after task removal
