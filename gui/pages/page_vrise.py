import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import math

import databases.vrise_dictionnaries as vrise_dictionnaries
import databases.constants as constants

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, **kwargs,bg=constants.set_baground_for_theme())


class PageVrise(Page):

   def __init__(self, *args, **kwargs):

       Page.__init__(self, *args, **kwargs)

       #List of entries
       self.ent_col1_name = ttk.Entry(self, width=13,justify='center',style="my.TEntry")
       self.ent_col2_name = ttk.Entry(self, width=13,justify='center',style="my.TEntry")
       self.ent_col3_name = ttk.Entry(self, width=13,justify='center',style="my.TEntry")
       self.ent_new_phase_inv_1 = ttk.Entry(self, width=2,style="my.TEntry")
       self.ent_new_phase_inv_2 = ttk.Entry(self, width=2,style="my.TEntry")
       self.ent_new_phase_inv_3 = ttk.Entry(self, width=2,style="my.TEntry")
       self.ent_new_imax_phase1 = ttk.Entry(self, width=4,style="my.TEntry")
       self.ent_new_imax_phase2= ttk.Entry(self, width=4,style="my.TEntry")
       self.ent_new_imax_phase3 = ttk.Entry(self, width=4,style="my.TEntry")
       self.ent_serv_len = ttk.Entry(self, width=3,style="my.TEntry")
       self.ent_cons_len = ttk.Entry(self, width=3,style="my.TEntry")
       self.ent_msb_len = ttk.Entry(self, width=3,style="my.TEntry")


       self.combobox_msb_wire_size = ttk.Combobox(self, values="",justify='center', state='readonly',width=3)
       self.combobox_cons_wire_size = ttk.Combobox(self, values="",justify='center', state='readonly',width=3)
       self.combobox_serv_wire_size = ttk.Combobox(self, values="",justify='center', state='readonly',width=3)
       self.combobox_msb_wire_type = ttk.Combobox(self, values="",justify='center', state='readonly',width=10)
       self.combobox_cons_wire_type = ttk.Combobox(self, values="",justify='center', state='readonly',width=10)
       self.combobox_serv_wire_type = ttk.Combobox(self, values="",justify='center',state='readonly',width=10)
       self.ent_notes =  ttk.Entry(self, width= 50,style="my.TEntry")

       self.locked_image =  tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/button_images/Lock.png")
       self.unlocked_image = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/button_images/Unlock.png")
       self.butt_lock_names = ttk.Button(self, image=self.locked_image, command=self.lock_names,style='my.TButton',width=1)
       self.var_lock_name = 0
       self.butt_lock_inv_phase = ttk.Button(self, image=self.locked_image, command=self.lock_inv_phases,style='my.TButton',width=1)
       self.var_lock_inv_phases = 0
       self.butt_lock_wire_type = ttk.Button(self, image=self.locked_image, command=self.lock_wire_type,style='my.TButton',width=1)
       self.var_lock_wire_type = 0
       self.butt_lock_imax_phase = ttk.Button(self, image=self.locked_image, command=self.lock_imax_phase,style='my.TButton',width=1)
       self.var_lock_imax_phase = 0
       self.butt_calculate = ttk.Button(self, text="   Calculate   ", command=self.calculate_Vrise)
       #Used to set text color for ttk labels - ! Formating is weird ('mRed.TLabel' - here I think TLabel is necessary)
       self.mRed = ttk.Style()
       self.mRed.configure('mRed.TLabel', foreground="red")
       self.mGreen = ttk.Style()
       self.mGreen.configure('mGreen.TLabel', foreground="green")

       self.pack()

   def show_entries(self,job_dict,user_pref,inv_dict):
       self.job_dict = job_dict
       self.user_pref = user_pref
       self.inv_dict = inv_dict

       lbl_title1 = ttk.Label(self, text="          Voltage Rise Calculations (AC Side)",font='Helvetica 14 bold').grid(row = 0,columnspan=4,pady=20)
       lbl_empty_space=ttk.Label(self, text="",font='Helvetica 14 bold').grid(row = 1,column=1,pady=constants.SPACING_FROM_TITLE_PGVRISE,padx = constants.COLUMN_PAD_X_TABLE)
       lbl_empty_space=ttk.Label(self, text="",font='Helvetica 14 bold').grid(row = 1,column=2,pady=constants.SPACING_FROM_TITLE_PGVRISE,padx = constants.COLUMN_PAD_X_TABLE)
       lbl_empty_space=ttk.Label(self, text="",font='Helvetica 14 bold').grid(row = 1,column=3,pady=constants.SPACING_FROM_TITLE_PGVRISE,padx = constants.COLUMN_PAD_X_TABLE)

       #1st line
       self.butt_lock_names.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=4)
       if self.var_lock_name == 0:#Condition so it only happens once (nad not when prev/next is hit)
           self.lock_names()
       #2nd line
       lbl_phases = ttk.Label(self, text="Inv phases:").grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=0, sticky="e")
       self.butt_lock_inv_phase.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=4)
       if self.var_lock_inv_phases == 0:#Condition so it only happens once (nad not when prev/next is hit)
           self.lock_inv_phases()
       #3rd line
       lbl_cond1 = ttk.Label(self, text="Conductor:").grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=0,pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE, sticky="e")
       self.butt_lock_wire_type.grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=4)
       if self.var_lock_wire_type == 0:#Condition so it only happens once (nad not when prev/next is hit)
           self.lock_wire_type()
       #4th line
       lbl_imax = ttk.Label(self, text="Imax/phase:").grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       self.butt_lock_imax_phase.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=4)
       if self.var_lock_imax_phase == 0:#Condition so it only happens once (nad not when prev/next is hit)
           self.lock_imax_phase()

       #4th line
       lbl_size = ttk.Label(self, text="     Size [mm^2]:").grid(row=constants.ROW_SIZE_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       self.combobox_serv_wire_size['values']=list(vrise_dictionnaries.AmPercent_dict.keys())
       self.combobox_serv_wire_size.bind("<<ComboboxSelected>>", self.link_serv_wire_ccc)
       self.combobox_serv_wire_size.current(4)# 16 mm2
       self.combobox_serv_wire_size.grid(row=constants.ROW_SIZE_ENT_PGVRISE, column=1)
       self.combobox_cons_wire_size['values']=list(vrise_dictionnaries.AmPercent_dict.keys())
       self.combobox_cons_wire_size.bind("<<ComboboxSelected>>", self.link_cons_wire_ccc)
       self.combobox_cons_wire_size.current(4)# 16 mm2
       self.combobox_cons_wire_size.grid(row=constants.ROW_SIZE_ENT_PGVRISE, column=2)
       self.combobox_msb_wire_size['values']=list(vrise_dictionnaries.AmPercent_dict.keys())
       self.combobox_msb_wire_size.bind("<<ComboboxSelected>>", self.link_msb_wire_ccc)
       self.combobox_msb_wire_size.current(1)# 4 mm2
       self.combobox_msb_wire_size.grid(row=constants.ROW_SIZE_ENT_PGVRISE, column=3)

       #5th line
       lbl_ccc = ttk.Label(self, text="C.C.C:").grid(row=constants.ROW_CCC_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)



       #6th line
       lbl_len1 = ttk.Label(self, text="Lenght [m]:").grid(row=constants.ROW_LENGHT_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       self.ent_serv_len.grid(row=constants.ROW_LENGHT_ENT_PGVRISE, column=1,pady=2)
       self.ent_cons_len.grid(row=constants.ROW_LENGHT_ENT_PGVRISE, column=2)
       self.ent_msb_len.grid(row=constants.ROW_LENGHT_ENT_PGVRISE, column=3)

       #Calculation part (the rest is in calculate_Vrise)
       lbl_imax = ttk.Label(self, text="Am/%Vd :").grid(row=constants.ROW_AM_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       lbl_Vdrop_prct = ttk.Label(self, text="Vdrop % :").grid(row=constants.ROW_VDROP_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       lbl_Vdrop_prct_tot = ttk.Label(self, text="Total %:").grid(row=constants.ROW_TOTAL_PRC_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       self.butt_calculate.grid(row=constants.ROW_CALC_BUTT_PGVRISE,columnspan=4,pady=20)

       #Notes part
       lbl_notes = ttk.Label(self, text="Vrise Notes:").grid(row=constants.ROW_NOTES_ENT_PGVRISE, column=0, sticky="e",pady=10)
       self.ent_notes.grid(row=constants.ROW_NOTES_ENT_PGVRISE,column = 1,columnspan=3,pady=10)

   def calculate_Vrise(self):
       Am1 = vrise_dictionnaries.AmPercent_dict[self.combobox_serv_wire_size.get()][self.new_phase_inv_1]
       Am2 = vrise_dictionnaries.AmPercent_dict[self.combobox_cons_wire_size.get()][self.new_phase_inv_2]
       Am3 = vrise_dictionnaries.AmPercent_dict[self.combobox_msb_wire_size.get()][self.new_phase_inv_3]

       constants.set_entries_background_for_darkmode()

       lbl_l7_left = ttk.Label(self, text=Am1)
       lbl_l7_left.grid(row=constants.ROW_AM_ENT_PGVRISE, column=1)
       lbl_l7_mid = ttk.Label(self, text=Am2)
       lbl_l7_mid.grid(row=constants.ROW_AM_ENT_PGVRISE, column=2)
       lbl_l7_right = ttk.Label(self, text=Am3)
       lbl_l7_right.grid(row=constants.ROW_AM_ENT_PGVRISE, column=3)

       Vdp1 = "{:.2f}".format(int(self.ent_serv_len.get())*float(self.ent_imax_serv.get())/int(Am1))
       Vdp2 = "{:.2f}".format(int(self.ent_cons_len.get())*float(self.ent_imax_cons.get())/int(Am2))
       Vdp3 = "{:.2f}".format(float(self.ent_msb_len.get())*float(self.ent_imax_msb.get())/int(Am3))

       #Coloring text in red/green if over/under limits
       if float(Vdp1)<1:
           lbl_l8_left = ttk.Label(self, style="mGreen.TLabel", text=Vdp1)
       elif float(Vdp1)>1:
           lbl_l8_left = ttk.Label(self, style="mRed.TLabel", text=Vdp1)
       lbl_l8_left.grid(row=constants.ROW_VDROP_ENT_PGVRISE, column=1)
       if float(Vdp2)<1:
           lbl_l8_mid = ttk.Label(self,style="mGreen.TLabel", text=Vdp2)
       elif float(Vdp2)>1:
           lbl_l8_mid = ttk.Label(self, style="mRed.TLabel", text=Vdp2)
       lbl_l8_mid.grid(row=constants.ROW_VDROP_ENT_PGVRISE, column=2)
       if float(Vdp3)<1:
           lbl_l8_right = ttk.Label(self, style="mGreen.TLabel", text=Vdp3)
       elif float(Vdp3)>1:
           lbl_l8_right = ttk.Label(self, style="mRed.TLabel", text=Vdp3)
       lbl_l8_right.grid(row=constants.ROW_VDROP_ENT_PGVRISE, column=3)
       Vdptot = "{:.2f}".format(float(Vdp1)+float(Vdp2)+float(Vdp3))
       if float(Vdptot)<3:
           lbl_l9_mid = ttk.Label(self, style="mGreen.TLabel", text=Vdptot)
       elif float(Vdptot)>3:
           lbl_l9_mid = ttk.Label(self, style="mRed.TLabel", text=Vdptot)
       lbl_l9_mid.grid(row=constants.ROW_TOTAL_PRC_ENT_PGVRISE, column=2)

       try:
           ccc_serv = vrise_dictionnaries.ccc_dict[self.new_phase_inv_1]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_serv_wire_size.get()]
           ccc_cons = vrise_dictionnaries.ccc_dict[self.new_phase_inv_2]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_cons_wire_size.get()]
           ccc_msb = vrise_dictionnaries.ccc_dict[self.new_phase_inv_3]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_msb_wire_size.get()]
           lbl_ccc2 = ttk.Label(self, text=ccc_serv).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=1,pady=2)
           lbl_ccc3 = ttk.Label(self, text=ccc_cons).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=2)
           lbl_ccc4 = ttk.Label(self, text=ccc_msb).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=3)
       except:
           tk.messagebox.showinfo(parent=self,title="Error - CCC not supported",message = "Sorry the Current Carrying Capacity for the cable selected is not supported yet", icon="warning")

   def lock_names(self,*args):
       if self.var_lock_name == 0:#Only happens once on instance
            self.var_lock_name=1
            if self.job_dict["jobVrise"]["col1Name"] != "": #If it is a saved job
                self.new_name1 = self.job_dict["jobVrise"]["col1Name"]
                self.new_name2 = self.job_dict["jobVrise"]["col2Name"]
                self.new_name3 = self.job_dict["jobVrise"]["col3Name"]
            else: #If not fill in the user preferred naming
                self.new_name1 = self.user_pref["Vrise_pref"]["col1_name"]
                self.new_name2 = self.user_pref["Vrise_pref"]["col2_name"]
                self.new_name3 = self.user_pref["Vrise_pref"]["col3_name"]
            self.lbl_col1_name = ttk.Label(self, text=self.new_name1,font='Helvetica 12 bold')
            self.lbl_col2_name = ttk.Label(self, text=self.new_name2,font='Helvetica 12 bold')
            self.lbl_col3_name = ttk.Label(self, text=self.new_name3,font='Helvetica 12 bold')
            self.lbl_col1_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=1)
            self.lbl_col2_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=2)
            self.lbl_col3_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=3)
       elif self.var_lock_name == 1:
            self.var_lock_name=2
            self.butt_lock_names.configure(image=self.unlocked_image)
            self.lbl_col1_name.grid_forget()
            self.lbl_col2_name.grid_forget()
            self.lbl_col3_name.grid_forget()
            self.ent_col1_name.delete(0, 'end')
            self.ent_col1_name.insert(0,self.new_name1)
            self.ent_col2_name.delete(0, 'end')
            self.ent_col2_name.insert(0,self.new_name2)
            self.ent_col3_name.delete(0, 'end')
            self.ent_col3_name.insert(0,self.new_name3)
            self.ent_col1_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=1)
            self.ent_col2_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=2)
            self.ent_col3_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=3)
       elif self.var_lock_name == 2:
            self.var_lock_name=1
            self.butt_lock_names.configure(image=self.locked_image)
            self.new_name1 = self.ent_col1_name.get()
            self.new_name2 = self.ent_col2_name.get()
            self.new_name3 = self.ent_col3_name.get()
            self.ent_col1_name.grid_forget()
            self.ent_col2_name.grid_forget()
            self.ent_col3_name.grid_forget()
            self.lbl_col1_name = ttk.Label(self, text=self.new_name1,font='Helvetica 12 bold')
            self.lbl_col1_name.grid(row = constants.ROW_NAME_ENT_PGVRISE,column=1)
            self.lbl_col2_name = ttk.Label(self, text=self.new_name2,font='Helvetica 12 bold')
            self.lbl_col2_name.grid(row = constants.ROW_NAME_ENT_PGVRISE,column=2)
            self.lbl_col3_name = ttk.Label(self, text=self.new_name3,font='Helvetica 12 bold')
            self.lbl_col3_name.grid(row = constants.ROW_NAME_ENT_PGVRISE,column=3)
       self.butt_lock_names.configure(takefocus=False)


   def lock_inv_phases(self,*args):
       inv_type = self.job_dict["jobComponents"]["invType"]
       inv_manu = self.job_dict["jobComponents"]["invManufacturer"]
       inv_model = self.job_dict["jobComponents"]["invModel"]
       if self.var_lock_inv_phases == 0:#Only happens once on instance
            self.var_lock_inv_phases=1
            self.new_phase_inv_1 = self.inv_dict[inv_type][inv_manu][inv_model]["Phases"]
            self.new_phase_inv_2 = self.inv_dict[inv_type][inv_manu][inv_model]["Phases"]
            self.new_phase_inv_3 = self.inv_dict[inv_type][inv_manu][inv_model]["Phases"]
            self.lbl_new_phase_inv_1 = ttk.Label(self, text=self.new_phase_inv_1,font='Helvetica 12')
            self.lbl_new_phase_inv_2 = ttk.Label(self, text=self.new_phase_inv_2,font='Helvetica 12')
            self.lbl_new_phase_inv_3 = ttk.Label(self, text=self.new_phase_inv_3,font='Helvetica 12')
            self.lbl_new_phase_inv_1.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=1)
            self.lbl_new_phase_inv_2.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=2)
            self.lbl_new_phase_inv_3.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=3)
       elif self.var_lock_inv_phases == 1:
            self.var_lock_inv_phases=2
            self.butt_lock_inv_phase.configure(image=self.unlocked_image)
            self.lbl_new_phase_inv_1.grid_forget()
            self.lbl_new_phase_inv_2.grid_forget()
            self.lbl_new_phase_inv_3.grid_forget()
            self.ent_new_phase_inv_1.delete(0, 'end')
            self.ent_new_phase_inv_1.insert(0,self.new_phase_inv_1)
            self.ent_new_phase_inv_2.delete(0, 'end')
            self.ent_new_phase_inv_2.insert(0,self.new_phase_inv_2)
            self.ent_new_phase_inv_3.delete(0, 'end')
            self.ent_new_phase_inv_3.insert(0,self.new_phase_inv_3)
            self.ent_new_phase_inv_1.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=1)
            self.ent_new_phase_inv_2.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=2)
            self.ent_new_phase_inv_3.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=3)
       elif self.var_lock_inv_phases == 2:
            self.var_lock_inv_phases=1
            self.butt_lock_inv_phase.configure(image=self.locked_image)
            self.new_phase_inv_1 = self.ent_new_phase_inv_1.get()
            self.new_phase_inv_2 = self.ent_new_phase_inv_2.get()
            self.new_phase_inv_3 = self.ent_new_phase_inv_3.get()
            self.ent_new_phase_inv_1.grid_forget()
            self.ent_new_phase_inv_2.grid_forget()
            self.ent_new_phase_inv_3.grid_forget()
            self.lbl_new_phase_inv_1 = ttk.Label(self, text=self.new_phase_inv_1,font='Helvetica 12')
            self.lbl_new_phase_inv_1.grid(row = constants.ROW_PHASE_ENT_PGVRISE,column=1)
            self.lbl_new_phase_inv_2 = ttk.Label(self, text=self.new_phase_inv_2,font='Helvetica 12')
            self.lbl_new_phase_inv_2.grid(row = constants.ROW_PHASE_ENT_PGVRISE,column=2)
            self.lbl_new_phase_inv_3 = ttk.Label(self, text=self.new_phase_inv_3,font='Helvetica 12')
            self.lbl_new_phase_inv_3.grid(row = constants.ROW_PHASE_ENT_PGVRISE,column=3)
       self.butt_lock_inv_phase.configure(takefocus=False)

   def lock_imax_phase(self,*args):
       inv_type = self.job_dict["jobComponents"]["invType"]
       inv_manu = self.job_dict["jobComponents"]["invManufacturer"]
       inv_model = self.job_dict["jobComponents"]["invModel"]

       if self.var_lock_imax_phase == 0:#Only happens once on instance
            print("A")
            self.var_lock_imax_phase=1
            if inv_type != "Micro":
                self.new_imax_phase1 = self.inv_dict[inv_type][inv_manu][inv_model]["IOutMax"]
                self.new_imax_phase2 = self.inv_dict[inv_type][inv_manu][inv_model]["IOutMax"]
                self.new_imax_phase3 = self.inv_dict[inv_type][inv_manu][inv_model]["IOutMax"]
            else:
                self.new_imax_phase1 = self.job_dict["jobVrise"]["maxCurrent"]
                self.new_imax_phase2 = self.job_dict["jobVrise"]["maxCurrent"]
                self.new_imax_phase3 = self.job_dict["jobVrise"]["maxCurrent"]
            self.lbl_new_imax_phase1 = ttk.Label(self, text=self.new_imax_phase1,font='Helvetica 12')
            self.lbl_new_imax_phase2 = ttk.Label(self, text=self.new_imax_phase2,font='Helvetica 12')
            self.lbl_new_imax_phase3 = ttk.Label(self, text=self.new_imax_phase3,font='Helvetica 12')
            self.lbl_new_imax_phase1.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=1)
            self.lbl_new_imax_phase2.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=2)
            self.lbl_new_imax_phase3.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=3)

       elif self.var_lock_imax_phase == 1:
            self.var_lock_imax_phase=2
            self.butt_lock_inv_phase.configure(image=self.unlocked_image)
            self.lbl_new_imax_phase1.grid_forget()
            self.lbl_new_imax_phase2.grid_forget()
            self.lbl_new_imax_phase3.grid_forget()
            self.ent_new_imax_phase1.delete(0, 'end')
            self.ent_new_imax_phase1.insert(0,self.new_imax_phase1)
            self.ent_new_imax_phase2.delete(0, 'end')
            self.ent_new_imax_phase2.insert(0,self.new_imax_phase2)
            self.ent_new_imax_phase3.delete(0, 'end')
            self.ent_new_imax_phase3.insert(0,self.new_imax_phase3)
            self.ent_new_imax_phase1.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=1)
            self.ent_new_imax_phase2.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=2)
            self.ent_new_imax_phase3.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=3)
       elif self.var_lock_imax_phase == 2:
            self.var_lock_imax_phase=1
            self.butt_lock_inv_phase.configure(image=self.locked_image)
            self.new_imax_phase1 = self.ent_new_imax_phase1.get()
            self.new_imax_phase2 = self.ent_new_imax_phase2.get()
            self.new_imax_phase3 = self.ent_new_imax_phase3.get()
            self.ent_new_imax_phase1.grid_forget()
            self.ent_new_imax_phase2.grid_forget()
            self.ent_new_imax_phase3.grid_forget()
            self.lbl_new_imax_phase1 = ttk.Label(self, text=self.new_imax_phase1,font='Helvetica 12')
            self.lbl_new_imax_phase1.grid(row = constants.ROW_IMAX_ENT_PGVRISE,column=1)
            self.lbl_new_imax_phase2 = ttk.Label(self, text=self.new_imax_phase2,font='Helvetica 12')
            self.lbl_new_imax_phase2.grid(row = constants.ROW_IMAX_ENT_PGVRISE,column=2)
            self.lbl_new_imax_phase3 = ttk.Label(self, text=self.new_imax_phase3,font='Helvetica 12')
            self.lbl_new_imax_phase3.grid(row = constants.ROW_IMAX_ENT_PGVRISE,column=3)
       self.butt_lock_inv_phase.configure(takefocus=False)

   def lock_wire_type(self,*args):
       if self.var_lock_wire_type == 0:#Only happens once on instance
            self.var_lock_wire_type=1
            self.new_wire_type_1 = vrise_dictionnaries.cable_type_dict["Copper"]
            self.new_wire_type_2 = vrise_dictionnaries.cable_type_dict["Copper"]
            self.new_wire_type_3 = vrise_dictionnaries.cable_type_dict["Copper"]
            self.lbl_new_wire_type_1 = ttk.Label(self, text=self.new_wire_type_1,font='Helvetica 12')
            self.lbl_new_wire_type_2 = ttk.Label(self, text=self.new_wire_type_2,font='Helvetica 12')
            self.lbl_new_wire_type_3 = ttk.Label(self, text=self.new_wire_type_3,font='Helvetica 12')
            self.lbl_new_wire_type_1.grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=1)
            self.lbl_new_wire_type_2.grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=2)
            self.lbl_new_wire_type_3.grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=3)
       elif self.var_lock_wire_type == 1:
            self.var_lock_wire_type=2
            self.butt_lock_wire_type.configure(image=self.unlocked_image)
            self.lbl_new_wire_type_1.grid_forget()
            self.lbl_new_wire_type_2.grid_forget()
            self.lbl_new_wire_type_3.grid_forget()
            self.combobox_serv_wire_type['values']=list(vrise_dictionnaries.cable_type_dict.keys())
            self.combobox_serv_wire_type.set(self.new_wire_type_1)
            self.combobox_serv_wire_type.grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=1)
            self.combobox_cons_wire_type['values']=list(vrise_dictionnaries.cable_type_dict.keys())
            self.combobox_cons_wire_type.set(self.new_wire_type_2)
            self.combobox_cons_wire_type.grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=2)
            self.combobox_msb_wire_type['values']=list(vrise_dictionnaries.cable_type_dict.keys())
            self.combobox_msb_wire_type.set(self.new_wire_type_3)
            self.combobox_msb_wire_type.grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=3)
       elif self.var_lock_wire_type == 2:
            self.var_lock_wire_type=1
            self.butt_lock_wire_type.configure(image=self.locked_image)
            self.new_wire_type_1 = self.combobox_serv_wire_type.get()
            self.new_wire_type_2 = self.combobox_cons_wire_type.get()
            self.new_wire_type_3 = self.combobox_msb_wire_type.get()
            self.combobox_serv_wire_type.grid_forget()
            self.combobox_cons_wire_type.grid_forget()
            self.combobox_msb_wire_type.grid_forget()
            self.lbl_new_wire_type_1 = ttk.Label(self, text=self.new_wire_type_1,font='Helvetica 12')
            self.lbl_new_wire_type_1.grid(row = constants.ROW_CONDUCTOR_ENT_PGVRISE,column=1)
            self.lbl_new_wire_type_2 = ttk.Label(self, text=self.new_wire_type_2,font='Helvetica 12')
            self.lbl_new_wire_type_2.grid(row = constants.ROW_CONDUCTOR_ENT_PGVRISE,column=2)
            self.lbl_new_wire_type_3 = ttk.Label(self, text=self.new_wire_type_3,font='Helvetica 12')
            self.lbl_new_wire_type_3.grid(row = constants.ROW_CONDUCTOR_ENT_PGVRISE,column=3)
       self.butt_lock_wire_type.configure(takefocus=False)

   def submit_Vrise(self,job_dict):
       if self.var_lock_name == 2 or self.var_lock_wire_type == 2 or self.var_lock_inv_phases == 2 or self.var_lock_imax_phase == 2:
           tk.messagebox.showinfo(parent=self,title="Error",message = "Please lock all modifications before going to next page", icon="warning")
           return False
       else:
           job_dict["jobVrise"]["col1Name"] = self.new_name1 # The way this is designed doesn't save if the locked
           job_dict["jobVrise"]["col2Name"] = self.new_name2
           job_dict["jobVrise"]["col3Name"] = self.new_name3
           job_dict["jobVrise"]["phasesService"] = self.new_phase_inv_1
           job_dict["jobVrise"]["phasesConsumer"] = self.new_phase_inv_2
           job_dict["jobVrise"]["phasesMsb"] = self.new_phase_inv_3
           job_dict["jobVrise"]["lenConsumer"] = self.ent_cons_len.get()
           job_dict["jobVrise"]["lenService"] = self.ent_serv_len.get()
           job_dict["jobVrise"]["lenMsb"]= self.ent_msb_len.get()
           job_dict["jobVrise"]["cableSize"] = self.combobox_msb_wire_size.get()
           job_dict["jobVrise"]["notes"] = self.ent_notes.get()
           job_dict["jobVrise"]["maxCurrent"] = max(self.new_imax_phase1,self.new_imax_phase2,self.new_imax_phase3)
           return True

   def fill_Vrise(self,job_dict,inv_dict,user_pref):
       #Maybe can ameliorate this
       inv_type = job_dict["jobComponents"]["invType"]
       inv_manu = job_dict["jobComponents"]["invManufacturer"]
       inv_model = job_dict["jobComponents"]["invModel"]

       #Only used if saved job
       self.ent_serv_len.delete(0, 'end')
       self.ent_serv_len.insert(0,job_dict["jobVrise"]["lenService"])
       self.ent_msb_len.delete(0, 'end')
       self.ent_msb_len.insert(0,job_dict["jobVrise"]["lenMsb"])
       self.ent_cons_len.delete(0, 'end')
       self.ent_cons_len.insert(0,job_dict["jobVrise"]["lenConsumer"])
       self.ent_notes.insert(0,job_dict["jobVrise"]["notes"])
       if job_dict["jobVrise"]["cableSize"] != "":
           self.combobox_msb_wire_size.set(job_dict["jobVrise"]["cableSize"])


   def link_serv_wire_ccc(self,job_dict):
       ccc_serv = vrise_dictionnaries.ccc_dict[self.new_phase_inv_1]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_serv_wire_size.get()]
       lbl_ccc2 = ttk.Label(self, text=ccc_serv).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=1,pady=2)
       self.calculate_Vrise()

   def link_cons_wire_ccc(self,job_dict):
       ccc_cons = vrise_dictionnaries.ccc_dict[self.new_phase_inv_2]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_cons_wire_size.get()]
       lbl_ccc3 = ttk.Label(self, text=ccc_cons).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=2,pady=2)
       self.calculate_Vrise()

   def link_msb_wire_ccc(self,job_dict):
       ccc_msb = vrise_dictionnaries.ccc_dict[self.new_phase_inv_3]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_msb_wire_size.get()]
       lbl_ccc4 = ttk.Label(self, text=ccc_msb).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=3)
       self.calculate_Vrise()
