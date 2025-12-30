import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        total = num1 + num2
        result_label.config(text=f"{num1} + {num2} = {total}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

# Create window
window = tk.Tk()
window.title("Sum Calculator")

# Input 1
entry1 = tk.Entry(window)
entry1.pack(pady=5)

# Input 2
entry2 = tk.Entry(window)
entry2.pack(pady=5)

# Button
button = tk.Button(window, text="Add", command=calculate)
button.pack(pady=5)

# Result label
result_label = tk.Label(window, text="")
result_label.pack(pady=5)

# Start the app
window.mainloop()
