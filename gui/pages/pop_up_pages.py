import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk

from gui.save_manager import save_user_pref
import databases.constants as constants

class ConfigBlockDiag(tk.Toplevel):

    def __init__(self,  master = None):
        super().__init__(master = master)
        self.title("Block diagram configuration")
        self.geometry("900x300+300+200")

        self.schema= tk.Canvas(self, width=1000, height=400, highlightthickness=0, bg=constants.set_baground_for_theme())

        #List of Entries
        self.ent_b1 = ttk.Entry(self.schema,width=9,style="my.TEntry")
        self.ent_l1a = ttk.Entry(self.schema,width=15,style="my.TEntry")
        self.ent_l1b = ttk.Entry(self.schema,width=15,style="my.TEntry")
        self.ent_b2 = ttk.Entry(self.schema,width=9,style="my.TEntry")
        self.ent_l2a = ttk.Entry(self.schema,width=15,style="my.TEntry")
        self.ent_l2b = ttk.Entry(self.schema,width=15,style="my.TEntry")
        self.ent_b3 = ttk.Entry(self.schema,width=9,style="my.TEntry")

        self.var_include = tk.IntVar()
        self.var_usr_pref = tk.IntVar()

    def show_layout(self,job_dict,user_pref):

        self.schema.grid(row=0,columnspan=4,sticky="nsew")

        #Square 1
        self.schema.create_line(100 ,100, 100, 200)
        self.schema.create_line(100 ,200, 200, 200)
        self.schema.create_line(100 ,100, 200, 100)
        self.schema.create_line(200 ,100, 200, 200)
        self.schema.create_window(150,150,window=self.ent_b1)
        self.schema.create_line(200,150,400,150)
        self.schema.create_window(300,130,window=self.ent_l1a)
        self.schema.create_window(300,170,window=self.ent_l1b)

        #Square 2
        self.schema.create_line(400 ,100, 400, 200)
        self.schema.create_line(400 ,200, 500, 200)
        self.schema.create_line(400 ,100, 500, 100)
        self.schema.create_line(500 ,100, 500, 200)
        self.schema.create_window(450,150,window=self.ent_b2)
        self.schema.create_line(500,150,700,150)
        self.schema.create_window(600,130,window=self.ent_l2a)
        self.schema.create_window(600,170,window=self.ent_l2b)

        #Square 3
        self.schema.create_line(700 ,100, 700, 200)
        self.schema.create_line(700 ,200, 800, 200)
        self.schema.create_line(700 ,100, 800, 100)
        self.schema.create_line(800 ,100, 800, 200)
        self.schema.create_window(750,150,window=self.ent_b3)


        #The rest
        self.lbl_title = ttk.Label(self.schema, text="Block Diagram Preview",font='Helvetica 14 bold')
        self.schema.create_window(450,30,window=self.lbl_title)

        self.lbl_note = ttk.Label(self.schema, text="Add a note:",font='Helvetica 14 bold')
        self.schema.create_window(100,240,window=self.lbl_note)
        self.ent_note = ttk.Entry(self.schema,width=50)
        self.schema.create_window(400,240,window=self.ent_note)

        self.check_block_diag= ttk.Checkbutton(self.schema, text="Include in the design",variable=self.var_include)
        self.schema.create_window(370,280,window= self.check_block_diag)
        self.check_save_pref= ttk.Checkbutton(self.schema, text="Save entries as Template",variable=self.var_usr_pref)
        self.schema.create_window(570,280,window= self.check_save_pref)

        #Creating the buttons
        self.butt_finish = ttk.Button(self.schema, text="   Finish   ", command=lambda: self.submit_bd(job_dict,user_pref))
        self.schema.create_window(800,280,window=self.butt_finish)
        self.butt_cancel = ttk.Button(self.schema, text="   Cancel   ", command=self.cancel_bd)
        self.schema.create_window(100,280,window=self.butt_cancel)
        self.butt_clear = ttk.Button(self.schema, text="   Clear   ", command=lambda: self.clear_bd(job_dict))
        self.schema.create_window(200,280,window=self.butt_clear)

        self.load_user_pref(user_pref)

    def load_user_pref(self,user_pref):
        self.ent_b1.insert(0,user_pref["blockDiagram"]["block1"])
        self.ent_l1a.insert(0,user_pref["blockDiagram"]["line1up"])
        self.ent_l1b.insert(0,user_pref["blockDiagram"]["line1down"])
        self.ent_b2.insert(0,user_pref["blockDiagram"]["block2"])
        self.ent_l2a.insert(0,user_pref["blockDiagram"]["line2up"])
        self.ent_l2b.insert(0,user_pref["blockDiagram"]["line2down"])
        self.ent_b3.insert(0,user_pref["blockDiagram"]["block3"])

    def submit_bd(self,job_dict,user_pref):
        if self.var_include.get() ==1:
            job_dict["blockDiagram"]={}
            job_dict["blockDiagram"]["block1"]=self.ent_b1.get()
            job_dict["blockDiagram"]["line1up"]=self.ent_l1a.get()
            job_dict["blockDiagram"]["line1down"]=self.ent_l1b.get()
            job_dict["blockDiagram"]["block2"]=self.ent_b2.get()
            job_dict["blockDiagram"]["line2up"]=self.ent_l2a.get()
            job_dict["blockDiagram"]["line2down"]=self.ent_l2b.get()
            job_dict["blockDiagram"]["block3"]=self.ent_b3.get()
            job_dict["blockDiagram"]["note"]=self.ent_note.get()

        if self.var_usr_pref.get()==1:
            user_pref["blockDiagram"]={}
            user_pref["blockDiagram"]["block1"]=self.ent_b1.get()
            user_pref["blockDiagram"]["line1up"]=self.ent_l1a.get()
            user_pref["blockDiagram"]["line1down"]=self.ent_l1b.get()
            user_pref["blockDiagram"]["block2"]=self.ent_b2.get()
            user_pref["blockDiagram"]["line2up"]=self.ent_l2a.get()
            user_pref["blockDiagram"]["line2down"]=self.ent_l2b.get()
            user_pref["blockDiagram"]["block3"]=self.ent_b3.get()
            user_pref["blockDiagram"]["note"]=self.ent_note.get()
            save_user_pref(user_pref)
        self.destroy()

    def cancel_bd(self,*args):
        self.destroy()

    def clear_bd(self,job_dict):
        del job_dict["blockDiagram"]
        self.destroy()

