import tkinter as tk
from tkinter import messagebox, Menu
from FrmDatamahasiswa import FormDatamahasiswa  # Ubah ini sesuai dengan nama file dan kelas

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("400x200")
        self.root.configure(background="Purple")
        self.background_label = tk.Label(root, text="Aplikasi Datamahasiwa", font=("Arial", 18, "bold"), bg="white", fg="black")
        self.background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.file_menu = Menu(root)
        self.file_menu.add_command(label='Login', command=self.log_in)
        self.file_menu.add_command(label='Exit', command=root.quit)

        self.menu_bar = Menu(root)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)

        root.config(menu=self.menu_bar)

    def log_in(self):
        self.root.withdraw()
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")
        login_window.geometry("300x150")

        self.username_label = tk.Label(login_window, text="Username:")
        self.username_entry = tk.Entry(login_window)

        self.password_label = tk.Label(login_window, text="Password:")
        self.password_entry = tk.Entry(login_window, show="*")

        self.login_button = tk.Button(login_window, text="Login", command=self.check_login)

        self.username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            messagebox.showinfo("Login Successful", "You are logged in!")
            self.open_application(username)
        else:
            messagebox.showerror("Login Failed", "Please enter username and password.")

    def open_application(self, username):
        self.root.deiconify()
        aplikasi_window = tk.Toplevel(self.root)
        aplikasi = FormDatamahasiswa(aplikasi_window, "Aplikasi Pengobatan")

if __name__ == "__main__":
    root = tk.Tk()
    dashboard = Dashboard(root)
    root.mainloop()
