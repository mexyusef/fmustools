import customtkinter as ctk
import customtkinter as ctk
from customtkinter import CTkInputDialog
from tkinter import messagebox

# Create a persistent root window and hide it
root = ctk.CTk()
root.withdraw()

ctk.set_appearance_mode("Dark")  # Set the theme to dark mode
ctk.set_default_color_theme("blue")  # Set the color theme

def input_text_ctk(prompt):
    dialog = CTkInputDialog(title="Input", text=prompt)
    return dialog.get_input()

def input_integer_ctk(prompt):
    while True:
        dialog = CTkInputDialog(title="Input", text=prompt)
        result = dialog.get_input()
        try:
            return int(result)
        except (ValueError, TypeError):
            messagebox.showerror(title="Error", message="Please enter a valid integer.")

def input_float_ctk(prompt):
    while True:
        dialog = CTkInputDialog(title="Input", text=prompt)
        result = dialog.get_input()
        try:
            return float(result)
        except (ValueError, TypeError):
            messagebox.showerror(title="Error", message="Please enter a valid float.")

def input_boolean_ctk(prompt):
    return messagebox.askyesno(title="Confirm", message=prompt)

def test_tkinput():
    text = input_text_ctk("Enter some text:")
    print("You entered:", text)

    integer = input_integer_ctk("Enter an integer:")
    print("You entered:", integer)

    floating_point = input_float_ctk("Enter a float:")
    print("You entered:", floating_point)

    confirmation = input_boolean_ctk("Confirm?")
    print("You confirmed:", confirmation)
