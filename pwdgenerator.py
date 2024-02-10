import random
import string
import tkinter as Tk
from tkinter import ttk

class Passwordgen:
    def __init__(self, master):
        self.master = master
        self.master.title("PASSWORD GENERATOR")
        self.master.geometry("500x400")

        self.length_label = ttk.Label(self.master, text='Enter the length of the PASSWORD')
        self.length_label.grid(row=0, column=0, pady=10, padx=10, sticky='w')

        self.length_var = Tk.IntVar()
        self.length_entry = ttk.Entry(self.master, textvariable=self.length_var)
        self.length_entry.grid(row=0, column=1, pady=10, padx=10)

        self.uppercase_var = Tk.IntVar()
        self.uppercase_check = ttk.Checkbutton(self.master, text='Include Uppercase Letters?', variable=self.uppercase_var)
        self.uppercase_check.grid(row=1, column=0, pady=5, padx=10, sticky='w')

        self.lowercase_var = Tk.IntVar()
        self.lowercase_check = ttk.Checkbutton(self.master, text='Include Lowercase Letters?', variable=self.lowercase_var)
        self.lowercase_check.grid(row=2, column=0, pady=5, padx=10, sticky='w')

        self.digits_var = Tk.IntVar()
        self.digits_check = ttk.Checkbutton(self.master, text='Include Digits?', variable=self.digits_var)
        self.digits_check.grid(row=3, column=0, pady=5, padx=10, sticky='w')

        self.specialchar_var = Tk.IntVar()
        self.specialchar_check = ttk.Checkbutton(self.master, text='Include Special Characters?', variable=self.specialchar_var)
        self.specialchar_check.grid(row=4, column=0, pady=5, padx=10, sticky='w')

        self.generate_button = ttk.Button(self.master, text="Generate Password!", command=self.generate_password)
        self.generate_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.result_var = Tk.StringVar()
        self.result_label = ttk.Label(self.master, textvariable=self.result_var)
        self.result_label.grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        uppercase = string.ascii_uppercase if self.uppercase_var.get() else ""
        lowercase = string.ascii_lowercase if self.lowercase_var.get() else ""
        digits = string.digits if self.digits_var.get() else ""    
        special = string.punctuation if self.specialchar_var.get() else ""

        all_characters = uppercase + lowercase + digits + special

        if not all_characters:
            self.result_var.set("Please select atleast one of the above character")
            return
        password = ''.join(random.choice(all_characters) for _ in range(length))
        self.result_var.set(f"GENERATE PASSWORD: {password}")

if __name__ == "__main__":
    root = Tk.Tk()
    app = Passwordgen(root)
    root.mainloop()