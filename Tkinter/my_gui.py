import tkinter as tk

# Dummy user data (replace with your own logic)
user = {'pin': 1234, 'name': 'Mr. Prateek Agarwal', 'balance': 3000}

# Function to handle the login button click
def login():
    entered_pin = entry_pin.get()
    if int(entered_pin) == user['pin']:
        label_message.config(text=f"Welcome, {user['name']}!")
        show_menu()
    else:
        label_message.config(text="Invalid PIN. Please try again.")

# Function to display the menu
def show_menu():
    entry_pin.pack_forget()
    button_login.pack_forget()
    label_message.pack()
    button_withdraw.pack()
    button_deposit.pack()
    button_exit.pack()

# Function to handle the withdraw button click
def withdraw():
    amount = int(entry_amount.get())
    if amount > user['balance']:
        label_message.config(text="Your account balance is too low! Please enter a lower amount.")
    else:
        user['balance'] -= amount
        label_message.config(text=f"Withdrew {amount} Rupees. Your remaining balance is {user['balance']} Rupees.")

# Function to handle the deposit button click
def deposit():
    amount = int(entry_amount.get())
    user['balance'] += amount
    label_message.config(text=f"Deposited {amount} Rupees. Your remaining balance is {user['balance']} Rupees.")

# Function to handle the exit button click
def exit_app():
    app.quit()

# Create the main application window
app = tk.Tk()
app.title("Python ATM")

# Create a label for PIN input
label_pin = tk.Label(app, text="Enter your PIN:")
label_pin.pack()

# Create an entry widget for PIN input
entry_pin = tk.Entry(app, show="*")
entry_pin.pack()

# Create a login button
button_login = tk.Button(app, text="Login", command=login)
button_login.pack()

# Create a label for displaying messages
label_message = tk.Label(app, text="")
label_message.pack()

# Create buttons for withdraw and deposit
button_withdraw = tk.Button(app, text="Withdraw", command=withdraw)
button_deposit = tk.Button(app, text="Deposit", command=deposit)

# Entry widget for amount input
entry_amount = tk.Entry(app)
entry_amount.pack()

# Create an exit button
button_exit = tk.Button(app, text="Exit", command=exit_app)

# Run the main event loop
app.mainloop()
