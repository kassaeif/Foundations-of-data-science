import streamlit as st

# Set title of the app
st.title("Streamlit App with Conditional Logic and Dropdowns")

# Sidebar dropdowns
st.sidebar.header("Select Options")

# First dropdown
option_1 = st.sidebar.selectbox(
    "Choose a value for option 1:",
    ["Option A", "Option B", "Option C"]
)

# Second dropdown
option_2 = st.sidebar.selectbox(
    "Choose a value for option 2:",
    ["Value 1", "Value 2", "Value 3"]
)

# Conditional logic using if and elif
if option_1 == "Option A" and option_2 == "Value 1":
    st.write("You selected Option A and Value 1.")
elif option_1 == "Option B" and option_2 == "Value 2":
    st.write("You selected Option B and Value 2.")
elif option_1 == "Option C" and option_2 == "Value 3":
    st.write("You selected Option C and Value 3.")
else:
    st.write(f"You selected **{option_1}** for option 1 and **{option_2}** for option 2.")

# Additional conditional logic example
if option_2 == "Option A":
    st.write("You chose Option A!")
elif option_2 == "Option B":
    st.write("You chose Option B!")
else:
    st.write("You chose Option C!")
