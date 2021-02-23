import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
import math
import webbrowser
import fitz  # this is pymupdf

import databases.constants as constants

from gui.save_manager import save_job,load_job

from import_info.read_txt import get_txtfile_info
from import_info.read_pdf import get_pdf_info

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, **kwargs, bg=constants.set_baground_for_theme())


class PageInfo(Page):
   def __init__(self, *args, **kwargs):
       #Initialie the Frame
       Page.__init__(self, *args, **kwargs)

       #List of all dynamic labels (dynamic = show/hide)
       self.lbl_existing_array = ttk.Label(self, text="Size (kWac):")
       self.lbl_monitoring = ttk.Label(self, text="Monitoring P:")

       #List of all the entries (text entries + comboboxes)
       self.ent_client_name = ttk.Entry(self, width=45,style="my.TEntry")
       self.ent_site = ttk.Entry(self, width=45,style="my.TEntry")
       self.ent_job_number = ttk.Entry(self, width=14,style="my.TEntry")
       self.ent_panel_number = ttk.Entry(self, width=3,style="my.TEntry")
       self.ent_num_msb_phases = ttk.Entry(self, width=3,style="my.TEntry")
       self.combobox_panel_manufacturer = ttk.Combobox(self, values="", state='readonly',width=15,style="my.TEntry")
       self.combobox_panel_model = ttk.Combobox(self, values="", state='readonly',width=15,style="my.TEntry")
       self.combobox_inv_type = ttk.Combobox(self, values="", state='readonly',width=15,style="my.TEntry")
       self.combobox_inv_manufacturer = ttk.Combobox(self, values="", state='readonly',width=15,style="my.TEntry")
       self.combobox_inv_model = ttk.Combobox(self, values="", state='readonly',width=15,style="my.TEntry" )
       self.ent_existing_array = ttk.Entry(self, width=5,style="my.TEntry") #only called if existing array checkbox (i.e dynamic)
       self.combobox_battery = ttk.Combobox(self, values="", state='readonly',width=15,style="my.TEntry")
       self.ent_num_battery = ttk.Entry(self, width=3,style="my.TEntry") #only called if battery checkbox (i.e dynamic)
       self.ent_monitoring = ttk.Entry(self, width=3,style="my.TEntry") #only called if monitoring checkbox  (i.e dynamic)
       self.ent_notes =  ttk.Entry(self, width= 45,style="my.TEntry")

       #list of the variables used
       self.var_monitoring = tk.IntVar() # used for the monitoring tickbox
       self.var_backup = tk.IntVar() # used for the monitoring tickbox
       self.var_relay = tk.IntVar() # used for the enphhase qrelay tickbox
       self.var_existing_array = tk.IntVar()  # used for the existing array tickbox
       self.var_battery = tk.IntVar()  # used for the battery tickbox
       self.var_block_diagram = tk.IntVar()  # used for the block diagram tickbox
       self.var_gateway = tk.IntVar()  # used for the block diagram tickbox

       #list of tickoxes used
       self.check_monitoring = ttk.Checkbutton(self, text="Monitoring:",variable=self.var_monitoring,command=self.monitoring_param)
       self.check_existing_array = ttk.Checkbutton(self, text="Existing array",variable=self.var_existing_array,command = self.existing_array_param)
       self.check_battery=ttk.Checkbutton(self, text="Battery:",variable=self.var_battery,command=self.battery_param)
       self.check_block_diag = ttk.Checkbutton(self, text="Block Diagram",variable=self.var_block_diagram)
       self.check_gateway = ttk.Checkbutton(self, text="Gateway:",variable=self.var_gateway)
       self.check_back_up = ttk.Checkbutton(self, text="Back-up", variable=self.var_backup)
       self.check_relay = ttk.Checkbutton(self, text="1P relay", variable=self.var_relay)

       #list of buttons
       self.butt_find_job = ttk.Button(self, text="Find", command=self.find_job,style='my.TButton')
       self.butt_import_pdf = ttk.Button(self, text="PDF", command=self.read_pdf,style='my.TButton')
       self.butt_datasheet_inv = ttk.Button(self, text="Datasheet Link", command=self.datasheet_inv,style='my.TButton')
       self.butt_datasheet_panel = ttk.Button(self, text="Datasheet Link", command=self.datasheet_panel,style='my.TButton')

       #List of images
       self.title_info = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Titles/InfoTitle.png")
       self.title_components = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Titles/ComponentsTitle.png")
       self.title_extras = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Titles/ExtrasTitle.png")

       #This may be improved but rn needed to link the comboboxes
       self.inv_dict = ""
       self.batt_dict = ""

       self.pack()

   def show_entries(self,job_dict,panel_dict,inv_dict,batt_dict): # Function which places the widget on the grid

       #This should be improved ( RN needed to link the comboboxes )
       self.job_dict = job_dict
       self.inv_dict = inv_dict
       self.batt_dict = batt_dict
       self.panel_dict = panel_dict

       #Client information section
       #lbl_empty_space0 = ttk.Label(self, text = "").grid(row = constants.ROW_EMPTY0_PGINFO,columnspan=5)
       lbl_title1 = ttk.Label(self, image = self.title_info)
       lbl_title1.grid(row = constants.ROW_TITLE_1_PGINFO,columnspan=5)
       # Create the Label and Entry widgets for "Client Name"
       lbl_client_name = ttk.Label(self, text="Client Name:").grid(row=constants.ROW_CLIENT_NAME_PGINFO, column=1, sticky="e")
       self.ent_client_name.grid(row=constants.ROW_CLIENT_NAME_PGINFO, column=2,columnspan=3,sticky="w")#Then insert the value we got from the text file in function insert_values()
       # Create the Label and Entry widgets for "Site"
       lbl_site = ttk.Label(self, text="Site:")
       lbl_site.grid(row=constants.ROW_SITE_ADDRESS_PGINFO, column=1, sticky="e")
       self.ent_site.grid(row=constants.ROW_SITE_ADDRESS_PGINFO, column=2,columnspan=3,sticky="w")
       # Create the Label and Entry widgets for "Job number"
       lbl_job_number = ttk.Label(self, text="Job number:").grid(row=constants.ROW_JOB_NUMBER_PGINFO, column=1, sticky="e")
       self.ent_job_number.grid(row=constants.ROW_JOB_NUMBER_PGINFO, column=2, sticky="w")
       self.ent_job_number.bind('<Return>', self.find_job)
       self.butt_find_job.grid(row=constants.ROW_JOB_NUMBER_PGINFO, column=3, sticky="w")
       self.butt_import_pdf.grid(row=constants.ROW_JOB_NUMBER_PGINFO, column=4, sticky="w")


       # Create the Label and Entry widgets for "MSB Phases""
       lbl_msb_phases = ttk.Label(self, text="MSB phases:").grid(row=constants.ROW_MSB_PHASES_PGINFO, column=1, sticky="e")
       self.ent_num_msb_phases.grid(row=constants.ROW_MSB_PHASES_PGINFO, column=2, sticky="w")


       #Job Components Section
       lbl_empty_space1 = ttk.Label(self, text = "").grid(row = constants.ROW_EMPTY1_PGINFO,columnspan=5,pady=constants.EMPTY_PADY_PGINFO)
       lbl_title2 = ttk.Label(self, image = self.title_components)
       lbl_title2.grid(row = constants.ROW_TITLE_2_PGINFO,columnspan=5)
       # Create the Label and Entry widgets for "Panels"
       lbl_panels = ttk.Label(self, text="Panel Manufacturer:").grid(row=constants.ROW_PANEL_MANUFACTURER_PGINFO, column=1, sticky="e")
       self.combobox_panel_manufacturer['values']=list(panel_dict.keys())
       self.combobox_panel_manufacturer.current(0)
       self.combobox_panel_manufacturer.bind("<<ComboboxSelected>>", self.link_panel_manufacturer_to_model)
       self.combobox_panel_manufacturer.grid(row=constants.ROW_PANEL_MANUFACTURER_PGINFO, column=2, sticky="w")
       lbl_panel_model = ttk.Label(self, text="Panel Model:").grid(row=constants.ROW_PANEL_MODEL_PGINFO, column=1, sticky="e")
       self.combobox_panel_model['values']=list(panel_dict["LG Electronics"].keys())
       self.combobox_panel_model.current(0)
       self.combobox_panel_model.bind("<<ComboboxSelected>>", self.panel_model_dehighlight)
       self.combobox_panel_model.grid(row=constants.ROW_PANEL_MODEL_PGINFO, column=2, sticky="w")
       lbl_panel_number = ttk.Label(self, text="Number:").grid(row=constants.ROW_PANEL_NUMBER_PGINFO, column=1, sticky="e")
       self.ent_panel_number.grid(row=constants.ROW_PANEL_NUMBER_PGINFO, column=2,pady=2,sticky="w")
       #Setup of the inverter type dropdown menu
       lbl_inv_type = ttk.Label(self, text="Inverter type:").grid(row=constants.ROW_INV_TYPE_PGINFO, column=3, sticky="e")
       self.combobox_inv_type['values']=list(inv_dict.keys())
       self.combobox_inv_type.current(0)
       self.combobox_inv_type.bind("<<ComboboxSelected>>", self.link_invtype_manufacturer)
       self.combobox_inv_type.grid(row=constants.ROW_INV_TYPE_PGINFO, column=4, sticky="w")
       #Setup of the inverter manufacturer dropdown menu
       lbl_inv_manu = ttk.Label(self, text="            Manufacturer:").grid(row=constants.ROW_INV_MANUFACTURER_PGINFO, column=3, sticky="e")#Extra space to have more room in between panels and  inverter selection
       self.combobox_inv_manufacturer['values']=list(inv_dict["String"].keys())
       self.combobox_inv_manufacturer.current(0)
       self.combobox_inv_manufacturer.bind("<<ComboboxSelected>>", self.link_manufacturer_model)
       self.combobox_inv_manufacturer.grid(row=constants.ROW_INV_MANUFACTURER_PGINFO, column=4, sticky="w")
       #Setup of the inverter model dropdown menu
       lbl_inv_model = ttk.Label(self, text="Model:")
       lbl_inv_model.grid(row=constants.ROW_INV_MODEL_PGINFO, column=3, sticky="e")
       self.combobox_inv_model['values']=list(inv_dict["String"]["SMA"].keys())
       self.combobox_inv_model.current(0)
       self.combobox_inv_model.bind("<<ComboboxSelected>>", self.inv_model_dehighlight)
       self.combobox_inv_model.grid(row=constants.ROW_INV_MODEL_PGINFO, column=4, sticky="w")
       #Setup datasheet buttons
       self.butt_datasheet_panel.grid(row=constants.ROW_BUTT_DATASHEET_PGINFO, column=1,columnspan=3)
       self.butt_datasheet_inv.grid(row=constants.ROW_BUTT_DATASHEET_PGINFO, column=4,sticky="w")

       # Extra option section
       lbl_empty_space2 = ttk.Label(self, text = "").grid(row = constants.ROW_EMPTY2_PGINFO,columnspan=5,pady=constants.EMPTY_PADY_PGINFO)
       lbl_title3 = ttk.Label(self, image = self.title_extras)
       lbl_title3.grid(row = constants.ROW_TITLE_3_PGINFO,columnspan=5)
       #Placement of the checkboxes
       self.check_monitoring.grid(row=constants.ROW_MONITORING_PGINFO, column = constants.COL_MONITORING_CHK_PGINFO, sticky="w",pady=2,padx=constants.PADX_CHK_PGINFO)
       self.check_existing_array.grid(row=constants.ROW_EXISTING_ARRAY_PGINFO, column = constants.COL_EXISTING_ARRAY_CHK_PGINFO, sticky="w",pady=2,padx=constants.PADX_CHK_PGINFO)
       self.check_battery.grid(row=constants.ROW_BATTERY_PGINFO, column = constants.COL_BATTERY_CHK_PGINFO, sticky="w",pady=2,padx=constants.PADX_CHK_PGINFO)
       self.check_block_diag.grid(row=constants.ROW_BLOCK_DIAGRAM_PGINFO, column = constants.COL_BLOCK_DIAGRAM_CHK_PGINFO, sticky="w",pady=2,padx=constants.PADX_CHK_PGINFO)
       self.check_gateway.grid(row=constants.ROW_GATEWAY_PGINFO, column = constants.COL_GATEWAY_CHK_PGINFO, sticky="w",pady=2,padx=constants.PADX_CHK_PGINFO)
       lbl_notes = ttk.Label(self, text="SLD Notes :").grid(row= constants.ROW_NOTES_PGINFO, column= constants.COL_NOTES_PGINFO, sticky="e",padx=5)
       self.ent_notes.grid(row=constants.ROW_NOTES_PGINFO,column = constants.COL_NOTES_PGINFO+1,columnspan=3,pady=10,sticky ="w")

       self.grid_rowconfigure(0, weight=1)
       self.grid_rowconfigure(constants.ROW_NOTES_PGINFO+1, weight=1)
       self.grid_columnconfigure(0, weight=1)
       self.grid_columnconfigure(4, weight=1)

   def inv_model_dehighlight(self,*args):
        self.combobox_inv_model.selection_clear()

   def panel_model_dehighlight(self,*args):
        self.combobox_panel_model.selection_clear()

   def link_panel_manufacturer_to_model(self,*args): #Function called upon choosing an inverter type from the combobox
        self.combobox_panel_model['values']=list(self.panel_dict[self.combobox_panel_manufacturer.get()].keys())
        self.combobox_panel_model.current(0)
        self.combobox_panel_manufacturer.selection_clear()

   def link_invtype_manufacturer(self,*args): #Function called upon choosing an inverter type from the combobox
        self.combobox_inv_manufacturer['values']=list(self.inv_dict[self.combobox_inv_type.get()].keys())
        self.combobox_inv_manufacturer.current(0)

        #Conditional appearance of inverter type specific options
        if self.combobox_inv_type.get() == "Hybrid":
             self.check_back_up.grid(row=constants.ROW_INV_MANUFACTURER_PGINFO, column =2, sticky="e")
        else:
             self.check_back_up.grid_remove()

        if self.combobox_inv_type.get() == "Micro":
             self.check_relay.grid(row=constants.ROW_INV_TYPE_PGINFO, column =2, sticky="e")
        else:
            self.check_relay.grid_remove()

        self.link_manufacturer_model() # Necessary otherwise manufacturer updates but not model

   def link_manufacturer_model(self,*args): #Function called upon choosing an inverter manufacturer from the combobox
        self.combobox_inv_model['values']=list(self.inv_dict[self.combobox_inv_type.get()][self.combobox_inv_manufacturer.get()].keys())
        self.combobox_inv_model.current(0) #Updates the inverter model list (for the choosen manufacturer)
        self.combobox_inv_type.selection_clear()
        self.combobox_inv_manufacturer.selection_clear()

   def existing_array_param(self,*args):
       if self.var_existing_array.get() == 1:
           self.lbl_existing_array.grid(row=constants.ROW_EXISTING_ARRAY_PGINFO, column=2,sticky="e")
           self.ent_existing_array.grid(row=constants.ROW_EXISTING_ARRAY_PGINFO, column=3,sticky="w")
       if self.var_existing_array.get() == 0:
           self.lbl_existing_array.grid_remove()
           self.ent_existing_array.grid_remove()


   def monitoring_param(self,*args):
       if self.var_monitoring.get() == 1:
           self.lbl_monitoring.grid(row=constants.ROW_MONITORING_PGINFO, column=2, sticky="e")
           self.ent_monitoring.grid(row=constants.ROW_MONITORING_PGINFO, column=3,sticky="w")
       else:
           self.lbl_monitoring.grid_remove()
           self.ent_monitoring.grid_remove()

   def battery_param(self,*args):
       self.combobox_battery['values']=list(self.batt_dict.keys())
       self.combobox_battery.current(0)
       self.combobox_battery.grid(row=constants.ROW_BATTERY_PGINFO, column=1, sticky="w")
       lbl_battery_num = ttk.Label(self, text="Number:").grid(row=constants.ROW_BATTERY_PGINFO, column=2, sticky="e")
       self.ent_num_battery.grid(row=constants.ROW_BATTERY_PGINFO, column=3, sticky="w")

   def insert_values(self): #Insert saved or txt_file read values in the entries
        self.ent_client_name.delete(0,"end")
        self.ent_client_name.insert(0,self.job_dict["jobInfo"]["clientName"])
        self.ent_site.delete(0,"end")
        self.ent_site.insert(0,self.job_dict["jobInfo"]["siteName"])
        self.ent_panel_number.delete(0,"end")
        self.ent_panel_number.insert(0,self.job_dict["jobComponents"]["panelNumber"])

        #Only for saved projects:
        if self.job_dict["jobComponents"]["panelModel"] != "":
            self.combobox_panel_model.set(self.job_dict["jobComponents"]["panelModel"])
            self.combobox_panel_manufacturer.set(self.job_dict["jobComponents"]["panelManufacturer"])
        if self.job_dict["jobComponents"]["invType"] != "":
            self.combobox_inv_type.set(self.job_dict["jobComponents"]["invType"])
            self.combobox_inv_manufacturer.set(self.job_dict["jobComponents"]["invManufacturer"])
            self.link_manufacturer_model()
            self.combobox_inv_model.set(self.job_dict["jobComponents"]["invModel"])
            self.ent_num_msb_phases.insert(0,self.job_dict["jobInfo"]["numMsbPhases"])
        if self.job_dict["jobExtra"]["existingArray"] == "On":
            self.var_existing_array.set(1)
            self.existing_array_param()
        elif self.job_dict["jobExtra"]["existingArray"] != "":
            self.var_existing_array.set(1)
            self.existing_array_param()
            self.ent_existing_array.insert(0,self.job_dict["jobExtra"]["existingArray"])
        if self.job_dict["jobExtra"]["monitoring"] == "On":
            self.var_monitoring.set(1)
            self.monitoring_param()
        elif self.job_dict["jobExtra"]["monitoring"] != "":
            self.var_monitoring.set(1)
            self.monitoring_param()
            self.ent_monitoring.insert(0,self.job_dict["jobExtra"]["monitoring"])
        if self.job_dict["jobExtra"]["gateway"] == 1:
            self.var_gateway.set(1)
        if self.job_dict["jobExtra"]["notes"] != "":
            self.ent_notes.insert(0,self.job_dict["jobExtra"]["notes"])


   def submit_job_info(self): #Called when leaving the page or on Save click - Updates the job_dictionary associated with the job number
       self.job_dict["jobInfo"]["clientName"] = self.ent_client_name.get()
       self.job_dict["jobInfo"]["jobNumber"] = self.ent_job_number.get()
       self.job_dict["jobComponents"]["panelNumber"] = self.ent_panel_number.get()
       self.job_dict["jobComponents"]["invType"] =self.combobox_inv_type.get()
       self.job_dict["jobComponents"]["panelManufacturer"] = self.combobox_panel_manufacturer.get()
       self.job_dict["jobComponents"]["panelModel"] = self.combobox_panel_model.get()
       self.job_dict["jobInfo"]["siteName"] = self.ent_site.get()
       self.job_dict["jobComponents"]["invModel"] = self.combobox_inv_model.get()
       self.job_dict["jobComponents"]["invManufacturer"]= self.combobox_inv_manufacturer.get()
       self.job_dict["jobInfo"]["numMsbPhases"] = self.ent_num_msb_phases.get()
       if self.ent_num_msb_phases.get() == "":
           tk.messagebox.showinfo(parent=self,title="Error - Number of MSB phase required",message = "The number of MSB phases was not specified", icon="warning")
           return "rollback"
       self.job_dict["jobExtra"]["backup"] = self.var_backup.get()
       self.job_dict["setupEnphase"]["qrelay"] = self.var_relay.get()
       self.job_dict["jobExtra"]["battery"] = self.combobox_battery.get()
       self.job_dict["jobExtra"]["batteryNumber"] = self.ent_num_battery.get()
       self.job_dict["jobExtra"]["blockDiagram"] = self.var_block_diagram.get()
       self.job_dict["jobExtra"]["gateway"] = self.var_gateway.get()
       self.job_dict["jobExtra"]["notes"] = self.ent_notes.get()

       if self.var_relay.get() == 1:
           self.job_dict["setupEnphase"]["micro_phases"]=1
       else:
           self.job_dict["setupEnphase"]["micro_phases"] = self.job_dict["jobInfo"]["numMsbPhases"]

       if self.var_existing_array.get() ==1 and self.ent_existing_array.get() != "":
           self.job_dict["jobExtra"]["existingArray"] = self.ent_existing_array.get()
       elif self.var_existing_array.get() ==1:
           self.job_dict["jobExtra"]["existingArray"] = "On"
       else:
           self.job_dict["jobExtra"]["existingArray"] = ""

       if self.var_monitoring.get() ==1 and self.ent_monitoring.get() != "":
           self.job_dict["jobExtra"]["monitoring"] = self.ent_monitoring.get()
       elif self.var_monitoring.get() ==1:
           self.job_dict["jobExtra"]["monitoring"] = "On"
       else:
           self.job_dict["jobExtra"]["monitoring"] = ""

       return self.job_dict

   def delete_entries(self,*args):
        self.ent_client_name.delete(0, 'end')
        self.ent_job_number.delete(0, 'end')
        self.ent_panel_number.delete(0, 'end')
        self.ent_num_msb_phases.delete(0, 'end')
        self.ent_num_battery.delete(0, 'end')
        self.ent_site.delete(0, 'end')
        self.ent_notes.delete(0, 'end')

        self.combobox_inv_type.current(0)
        self.combobox_panel_manufacturer.current(0)
        self.combobox_panel_model.current(0)
        self.combobox_inv_model.current(0)
        self.combobox_inv_manufacturer.current(0)

        self.var_block_diagram.set(0)
        self.var_gateway.set(0)
        self.var_backup.set(0)
        self.var_relay.set(0)
        self.var_monitoring.set(0)
        self.var_monitoring.set(0)

   def datasheet_inv(self,*args):
       inv_type=self.combobox_inv_type.get()
       inv_manufacturer=self.combobox_inv_manufacturer.get()
       inv_model=self.combobox_inv_model.get()
       url = self.inv_dict[inv_type][inv_manufacturer][inv_model]["Url"]
       webbrowser.open(url)


   def datasheet_panel(self,*args):
       panel_manufacturer=self.combobox_panel_manufacturer.get()
       panel_model=self.combobox_panel_model.get()
       url = self.panel_dict[panel_manufacturer][panel_model]["Url"]
       webbrowser.open(url)

   def read_pdf(self,*args):
       pdf_file = filedialog.askopenfilename(title = "Select input pdf",initialdir = "/Users/Jean/Downloads")
       with fitz.open(pdf_file) as doc:
           text = ""
           for page in doc:
               text += page.getText()
       get_pdf_info(text,self.job_dict,self.panel_dict,self.inv_dict)
       self.insert_values()

   def find_job(self,*args):
       job_number=self.ent_job_number.get()
       try:
           get_txtfile_info(job_number,self.job_dict)
           try:
               self.job_dict=load_job(job_number)
               print("Using Saved Values")
           except:
               print("Using Gdrive Values")
       except:
           tk.messagebox.showinfo(title="Error - Job not found",message = "The job number specified was not found", icon="warning")
       self.insert_values()
