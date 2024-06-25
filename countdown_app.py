import streamlit as st
import time

# Define the countdown function
def countdown(t):
    countdown_placeholder = st.empty()
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        countdown_placeholder.text(timer)
        time.sleep(1)
        t -= 1

    countdown_placeholder.text('Fire in the hole!!')

# Streamlit app
def main():
    st.title("Countdown Timer")
    t = st.number_input("Enter the time in seconds:", min_value=0, step=1)
    if st.button("Start Countdown"):
        countdown(int(t))

if __name__ == "__main__":
    main()
