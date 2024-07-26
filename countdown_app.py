import streamlit as st
import time

# Define the countdown function
def countdown(t):
    start_time = time.time()
    remaining_time = t
    
    countdown_placeholder = st.empty()  # Placeholder for the timer display
    notification_placeholder = st.empty()  # Placeholder for the notification message
    
    while remaining_time > 0:
        if st.session_state.stop:
            st.session_state.stop = False  # Reset the stop flag
            st.session_state.pause = False  # Ensure pause is off
            st.session_state.restart = False  # Ensure restart is off
            st.session_state.timer_running = False  # Timer is stopped
            st.session_state.countdown_display = 'Countdown Stopped'
            break
        
        if st.session_state.restart:
            st.session_state.restart = False  # Reset the restart flag
            st.session_state.timer_running = False  # Ensure timer is stopped
            st.session_state.countdown_display = ''  # Clear the countdown display
            notification_placeholder.text('Set Your Time')  # Prompt to set time again
            st.experimental_rerun()  # Force a rerun of the app
            return  # Exit the countdown function to restart the process
        
        if st.session_state.pause:
            st.session_state.countdown_display = 'Countdown Paused'
            while st.session_state.pause:
                time.sleep(0.1)  # Wait until pause is released
        else:
            elapsed_time = time.time() - start_time
            remaining_time = max(t - int(elapsed_time), 0)
            mins, secs = divmod(remaining_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            st.session_state.countdown_display = timer
            countdown_placeholder.text(timer)
            time.sleep(1)
    
    if remaining_time <= 0:
        countdown_placeholder.text('Time is Over!')
        notification_placeholder.text('Time is Over!')
        st.balloons()  # Show a notification (balloons animation) when the countdown finishes
        st.success('Time is Over!')  # Show a success notification
        st.session_state.timer_running = False  # Ensure timer is stopped

# Streamlit app
def main():
    st.title("Countdown Timer")

    # Display introductory text
    st.markdown("""
    This app helps you set a countdown timer for your tasks. 
    You can start, pause, stop, or restart the countdown. 
    When the countdown reaches zero, a notification will pop up.
    """, unsafe_allow_html=True)

    # Initialize session state variables
    if 'stop' not in st.session_state:
        st.session_state.stop = False
    if 'pause' not in st.session_state:
        st.session_state.pause = False
    if 'restart' not in st.session_state:
        st.session_state.restart = False
    if 'timer_running' not in st.session_state:
        st.session_state.timer_running = False
    if 'countdown_display' not in st.session_state:
        st.session_state.countdown_display = ''

    t = st.number_input("Enter the time in seconds:", min_value=0, step=1, value=10)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Start Countdown"):
            if not st.session_state.timer_running:
                st.session_state.stop = False
                st.session_state.pause = False
                st.session_state.restart = False
                st.session_state.timer_running = True
                countdown(t)
    
    with col2:
        if st.button("Pause Countdown"):
            st.session_state.pause = not st.session_state.pause
    
    with col3:
        if st.button("Stop Countdown"):
            st.session_state.stop = True
    
    with col4:
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
