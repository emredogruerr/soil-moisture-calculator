import json
from logging import root
import os
import tkinter as tk 


print("Enter the dry and wet weights to calculate the soil moisture content.") 

def calculate_soil_moisture():
    try:
        weight_dry = float(entry_dry.get())
        weight_wet = float(entry_wet.get())
        if weight_wet <= weight_dry:
            result_label.config(text="Wet weight must be greater than dry weight.")
            return
        moisture_content = ((weight_wet - weight_dry) / weight_wet) * 100
        result_label.config(text=f"Soil Moisture Content: {moisture_content:.2f}%")
        # Display soil condition message
        if moisture_content < 10:
            print("Soil is very dry. Irrigation is recommended.")
        elif 10 <= moisture_content < 20:
            print("Soil is dry. Irrigation may be needed.")
        elif 20 <= moisture_content < 30:
            print("Soil is moist. No irrigation needed.")
        elif 30 <= moisture_content < 40:
            print("Soil is wet. No irrigation needed.")
        else:
            print("Soil is very wet. No irrigation needed.")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return


root = tk.Tk()
root.title("Soil Moisture Calculator")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_dry = tk.Label(frame, text="Dry Weight (g):")
label_dry.grid(row=0, column=0)
entry_dry = tk.Entry(frame)
entry_dry.grid(row=0, column=1)

label_wet = tk.Label(frame, text="Wet Weight (g):")
label_wet.grid(row=1, column=0)
entry_wet = tk.Entry(frame)
entry_wet.grid(row=1, column=1)

result_label = tk.Label(frame, text="")
result_label.grid(row=3, columnspan=2)

# Yeni: Durum mesajı için ek bir label
status_label = tk.Label(frame, text="")
status_label.grid(row=4, columnspan=2)

def calculate_soil_moisture():
    try:
        weight_dry = float(entry_dry.get())
        weight_wet = float(entry_wet.get())
        if weight_wet <= weight_dry:
            result_label.config(text="Wet weight must be greater than dry weight.")
            status_label.config(text="")
            return
        moisture_content = ((weight_wet - weight_dry) / weight_wet) * 100
        result_label.config(text=f"Soil Moisture Content: {moisture_content:.2f}%")
        # Display soil condition message in GUI
        if moisture_content < 10:
            status_label.config(text="Soil is very dry. Irrigation is recommended.")
        elif 10 <= moisture_content < 20:
            status_label.config(text="Soil is dry. Irrigation may be needed.")
        elif 20 <= moisture_content < 30:
            status_label.config(text="Soil is moist. No irrigation needed.")
        elif 30 <= moisture_content < 40:
            status_label.config(text="Soil is wet. No irrigation needed.")
        else:
            status_label.config(text="Soil is very wet. No irrigation needed.")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        status_label.config(text="")
        return

calculate_button = tk.Button(frame, text="Calculate", command=calculate_soil_moisture)
calculate_button.grid(row=2, columnspan=2)

root.mainloop()