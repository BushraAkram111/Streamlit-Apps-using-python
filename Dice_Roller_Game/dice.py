import random
import streamlit as st

# Dictionary to hold ASCII art for dice faces
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}

# Dictionary to define different types of dice
DICE_SIDES = {
    "4-sided": 4,
    "6-sided": 6,
    "8-sided": 8,
    "10-sided": 10,
    "12-sided": 12,
    "20-sided": 20
}

# Function to roll dice
def roll_dice(dice_type, num_dice):
    dice_sides = DICE_SIDES[dice_type]
    return [random.randint(1, dice_sides) for _ in range(num_dice)]

# Streamlit interface
st.title("Dice Roller")
st.subheader("Simulate rolling various types of dice and display the results.")

# Dice type selection
dice_type = st.selectbox("Select Dice Type:", list(DICE_SIDES.keys()))

# Number of dice selection
num_dice = st.number_input("Number of Dice:", min_value=1, max_value=10, value=1, step=1)

# Roll Dice button
if st.button("Roll Dice"):
    dice_rolls = roll_dice(dice_type, num_dice)
    total_sum = sum(dice_rolls)
    st.write(f"Rolling {num_dice} {dice_type} dice: {dice_rolls}")
    st.write(f"Total sum of all dice rolled: {total_sum}")

    for roll in dice_rolls:
        if dice_type == "6-sided":
            st.text("\n".join(DICE_ART[roll]))
        else:
            st.write(f"Rolled: {roll}")

# Clear Dice button
if st.button("Clear Results"):
    st.caching.clear_cache()
