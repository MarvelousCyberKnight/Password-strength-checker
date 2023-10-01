import re
import tkinter as tk
from termcolor import colored
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define global variable for background color
bg_color = "white"

def get_password_security_level(password):
    # Check if the password is at least 8 characters long
    length_ok = len(password) >= 8
    
    # Check if the password contains both uppercase and lowercase letters
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    
    # Check if the password contains at least one digit
    has_digit = any(c.isdigit() for c in password)
    
    # Check if the password contains at least one special character
    has_special_char = bool(re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]", password))
    
    # Calculate the security level
    if length_ok and has_lowercase and has_uppercase and has_digit and has_special_char:
        return "Strong"
    elif length_ok and (has_lowercase or has_uppercase) and has_digit:
        return "Moderate"
    else:
        return "Weak"

def check_password_strength():
    global bg_color  # Use the global background color variable
    password = password_entry.get()
    security_level = get_password_security_level(password)

    # Define colors based on security level
    if security_level == "Strong":
        color = "green"
    elif security_level == "Moderate":
        color = "yellow"
    else:
        color = "red"

    # Create a custom dialog box for displaying the password strength
    custom_dialog = tk.Toplevel()
    custom_dialog.title("Password Strength")
    
    # Calculate 1/3 of the screen size
    dialog_width = window.winfo_screenwidth() // 3
    dialog_height = window.winfo_screenheight() // 3
    
    custom_dialog.geometry(f"{dialog_width}x{dialog_height}")
    custom_dialog.configure(bg=color)

    # Display a message in the custom dialog
    message_label = tk.Label(custom_dialog, text=f"Password security level: {security_level}", fg="black", bg=color)
    message_label.pack(pady=10)

    if security_level == "Weak" or security_level == "Moderate":
        # Add a "Yes" button to generate a strong password
        yes_button = tk.Button(custom_dialog, text="Yes", command=generate_strong_password)
        yes_button.pack()

    # Set the background color to the current password strength color
    bg_color = color

def generate_strong_password():
    # Generate a strong password
    strong_password = get_random_bytes(8).hex()

    # Create a custom dialog box for displaying the strong password
    custom_dialog = tk.Toplevel()
    custom_dialog.title("Strong Password Generated")
    
    # Calculate 1/3 of the screen size
    dialog_width = window.winfo_screenwidth() // 3
    dialog_height = window.winfo_screenheight() // 3
    
    custom_dialog.geometry(f"{dialog_width}x{dialog_height}")
    custom_dialog.configure(bg="green")

    # Display the strong password in the custom dialog
    strong_password_label = tk.Label(custom_dialog, text=f"Generated strong password: {strong_password}", fg="black", bg="green")
    strong_password_label.pack()

# Create a Tkinter window
window = tk.Tk()
window.title("Password Strength Checker")

# Customize the window size (1/3 of the screen)
window_width = window.winfo_screenwidth() // 3
window_height = window.winfo_screenheight() // 3
window.geometry(f"{window_width}x{window_height}")

# Create a label with black text
label = tk.Label(window, text="Enter a password:", fg="black")
label.pack(pady=10)

# Create an entry field with white background
password_entry = tk.Entry(window, show="*", bg="white")
password_entry.pack(pady=5)

# Create a button to check password strength
check_button = tk.Button(window, text="Check Strength", command=check_password_strength)
check_button.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()
