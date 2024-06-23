import streamlit as st
import time

# File handling functions

def readfile(filepath="ToDos.txt"):
    try:
        with open(filepath, "r") as file:
            todos = file.readlines()
    except FileNotFoundError:
        todos = []
    return todos

def writefile(filepath, todos):
    with open(filepath, "w") as file:
        file.writelines(todos)

def get_time():
    return time.strftime("%Y-%m-%d, %H:%M:%S")

# Load the to-dos from the file
todos = readfile()

# Initialize list for completed tasks
completed_tasks = []

# Streamlit application layout
st.title("To_Do List")
st.subheader("This is my to-do-List app.")
st.write(f"Current Date and Time: {get_time()}")


# Input for adding a new to-do
new_todo = st.text_input(label="Enter a to-do:", placeholder="Add a new to-do task", key="new_todo")

# Add button to add the new to-do
if st.button("Add Task"):
    if new_todo.strip() != "":
        todos.append(new_todo + "\n")
        writefile("ToDos.txt", todos)
        st.experimental_rerun()

# Display existing to-dos with checkboxes and remove button inline
for index, todo in enumerate(todos):
    # Checkbox and remove button for each to-do item
    col1, col2, col3 = st.columns([0.1, 0.7, 0.2])
    if col2.checkbox(f"{index + 1}. {todo.strip()}"):
        completed_tasks.append(todo)
    with col3:
        if st.button(f"Remove {index + 1}"):
            todos.pop(index)
            writefile("ToDos.txt", todos)
            st.experimental_rerun()

# Display completed tasks
if completed_tasks:
    st.subheader("Completed Tasks")
    for completed_task in completed_tasks:
        st.write(completed_task.strip())

# Display the tasks count
st.write(f"Total tasks: {len(todos)}")
