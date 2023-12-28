import tkinter as tk
from tkinter import ttk

def calculate_loan():
    try:
        principal = float(principal_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100.0
        time_period = float(time_period_entry.get())

        # Formula to calculate monthly payment
        monthly_payment = (principal * interest_rate / 12) / (1 - (1 + interest_rate / 12) ** (-12 * time_period))

        result_label.config(text=f"Monthly Payment: ${monthly_payment:.2f}")
    except ValueError:
        result_label.config(text="Please enter valid numeric values.")

# Create the main window
window = tk.Tk()
window.title("Loan Calculator")

# Create and place widgets
principal_label = ttk.Label(window, text="Loan Amount:")
principal_label.grid(row=0, column=0, padx=10, pady=10)

principal_entry = ttk.Entry(window)
principal_entry.grid(row=0, column=1, padx=10, pady=10)




interest_rate_label = ttk.Label(window, text="Annual Interest Rate (%):")
interest_rate_label.grid(row=1, column=0, padx=10, pady=10)

interest_rate_entry = ttk.Entry(window)
interest_rate_entry.grid(row=1, column=1, padx=10, pady=10)

time_period_label = ttk.Label(window, text="Loan Term (years):")
time_period_label.grid(row=2, column=0, padx=10, pady=10)

time_period_entry = ttk.Entry(window)
time_period_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = ttk.Button(window, text="Calculate", command=calculate_loan)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
window.mainloop()
