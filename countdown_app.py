import streamlit as st
import time

# Define the countdown function
def countdown():
    while st.session_state.remaining_time > 0:
        if st.session_state.stop:
            st.session_state.stop = False
            st.session_state.timer_running = False
            st.session_state.countdown_display = 'Countdown Stopped'
            break
        
        if st.session_state.restart:
            st.session_state.restart = False
            st.session_state.remaining_time = st.session_state.initial_time
            st.session_state.countdown_display = ''
            st.warning("Please set the time again.")
            break
        
        elapsed_time = time.time() - st.session_state.start_time
        st.session_state.remaining_time = max(st.session_state.initial_time - int(elapsed_time), 0)
        mins, secs = divmod(st.session_state.remaining_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        st.session_state.countdown_display = timer
        st.session_state.countdown_placeholder.text(timer)
        time.sleep(1)
    
    if st.session_state.remaining_time <= 0:
        st.session_state.countdown_placeholder.text('Time is Over!')
        st.session_state.notification_placeholder.text('Time is Over!')
        st.balloons()
        st.success('Time is Over!')
        st.session_state.timer_running = False

# Streamlit app
def main():
    st.title("Countdown Timer")

    st.markdown("""
    This app helps you set a countdown timer for your tasks. 
    You can start, stop, or restart the countdown. 
    When the countdown reaches zero, a notification will pop up.
    """, unsafe_allow_html=True)

    # Initialize session state variables
    if 'stop' not in st.session_state:
        st.session_state.stop = False
    if 'restart' not in st.session_state:
        st.session_state.restart = False
    if 'timer_running' not in st.session_state:
        st.session_state.timer_running = False
    if 'countdown_display' not in st.session_state:
        st.session_state.countdown_display = ''
    if 'remaining_time' not in st.session_state:
        st.session_state.remaining_time = 0
    if 'initial_time' not in st.session_state:
        st.session_state.initial_time = 0
    if 'start_time' not in st.session_state:
        st.session_state.start_time = 0
    if 'countdown_placeholder' not in st.session_state:
        st.session_state.countdown_placeholder = st.empty()
    if 'notification_placeholder' not in st.session_state:
        st.session_state.notification_placeholder = st.empty()

    # Time input
    t = st.number_input("Enter the time in seconds:", min_value=0, step=1, value=10)

    # Buttons for timer control
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Start Countdown"):
            if not st.session_state.timer_running:
                st.session_state.stop = False
                st.session_state.restart = False
                st.session_state.timer_running = True
                st.session_state.initial_time = t
                st.session_state.remaining_time = t
                st.session_state.start_time = time.time()
                countdown()
    
    with col2:
        if st.button("Stop Countdown"):
            st.session_state.stop = True
    
    with col3:
        if st.button("Restart Countdown"):
            st.session_state.restart = True

    # Display the countdown timer
    st.markdown(f'<h1 style="text-align: center; color: #61dafb;">{st.session_state.countdown_display}</h1>', unsafe_allow_html=True)

    # Add a unique and modern style
    st.markdown("""
    <style>
    .css-18e3th9 {
        background-color: #1e1e1e;
        color: #f5f5f5;
    }
    .css-1aumxhk {
        background-color: #007acc;
        color: #ffffff;
        border: none;
        border-radius: 5px;
        padding: 10px;
        margin: 5px;
        font-weight: bold;
    }
    .css-1aumxhk:hover {
        background-color: #005a9e;
    }
    .css-1p5f5p1 {
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
