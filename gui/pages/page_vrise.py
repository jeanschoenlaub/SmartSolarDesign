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
       self.ent_phase_serv = ttk.Entry(self, width=2,style="my.TEntry")
       self.ent_phase_cons = ttk.Entry(self, width=2,style="my.TEntry")
       self.ent_phase_msb = ttk.Entry(self, width=2,style="my.TEntry")
       self.ent_serv_len = ttk.Entry(self, width=3,style="my.TEntry")
       self.ent_cons_len = ttk.Entry(self, width=3,style="my.TEntry")
       self.ent_msb_len = ttk.Entry(self, width=3,style="my.TEntry")
       self.ent_imax_serv = ttk.Entry(self, width=4,style="my.TEntry")
       self.ent_imax_cons= ttk.Entry(self, width=4,style="my.TEntry")
       self.ent_imax_msb = ttk.Entry(self, width=4,style="my.TEntry")
       self.butt_calculate = ttk.Button(self, text="   Calculate   ", command=self.calculate_Vrise)
       self.combobox_msb_wire_size = ttk.Combobox(self, values="", state='readonly',width=3)
       self.combobox_cons_wire_size = ttk.Combobox(self, values="", state='readonly',width=3)
       self.combobox_serv_wire_size = ttk.Combobox(self, values="", state='readonly',width=3)
       self.ent_notes =  ttk.Entry(self, width= 50,style="my.TEntry")

       #Used to set text color for ttk labels - ! Formating is weird ('mRed.TLabel' - here I think TLabel is necessary)
       self.mRed = ttk.Style()
       self.mRed.configure('mRed.TLabel', foreground="red")
       self.mGreen = ttk.Style()
       self.mGreen.configure('mGreen.TLabel', foreground="green")

       self.pack()

   def show_entries(self):

       lbl_title1 = ttk.Label(self, text="          Voltage Rise Calculations (AC Side)",font='Helvetica 14 bold').grid(row = 0,columnspan=4,pady=20)
       lbl_empty_space=ttk.Label(self, text="",font='Helvetica 14 bold').grid(row = 1,columnspan=4,pady=constants.SPACING_FROM_TITLE_PGVRISE)
       #1st line
       self.ent_col1_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=1,padx=constants.COLUMN1_NAME_PADX_PGVRISE)
       self.ent_col2_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=2,padx=constants.COLUMN2_NAME_PADX_PGVRISE)
       self.ent_col3_name.grid(row=constants.ROW_NAME_ENT_PGVRISE, column=3,padx=constants.COLUMN3_NAME_PADX_PGVRISE)

       #2nd line
       lbl_phases = ttk.Label(self, text="Inv phases:").grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=0, sticky="e")
       self.ent_phase_serv.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=1,pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       self.ent_phase_cons.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=2)
       self.ent_phase_msb.grid(row=constants.ROW_PHASE_ENT_PGVRISE, column=3)

       #3rd line
       lbl_cond1 = ttk.Label(self, text="Conductor:").grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=0, sticky="e")
       lbl_cond2 = ttk.Label(self, text="Copper").grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=1,pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       lbl_cond3 = ttk.Label(self, text="Copper").grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=2)
       lbl_cond4 = ttk.Label(self, text="Copper").grid(row=constants.ROW_CONDUCTOR_ENT_PGVRISE, column=3)

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

       #7th line
       lbl_imax = ttk.Label(self, text="Imax/phase:").grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       self.ent_imax_serv.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=1,pady=2)
       self.ent_imax_cons.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=2)
       self.ent_imax_msb.grid(row=constants.ROW_IMAX_ENT_PGVRISE, column=3)

       #Calculation part (the rest is in calculate_Vrise)
       lbl_imax = ttk.Label(self, text="Am/%Vd :").grid(row=constants.ROW_AM_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       lbl_Vdrop_prct = ttk.Label(self, text="Vdrop % :").grid(row=constants.ROW_VDROP_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       lbl_Vdrop_prct_tot = ttk.Label(self, text="Total %:").grid(row=constants.ROW_TOTAL_PRC_ENT_PGVRISE, column=0, sticky="e",pady=constants.ROW_SPACING_TABLE_PADY_PGVRISE)
       self.butt_calculate.grid(row=constants.ROW_CALC_BUTT_PGVRISE,columnspan=4,pady=20)

       #Notes part
       lbl_notes = ttk.Label(self, text="Vrise Notes:").grid(row=constants.ROW_NOTES_ENT_PGVRISE, column=0, sticky="e",pady=10)
       self.ent_notes.grid(row=constants.ROW_NOTES_ENT_PGVRISE,column = 1,columnspan=3,pady=10)

   def calculate_Vrise(self):
       Am1 = vrise_dictionnaries.AmPercent_dict[self.combobox_serv_wire_size.get()][self.ent_phase_serv.get()]
       Am2 = vrise_dictionnaries.AmPercent_dict[self.combobox_cons_wire_size.get()][self.ent_phase_cons.get()]
       Am3 = vrise_dictionnaries.AmPercent_dict[self.combobox_msb_wire_size.get()][self.ent_phase_msb.get()]

       constants.set_entries_background_for_darkmode()

       lbl_l7_left = ttk.Label(self, text=Am1).grid(row=constants.ROW_AM_ENT_PGVRISE, column=1)
       lbl_l7_mid = ttk.Label(self, text=Am2).grid(row=constants.ROW_AM_ENT_PGVRISE, column=2)
       lbl_l7_right = ttk.Label(self, text=Am3).grid(row=constants.ROW_AM_ENT_PGVRISE, column=3)

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



   def submit_Vrise(self,job_dict):

       job_dict["jobVrise"]["col1Name"] = self.ent_col1_name.get()
       job_dict["jobVrise"]["col2Name"] = self.ent_col2_name.get()
       job_dict["jobVrise"]["col3Name"] = self.ent_col3_name.get()
       job_dict["jobSetup"]["phases"] = self.ent_phase_serv.get()#This one is not very usefull and maybe should be removed
       job_dict["jobVrise"]["lenConsumer"] = self.ent_cons_len.get()
       job_dict["jobVrise"]["lenService"] = self.ent_serv_len.get()
       job_dict["jobVrise"]["lenMsb"]= self.ent_msb_len.get()
       job_dict["jobVrise"]["cableSize"] = self.combobox_msb_wire_size.get()
       job_dict["jobVrise"]["notes"] = self.ent_notes.get()
       job_dict["jobVrise"]["maxCurrent"] = max(self.ent_imax_serv.get(),self.ent_imax_cons.get(),self.ent_imax_msb.get())

   def fill_Vrise(self,job_dict,inv_dict,user_pref):
       #Maybe can ameliorate this
       inv_type = job_dict["jobComponents"]["invType"]
       inv_manu = job_dict["jobComponents"]["invManufacturer"]
       inv_model = job_dict["jobComponents"]["invModel"]

       #1st line
       if job_dict["jobVrise"]["col1Name"] != "": #If it is a saved job
           self.ent_col1_name.delete(0, 'end')
           self.ent_col1_name.insert(0,job_dict["jobVrise"]["col1Name"])
           self.ent_col2_name.delete(0, 'end')
           self.ent_col2_name.insert(0,job_dict["jobVrise"]["col2Name"])
           self.ent_col3_name.delete(0, 'end')
           self.ent_col3_name.insert(0,job_dict["jobVrise"]["col3Name"])
       else: #If not fill in the user preferred naming
           self.ent_col1_name.delete(0, 'end')
           self.ent_col1_name.insert(0,user_pref["Vrise_pref"]["col1_name"])
           self.ent_col2_name.delete(0, 'end')
           self.ent_col2_name.insert(0,user_pref["Vrise_pref"]["col2_name"])
           self.ent_col3_name.delete(0, 'end')
           self.ent_col3_name.insert(0,user_pref["Vrise_pref"]["col3_name"])

       #Fills the phases depending on inverter
       self.ent_phase_serv.delete(0, 'end') #deletes previous entries
       self.ent_phase_serv.insert(0,inv_dict[inv_type][inv_manu][inv_model]["Phases"])
       self.ent_phase_cons.delete(0, 'end')
       self.ent_phase_cons.insert(0,inv_dict[inv_type][inv_manu][inv_model]["Phases"])
       self.ent_phase_msb.delete(0, 'end')
       self.ent_phase_msb.insert(0,inv_dict[inv_type][inv_manu][inv_model]["Phases"])

       #Fills the Imax out depending on the chosen inverter (Editable if export limit)
       if inv_type != "Micro": #Because micro inverter output current depends on their number in a string
           self.ent_imax_serv.delete(0, 'end')
           self.ent_imax_serv.insert(0,inv_dict[inv_type][inv_manu][inv_model]["IOutMax"])
           self.ent_imax_cons.delete(0, 'end')
           self.ent_imax_cons.insert(0,inv_dict[inv_type][inv_manu][inv_model]["IOutMax"])
           self.ent_imax_msb.delete(0, 'end')
           self.ent_imax_msb.insert(0,inv_dict[inv_type][inv_manu][inv_model]["IOutMax"])
       else:#i.e for micro inverters (only if saved before)
           self.ent_imax_serv.delete(0, 'end')
           self.ent_imax_serv.insert(0,job_dict["jobVrise"]["maxCurrent"])
           self.ent_imax_cons.delete(0, 'end')
           self.ent_imax_cons.insert(0,job_dict["jobVrise"]["maxCurrent"])
           self.ent_imax_msb.delete(0, 'end')
           self.ent_imax_msb.insert(0,job_dict["jobVrise"]["maxCurrent"])
           self.ent_phase_serv.delete(0, 'end') #deletes previous entries
           self.ent_phase_serv.insert(0,job_dict["setupEnphase"]["micro_phases"])
           self.ent_phase_cons.delete(0, 'end')
           self.ent_phase_cons.insert(0,job_dict["setupEnphase"]["micro_phases"])
           self.ent_phase_msb.delete(0, 'end')
           self.ent_phase_msb.insert(0,job_dict["setupEnphase"]["micro_phases"])

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

       #CCC after saves on purpose
       try:
           ccc_serv = vrise_dictionnaries.ccc_dict[self.ent_phase_serv.get()]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_serv_wire_size.get()]
           ccc_cons = vrise_dictionnaries.ccc_dict[self.ent_phase_cons.get()]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_cons_wire_size.get()]
           ccc_msb = vrise_dictionnaries.ccc_dict[self.ent_phase_msb.get()]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_msb_wire_size.get()]
           lbl_ccc2 = ttk.Label(self, text=ccc_serv).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=1,pady=2)
           lbl_ccc3 = ttk.Label(self, text=ccc_cons).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=2)
           lbl_ccc4 = ttk.Label(self, text=ccc_msb).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=3)
       except:
           tk.messagebox.showinfo(title="Error - CCC not supported",message = "Sorry the Current Carrying Capacity for the cable selected is not supported yet", icon="warning")


   def link_serv_wire_ccc(self,job_dict):
       ccc_serv = vrise_dictionnaries.ccc_dict[self.ent_phase_serv.get()]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_serv_wire_size.get()]
       lbl_ccc2 = ttk.Label(self, text=ccc_serv).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=1,pady=2)

   def link_cons_wire_ccc(self,job_dict):
       ccc_cons = vrise_dictionnaries.ccc_dict[self.ent_phase_cons.get()]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_cons_wire_size.get()]
       lbl_ccc3 = ttk.Label(self, text=ccc_cons).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=2,pady=2)

   def link_msb_wire_ccc(self,job_dict):
       ccc_msb = vrise_dictionnaries.ccc_dict[self.ent_phase_msb.get()]["XlpeCu"]["CompleteThermalInsulation"][self.combobox_msb_wire_size.get()]
       lbl_ccc4 = ttk.Label(self, text=ccc_msb).grid(row=constants.ROW_CCC_ENT_PGVRISE, column=3)
