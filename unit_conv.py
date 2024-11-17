import tkinter as tk
from tkinter import ttk

def convert():
    input_value = float(entry.get())
    unit_from = from_unit.get()
    unit_to = to_unit.get()

    conversion_factors = {
        "Celsius to Fahrenheit": lambda c: (c * 9/5) + 32,
        "Fahrenheit to Celsius": lambda f: (f - 32) * 5/9,
        "Kilograms to Pounds": lambda kg: kg * 2.20462,
        "Pounds to Kilograms": lambda lb: lb / 2.20462,
    }

    conversion_key = f"{unit_from} to {unit_to}"
    if conversion_key in conversion_factors:
        result = conversion_factors[conversion_key](input_value)
        result_label.config(text=f"Result: {result:.2f} {unit_to}")
    else:
        result_label.config(text="Conversion not available")

# GUI setup
root = tk.Tk()
root.title("Unit Converter")

tk.Label(root, text="Enter Value:").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

tk.Label(root, text="From:").grid(row=1, column=0)
from_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kilograms", "Pounds"])
from_unit.grid(row=1, column=1)

tk.Label(root, text="To:").grid(row=2, column=0)
to_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kilograms", "Pounds"])
to_unit.grid(row=2, column=1)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
