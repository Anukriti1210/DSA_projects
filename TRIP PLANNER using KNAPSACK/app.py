import streamlit as st
import subprocess

st.set_page_config(page_title="Trip Planner")

st.title("Smart Trip Planner")

# Input
n = st.number_input("Number of places", 1, 5, 3)

costs = []
values = []

for i in range(n):
    col1, col2 = st.columns(2)
    with col1:
        cost = st.number_input(f"Cost {i+1}", min_value=0, key=f"c{i}")
    with col2:
        value = st.number_input(f"Value {i+1}", min_value=0, key=f"v{i}")

    costs.append(cost)
    values.append(value)

budget = st.number_input("Budget", min_value=0)

# Button
if st.button("Optimize"):
    # Prepare input for C++
    input_data = str(n) + "\n"
    for i in range(n):
        input_data += f"{int(costs[i])} {int(values[i])}\n"
    input_data += str(int(budget)) + "\n"

    # Run C++ program
    result = subprocess.run(
        ["./knapsack.exe"],   # IMPORTANT
        input=input_data,
        text=True,
        capture_output=True
    )

    output = result.stdout.strip()

    # Debug (optional)
    # st.write("DEBUG:", output)
    # st.write("ERROR:", result.stderr)

    if output:
        st.success(f"Max Enjoyment: {float(output):.2f}")
    else:
        st.error("Error: No output from C++ program")
