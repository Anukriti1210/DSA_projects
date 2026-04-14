# Smart Trip Planner (C++ + Python)

Plan smarter, not harder.

This project helps you choose the best travel destinations within a limited budget using the Fractional Knapsack algorithm. It combines a fast C++ backend for computation with a simple Python Streamlit interface for interaction.

## How it works

Enter costs, values, and your budget. The system calculates the maximum possible enjoyment by optimally selecting (and even partially selecting) destinations.

## Tech Stack

* C++
* Python (Streamlit)

## Run

g++ knapsack.cpp -o knapsack
python -m streamlit run app.py

## Sample

Input: Budget = 50, Costs = [10, 20, 30], Values = [60, 100, 120]
Output: Max Enjoyment = 240.00

## Why this project

A practical demonstration of greedy algorithms, combined with real-world UI interaction.