class ConfigVrise(tk.Toplevel):

    def __init__(self,  master = None):
        super().__init__(master = master)
        self.title("Voltage Rise configuration")
        self.geometry("550x400+300+200")
        self.configure(bg=constants.set_baground_for_theme())

        #List of Entries
        self.ent_col1_auto = ttk.Entry(self,width=25,style="my.TEntry")
        self.ent_col2_auto = ttk.Entry(self,width=25,style="my.TEntry")
        self.ent_col3_auto = ttk.Entry(self,width=25,style="my.TEntry")

    def show_layout(self,user_pref):

        print(user_pref)

        lbl_title1 = ttk.Label(self, text="                 Configuring Automatic Entries",font='Helvetica 14 bold').grid(row = 0,columnspan=4,pady=5)

        #3 first rows for configuring the automatic fills for Vrise
        lbl_col1 = ttk.Label(self, text="Column 1 Auto-entry:").grid(row = 1,column=0)
        self.ent_col1_auto.grid(row=1,column=1, sticky="e")
        lbl_col2= ttk.Label(self, text="Column 2 Auto-entry:").grid(row = 2,column=0)
        self.ent_col2_auto.grid(row=2,column=1, sticky="e")
        lbl_col3 = ttk.Label(self, text="Column 3 Auto-entry:").grid(row = 3,column=0)
        self.ent_col3_auto.grid(row=3,column=1, sticky="e")

        lbl_title1 = ttk.Label(self, text="                 Configuring Automatic Entries",font='Helvetica 14 bold').grid(row = 4,columnspan=4,pady=5)

        #Then this will be where you can select the wire type (ANSZ )

        lbl_note = ttk.Label(self, text="Note: To apply the changes, you will need to reload the page (use Previous/Next)",font='Helvetica 12 italic').grid(row = 9,columnspan=4,pady=5)
        #Creating the buttons
        self.butt_finish = ttk.Button(self, text="   Finish   ", command=lambda: self.submit_vr(user_pref))
        self.butt_finish.grid(row=10,column=4,sticky="e",padx=10,pady=5)
        self.butt_cancel = ttk.Button(self, text="   Cancel   ", command=self.cancel_vr)
        self.butt_cancel.grid(row=10,column=0,sticky="w",padx=10,pady=5)

        self.fill_vr(user_pref)#Fills the entries created with the stored values in user_pref dict

    def fill_vr(self,user_pref):

        self.ent_col1_auto.insert(0, user_pref["Vrise_pref"]["col1_name"])
        self.ent_col2_auto.insert(0, user_pref["Vrise_pref"]["col2_name"])
        self.ent_col3_auto.insert(0, user_pref["Vrise_pref"]["col3_name"])

    def submit_vr(self,user_pref):

        user_pref["Vrise_pref"]["col1_name"]= self.ent_col1_auto.get()
        user_pref["Vrise_pref"]["col2_name"]= self.ent_col2_auto.get()
        user_pref["Vrise_pref"]["col3_name"]= self.ent_col3_auto.get()
        save_user_pref(user_pref)
        self.destroy()

    def cancel_vr(self,*args):
        self.destroy()
