#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from datetime import date

def calculate_age():
    birthdate = entry_birthdate.get()
    try:
        birthdate = date(*map(int, birthdate.split('-')))
        today = date.today()
        age = today - birthdate

        years = age.days // 365
        remaining_days = age.days % 365
        months = remaining_days // 30
        days = remaining_days % 30

        result_text = f"Your age is {years} years, {months} months, and {days} days."
        label_result.config(text=result_text)
    except ValueError:
        label_result.config(text="Invalid date format. Use YYYY-MM-DD.")

# Create the main application window
root = tk.Tk()
root.title("Age Calculator")

# Create widgets
label_instructions = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):")
entry_birthdate = tk.Entry(root)
button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
label_result = tk.Label(root, text="")

# Place widgets on the window using grid layout
label_instructions.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entry_birthdate.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
button_calculate.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Start the Tkinter main loop
root.mainloop()


# In[ ]:




