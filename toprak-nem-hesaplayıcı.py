import tkinter as tk


def calculate_soil_moisture():
    """Calculate gravimetric soil water content from wet and dry sample weights."""
    try:
        dry_weight = float(entry_dry.get())
        wet_weight = float(entry_wet.get())

        if dry_weight <= 0:
            result_label.config(text="Dry weight must be greater than zero.")
            return

        if wet_weight < dry_weight:
            result_label.config(text="Wet weight must be greater than or equal to dry weight.")
            return

        moisture_content = ((wet_weight - dry_weight) / dry_weight) * 100
        result_label.config(
            text=f"Gravimetric Water Content: {moisture_content:.2f}%"
        )

    except ValueError:
        result_label.config(text="Please enter valid numeric values.")


root = tk.Tk()
root.title("Soil Moisture Calculator")
root.resizable(False, False)

frame = tk.Frame(root, padx=16, pady=16)
frame.pack()

tk.Label(frame, text="Dry Weight (g):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_dry = tk.Entry(frame, width=18)
entry_dry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Wet Weight (g):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_wet = tk.Entry(frame, width=18)
entry_wet.grid(row=1, column=1, padx=5, pady=5)

calculate_button = tk.Button(frame, text="Calculate", command=calculate_soil_moisture)
calculate_button.grid(row=2, column=0, columnspan=2, pady=(8, 6))

result_label = tk.Label(frame, text="", wraplength=320)
result_label.grid(row=3, column=0, columnspan=2, pady=(4, 0))

root.mainloop()
