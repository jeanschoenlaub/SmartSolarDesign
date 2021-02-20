import tkinter as tk
import tkinter.ttk as ttk

class AccountPage(tk.Toplevel):

    def __init__(self,  master = None):
        super().__init__(master = master)
        self.title("User settings")
        self.geometry("900x300+300+200")

        self.butt_quit_account = ttk.Button(self, text="Back to Main Menu",command=self.quit_account)

        self.show_layout()

    def show_layout(self,*args):

        self.butt_quit_account.grid(row=1,column=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)


    def quit_account(self,*args):
        self.destroy()
