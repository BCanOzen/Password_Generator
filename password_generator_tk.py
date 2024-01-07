import tkinter as tk
import string
import random 
import pyperclip


def main():
    class password_types:
        characters = list(string.ascii_letters + string.digits +"!@#$%^&*()")
        characters_without_specials = list(string.ascii_letters + string.digits)

    def create_password():
        password = []
        try:
            if check_variable.get():
                for x in range(int(password_length_var.get())):
                    password.append(random.choice(password_types.characters))                
            else:
                for x in range(int(password_length_var.get())):
                    password.append(random.choice(password_types.characters_without_specials))
            created_password = "".join(password)
            password_text.delete(1.0, tk.END)
            password_text.insert(tk.END, created_password)
        except Exception as e:
            password_length_var.set("İnput Number")

    def copy_password():
        try:
            pyperclip.copy(password_text.get("1.0", tk.END))
        except Exception as e:
            password_length_var.set("No password to copy")


    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("300x300")
    root.configure(bg="green")
    root.resizable(width=False,height=False)


    password_text = tk.Text(root, width=30, height=5)
    password_text.pack(pady=10)

    password_length_var = tk.StringVar()
    password_length_entry = tk.Entry(root, textvariable=password_length_var)
    password_length_var.set("Input Password Length")
    password_length_entry.pack(pady=10)


    create_password_button = tk.Button(root, text="Create Password", command= create_password, bg="White")
    create_password_button.pack(pady=10)

    copy_password_button = tk.Button(root, text="Copy Password", command = copy_password, bg="White")
    copy_password_button.pack(pady=10)

    check_variable = tk.IntVar()
    special_password_checker = tk.Checkbutton(root, text="Special Char: !@#$%^&*()",variable=check_variable)
    special_password_checker.pack(pady=10)

    root.mainloop()
    
if __name__ == '__main__':
  main()