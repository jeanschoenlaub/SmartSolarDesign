import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import math

import databases.constants as constants


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self,  **kwargs,bg=constants.set_baground_for_theme())


class PageString(Page):
   def __init__(self, *args, **kwargs,):
       Page.__init__(self, *args, **kwargs)

       self.title_layout = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Titles/LayoutTitle.png")

       lbl_title1 = ttk.Label(self, image = self.title_layout)
       lbl_title1.grid(row = 1 ,column=1)

       self.inv= tk.Canvas(self, width=constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT, height=400, highlightthickness=0)#highlightthickness set to 0 to eliminate gap, width and height set bigger than window



       #This section centers the canvas
       if (constants.WINDOW_SIZE_X-constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT) > 0:
           centered_canvas_x = (constants.WINDOW_SIZE_X-constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT)/2
           self.delta_x=(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT-600)/2#600 is the measured size of drawing
       else:
           centered_canvas_x = 0
           self.delta_x=0
       if (constants.WINDOW_SIZE_Y-constants.HEIGHT_CANVAS_LAYOUT_STRING_PGLAYOUT) > 0:
           centered_canvas_y = (constants.WINDOW_SIZE_Y-constants.HEIGHT_CANVAS_LAYOUT_STRING_PGLAYOUT)/2
       else:
           centered_canvas_y = 0
       self.inv.grid(row=2,column=1,sticky="nsew", padx=centered_canvas_x,pady=centered_canvas_y)

       self.number_string_mpptA = 1
       self.number_string_mpptB = 1

       #Manually drawing the inverter and string schematics
       #Inverter
       self.inv.create_line(self.delta_x+10, 100 ,self.delta_x+60, 100)
       self.inv.create_line(self.delta_x+10, 100 ,self.delta_x+10, 250)
       self.inv.create_line(self.delta_x+60, 100,+self.delta_x+60, 250)
       self.inv.create_line(self.delta_x+10, 250,self.delta_x+60, 250)
       self.inv.create_line(self.delta_x+10, 100,self.delta_x+60, 250)
       #mpptA3
       self.ent_mppt_a_3 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       #mpptA2
       self.ent_mppt_a_2 = ttk.Entry(self.inv,width =4,style="my.TEntry") #defined here but only appears if + clicked(for tab functionality)
       #mpptA1
       self.inv.create_line(self.delta_x+60, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT,self.delta_x+300, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT)
       self.ent_mppt_a_1 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(self.delta_x+300,constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT,window=self.ent_mppt_a_1)
       #mpptB1
       self.inv.create_line(self.delta_x+60, 210,self.delta_x+300, 210)
       self.ent_mppt_b_1 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(self.delta_x+300,210,window=self.ent_mppt_b_1)
       #mpptB2
       self.ent_mppt_b_2 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       #mpptB3
       self.ent_mppt_b_3 = ttk.Entry(self.inv,width =4,style="my.TEntry")

       #Functions that dinamically add and remove strings
       self.butt_add_string_mpptA = ttk.Button(self, text="+", command=self.add_string_mpptA,style='my.TButton',width=1)
       self.inv.create_window(self.delta_x+550, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT,window=self.butt_add_string_mpptA)
       self.butt_add_string_mpptB = ttk.Button(self, text="+", command=self.add_string_mpptB,style='my.TButton',width=1)
       self.inv.create_window(self.delta_x+550, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT,window=self.butt_add_string_mpptB)
       self.butt_remove_string_mpptA = ttk.Button(self, text="-", command=self.remove_string_mpptA,style='my.TButton',width=1)
       self.butt_remove_string_mpptB = ttk.Button(self, text="-", command=self.remove_string_mpptB,style='my.TButton',width=1)



       #Functions that link the datasheets
       self.butt_datasheet_inv = ttk.Button(self, text="Inverter Datasheet Link", command=self.datasheet_inv,style='my.TButton')
       self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/2 -150,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT+50,window=self.butt_datasheet_inv)
       self.butt_datasheet_panel = ttk.Button(self, text="Panel Datasheet Link", command=self.datasheet_panel,style='my.TButton')
       self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/2 +150,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT+50,window=self.butt_datasheet_panel)

       self.lbl_designer = ttk.Label(self, text = "Drawn by:")
       self.inv.create_window(self.delta_x+10 ,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT+70,window=self.lbl_designer)
       self.lbl_checked = ttk.Label(self, text = "Checked by:")
       self.inv.create_window(self.delta_x+(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/3)+10,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT+70,window=self.lbl_checked)
       self.lbl_approved = ttk.Label(self, text = "Approved by:")
       self.inv.create_window(self.delta_x+(2*constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/3)+10,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT+70,window=self.lbl_approved)


       self.grid_rowconfigure(0, weight=1)
       self.grid_rowconfigure(3, weight=1)
       self.grid_columnconfigure(0, weight=1)
       self.grid_columnconfigure(3, weight=1)

   def add_string_mpptA(self,*args):
        if self.number_string_mpptA == 1:
            self.number_string_mpptA = 2
            self.mpptA2_p1=self.inv.create_line(self.delta_x+220, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+220, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT)
            self.mpptA2_p2=self.inv.create_line(self.delta_x+220, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+300, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT)
            self.mpptA2_p3=self.inv.create_window(self.delta_x+300,constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT,window=self.ent_mppt_a_2)
            lbl_min_stringA2 = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
            self.mpptA2_p4=self.inv.create_window(self.delta_x+420,constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT,window=lbl_min_stringA2)
            self.butt_minus_mpptA = self.inv.create_window(self.delta_x+600, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT,window=self.butt_remove_string_mpptA)
        elif self.number_string_mpptA == 2:
            self.number_string_mpptA = 3
            self.mpptA3_p1=self.inv.create_line(self.delta_x+200, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+200, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT)
            self.mpptA3_p2=self.inv.create_line(self.delta_x+200, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+300, constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT)
            self.mpptA3_p3=self.inv.create_window(self.delta_x+300,constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT,window=self.ent_mppt_a_3)
            lbl_min_stringA3 = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
            self.mpptA3_p4=self.inv.create_window(self.delta_x+420,constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT,window=lbl_min_stringA3)
        elif self.number_string_mpptA == 3:
            tk.messagebox.showinfo(parent=self,title="Warning",message = "Sorry, at the moment 4 parrallel strings are not supported yet", icon="warning")
            #tk.messagebox.showwarning(parent=self"Warning","Sorry, at the moment 4 parrallel strings are not supported on SSD")

   def remove_string_mpptA(self,*args):
        if self.number_string_mpptA == 2:
            self.number_string_mpptA = 1
            self.inv.delete(self.mpptA2_p1)
            self.inv.delete(self.mpptA2_p2)
            self.inv.delete(self.mpptA2_p3)
            self.inv.delete(self.mpptA2_p4)
            self.inv.delete(self.butt_minus_mpptA)
            self.ent_mppt_a_2.delete(0,"end")
        elif self.number_string_mpptA == 3:
            self.number_string_mpptA = 2
            self.inv.delete(self.mpptA3_p1)
            self.inv.delete(self.mpptA3_p2)
            self.inv.delete(self.mpptA3_p3)
            self.inv.delete(self.mpptA3_p4)
            self.ent_mppt_a_3.delete(0,"end")


   def add_string_mpptB(self,*args):
        if self.number_string_mpptB == 1:
            self.number_string_mpptB = 2
            self.mpptB2_p1=self.inv.create_line(self.delta_x+220, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+220, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT)
            self.mpptB2_p2=self.inv.create_line(self.delta_x+220, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+300, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+constants.SPACING_MPPTS_STRING_PGLAYOUT)
            self.mpptB2_p3=self.inv.create_window(self.delta_x+300,constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+constants.SPACING_MPPTS_STRING_PGLAYOUT,window=self.ent_mppt_b_2)
            lbl_min_stringB2 = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
            self.mpptB2_p4=self.inv.create_window(self.delta_x+420,constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+constants.SPACING_MPPTS_STRING_PGLAYOUT,window=lbl_min_stringB2)
            self.butt_minus_mpptB = self.inv.create_window(self.delta_x+600, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT,window=self.butt_remove_string_mpptB)
        elif self.number_string_mpptB == 2:
            self.number_string_mpptB = 3
            self.mpptB3_p1=self.inv.create_line(self.delta_x+200, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+2*constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+200, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT)
            self.mpptB3_p2=self.inv.create_line(self.delta_x+200, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+2*constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+300, constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+2*constants.SPACING_MPPTS_STRING_PGLAYOUT)
            self.mpptB3_p3=self.inv.create_window(self.delta_x+300,constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+2*constants.SPACING_MPPTS_STRING_PGLAYOUT,window=self.ent_mppt_b_3)
            lbl_min_stringB3 = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
            self.mpptB3_p4=self.inv.create_window(self.delta_x+420,constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT+2*constants.SPACING_MPPTS_STRING_PGLAYOUT,window=lbl_min_stringB3)
        elif self.number_string_mpptB == 3:
            tk.messagebox.showinfo(parent=self,title="Warning",message = "Sorry, at the moment 4 parrallel strings are not supported yet", icon="warning")

   def remove_string_mpptB(self,*args):
        if self.number_string_mpptB == 2:
            self.number_string_mpptB = 1
            self.inv.delete(self.mpptB2_p1)
            self.inv.delete(self.mpptB2_p2)
            self.inv.delete(self.mpptB2_p3)
            self.inv.delete(self.mpptB2_p4)
            self.inv.delete(self.butt_minus_mpptB)
            self.ent_mppt_b_2.delete(0,"end")

        elif self.number_string_mpptB == 3:
            self.number_string_mpptB = 2
            self.inv.delete(self.mpptB3_p1)
            self.inv.delete(self.mpptB3_p2)
            self.inv.delete(self.mpptB3_p3)
            self.inv.delete(self.mpptB3_p4)
            self.ent_mppt_b_3.delete(0,"end")


   def datasheet_inv(self,*args):
        inv_type=self.job_dict["jobComponents"]["invType"]
        inv_manufacturer=self.job_dict["jobComponents"]["invManufacturer"]
        inv_model=self.job_dict["jobComponents"]["invModel"]
        inv_serial = self.job_dict["jobComponents"]["invSerial"]

        url = self.inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Url"]
        webbrowser.open(url)


   def datasheet_panel(self,*args):
        panel_manufacturer=self.job_dict["jobComponents"]["panelManufacturer"]
        panel_model=self.job_dict["jobComponents"]["panelModel"]
        url = self.panel_dict[panel_manufacturer][panel_model]["Url"]
        webbrowser.open(url)

   def submit_inv_setup(self,job_dict): #Called when next paged is pressed

       #if job_dict["jobInfo"]["creationTimestamp"] == "":
           #job_dict["jobInfo"]["creationTimestamp"] = datetime.datetime.now()

       error_parra_string = True
       if self.ent_mppt_a_2.get() != "" and self.ent_mppt_a_1.get()=="":
           error_parra_string=tk.messagebox.askyesno(parent=self,title="Layout Error",message="You have inputed a parrallel string, but the main string is empty, are you sure you want to continue ?",icon="warning")
       elif self.ent_mppt_a_2.get() != self.ent_mppt_a_1.get() and self.ent_mppt_a_2.get() != "":
           error_parra_string=tk.messagebox.askyesno(parent=self,title="Layout Error",message="You have inputed parrallel strings of different lenghts, are you sure you want to continue ?",icon="warning")


       if error_parra_string == True:
           job_dict["jobSetup"]["mpptA1"] = self.ent_mppt_a_1.get()
           job_dict["jobSetup"]["mpptA2"] = self.ent_mppt_a_2.get()
           job_dict["jobSetup"]["mpptB1"] = self.ent_mppt_b_1.get()
           return "good"
       else:
           return "rollback"



   def show_limits(self,inv_dict,job_dict,panel_dict):#also loads savec entries (end)
        #list of parameters used to calculate the max and min number of panels
        #in a string (improves readability)
        panel_manu = job_dict["jobComponents"]["panelManufacturer"]
        panel_name = job_dict["jobComponents"]["panelModel"]
        panel_serial = job_dict["jobComponents"]["panelSerial"]
        inv_type = job_dict["jobComponents"]["invType"]
        inv_manufacturer = job_dict["jobComponents"]["invManufacturer"]
        inv_model = job_dict["jobComponents"]["invModel"]
        inv_serial = job_dict["jobComponents"]["invSerial"]

        self.job_dict = job_dict


        #Calulates the min and max panels (note diff round and floor)
        self.max_panels_string = math.floor(float(inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Vmax"])/(float(panel_dict[panel_manu][panel_name][panel_serial]["Voc"])*1.1))
        self.min_panels_string = round(float(inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Vmin"])/float(panel_dict[panel_manu][panel_name][panel_serial]["Voc"]))
        self.max_total_panels = str(math.floor(int(inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Pdcmax"])/int(panel_dict[panel_manu][panel_name][panel_serial]["P"])))
        self.max_panels_cec = str(math.floor((float(inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["P"])*1000)/(float(panel_dict[panel_manu][panel_name][panel_serial]["P"])*constants.STC_AC_DC_LIMIT)))

        #Places the result on the Canvas
        lbl_min_stringA = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
        lbl_min_stringB = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
        self.inv.create_window(self.delta_x+420,constants.HEIGHT_STRING_MPPTA_STRING_PGLAYOUT,window=lbl_min_stringA)
        self.inv.create_window(self.delta_x+420,constants.HEIGHT_STRING_MPPTB_STRING_PGLAYOUT,window=lbl_min_stringB)


        #Places other inverter specific limits
        lbl_mppt_a = ttk.Label(self.inv, text="Input: "+ inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Mppt_a_input"] + " - Imax: "+ inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Mppt_a_i_max"])
        self.inv.create_window(self.delta_x+130,120,window=lbl_mppt_a)
        lbl_mppt_b = ttk.Label(self.inv, text="Input: "+ inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Mppt_b_input"] + " - Imax: "+ inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Mppt_b_i_max"])
        self.inv.create_window(self.delta_x+130,221,window=lbl_mppt_b)
        lbl_max_cec = ttk.Label(self.inv, text="Total max number of panels (" + str(constants.STC_AC_DC_LIMIT*100)+ "% AC/DC min ratio, CEC design guidelines 9.4) = " + self.max_panels_cec)
        self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/2,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT,window=lbl_max_cec)
        lbl_max_tot = ttk.Label(self.inv, text="Total max number of panels (Maximum Input DC Power) = " + self.max_total_panels )
        self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/2,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT+20,window=lbl_max_tot)


        #And finaly loads details from save file ( "" if new job)
        self.ent_mppt_a_1.delete(0,'end')
        self.ent_mppt_a_1.insert(0,job_dict["jobSetup"]["mpptA1"])
        self.ent_mppt_b_1.delete(0,'end')
        self.ent_mppt_b_1.insert(0,job_dict["jobSetup"]["mpptB1"])
        if job_dict["jobSetup"]["mpptA2"] != "":
            self.ent_mppt_a_2.delete(0,'end')
            self.ent_mppt_a_2.insert(0,job_dict["jobSetup"]["mpptA2"])
            self.add_string_mpptA()
            #if job_dict["jobSetup"]["mpptA3"] != "":
                #self.ent_mppt_a_3.delete(0,'end')
                #self.ent_mppt_a_3.insert(0,job_dict["jobSetup"]["mpptA2"])
                #self.add_string_mpptA()
        if job_dict["jobSetup"]["mpptB2"] != "":
            self.ent_mppt_b_2.delete(0,'end')
            self.ent_mppt_b_2.insert(0,job_dict["jobSetup"]["mpptB2"])
            self.add_string_mpptB()
            #if job_dict["jobSetup"]["mpptB3"] != "":
                #self.ent_mppt_b_3.delete(0,'end')
                #self.ent_mppt_b_3.insert(0,job_dict["jobSetup"]["mpptA2"])
                #self.add_string_mpptB()

class PageSolarEdge(Page):
   def __init__(self, *args, **kwargs,):
       Page.__init__(self, *args, **kwargs)
       self.inv= tk.Canvas(self, width=constants.WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT, height=600,highlightthickness=0)#highlightthickness set to 0 to eliminate gap, width and height set bigger than window

       self.title_layout = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Titles/LayoutTitle.png")

       lbl_title1 = ttk.Label(self, image = self.title_layout)
       lbl_title1.grid(row = 1 ,column=1)

       #This section centers the canvas
       if (constants.WINDOW_SIZE_X-constants.WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT) > 0:
           self.centered_canvas_x = (constants.WINDOW_SIZE_X-constants.WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT)/2
           self.delta_x=(constants.WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT-450)/2#450 is the measured size of drawing
       else:
           slef.centered_canvas_x = 0
           self.delta_x=0

       if (constants.WINDOW_SIZE_Y-constants.HEIGHT_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT) > 0:#530 is the measured size of drawing
           centered_canvas_y = (constants.WINDOW_SIZE_Y-constants.HEIGHT_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT)/2
       else:
           centered_canvas_y = 0

       self.inv.grid(row=2,columnspan=4,sticky="nsew", padx=self.centered_canvas_x,pady=centered_canvas_y)

       #Manually drawing the inverter and string schematics
       #Inverter
       self.inv.create_line(self.delta_x+10, 100 ,self.delta_x+60, 100)
       self.inv.create_line(self.delta_x+10, 100 ,self.delta_x+10, 250)
       self.inv.create_line(self.delta_x+60, 100,self.delta_x+60, 250)
       self.inv.create_line(self.delta_x+10, 250,self.delta_x+60, 250)
       self.inv.create_line(self.delta_x+10, 100,self.delta_x+60, 250)
       #String1
       self.inv.create_line(self.delta_x+60, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT,self.delta_x+300, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT)
       self.ent_string_1 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(self.delta_x+300,constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT,window=self.ent_string_1)
       self.ent_string_2 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.ent_string_3 = ttk.Entry(self.inv,width =4,style="my.TEntry")

       #Section for dinamicaly adding strings
       self.butt_add_string_mpptA = ttk.Button(self, text="+", command=self.add_string_mpptA,style='my.TButton',width=1)
       self.inv.create_window(self.delta_x+500, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT,window=self.butt_add_string_mpptA)
       self.butt_remove_string_mpptA = ttk.Button(self, text="-", command=self.remove_string_mpptA,style='my.TButton',width=1)
       self.number_string_mpptA=1

       self.butt_datasheet_inv = ttk.Button(self, text="Inverter Datasheet Link", command=self.datasheet_inv,style='my.TButton')
       self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT/2 -150,400,window=self.butt_datasheet_inv)
       self.butt_datasheet_panel = ttk.Button(self, text="Panel Datasheet Link", command=self.datasheet_panel,style='my.TButton')
       self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT/2 +150,400,window=self.butt_datasheet_panel)


   def add_string_mpptA(self,*args):
        if self.number_string_mpptA == 1:
            self.number_string_mpptA = 2
            self.mpptA2_p1=self.inv.create_line(self.delta_x+220, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+220, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT)
            self.mpptA2_p2=self.inv.create_line(self.delta_x+220, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+300, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT)
            self.mpptA2_p3=self.inv.create_window(self.delta_x+300,constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT,window=self.ent_string_2)
            lbl_min_stringA2 = ttk.Label(self.inv, text="Max per string = "+str(self.max_panels_string))
            self.mpptA2_p4=self.inv.create_window(self.delta_x+390,constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-constants.SPACING_MPPTS_STRING_PGLAYOUT,window=lbl_min_stringA2)
            self.butt_minus_mpptA = self.inv.create_window(self.delta_x+550, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT,window=self.butt_remove_string_mpptA)
        elif self.number_string_mpptA == 2:
            self.number_string_mpptA = 3
            self.mpptA3_p1=self.inv.create_line(self.delta_x+200, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+200, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT)
            self.mpptA3_p2=self.inv.create_line(self.delta_x+200, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT,self.delta_x+300, constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT)
            self.mpptA3_p3=self.inv.create_window(self.delta_x+300,constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT,window=self.ent_string_3)
            lbl_min_stringA3 = ttk.Label(self.inv, text="Max per string = "+str(self.max_panels_string))
            self.mpptA3_p4=self.inv.create_window(self.delta_x+390,constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT-2*constants.SPACING_MPPTS_STRING_PGLAYOUT,window=lbl_min_stringA3)
        elif self.number_string_mpptA == 3:
            tk.messagebox.showwarning("Warning","Sorry, at the moment 4 parrallel strings are not supported on SSD")

   def remove_string_mpptA(self,*args):
        if self.number_string_mpptA == 2:
            self.number_string_mpptA = 1
            self.inv.delete(self.mpptA2_p1)
            self.inv.delete(self.mpptA2_p2)
            self.inv.delete(self.mpptA2_p3)
            self.inv.delete(self.mpptA2_p4)
            self.inv.delete(self.butt_minus_mpptA)
            self.ent_string_2.delete(0,"end")
        elif self.number_string_mpptA == 3:
            self.number_string_mpptA = 2
            self.inv.delete(self.mpptA3_p1)
            self.inv.delete(self.mpptA3_p2)
            self.inv.delete(self.mpptA3_p3)
            self.inv.delete(self.mpptA3_p4)
            self.ent_string_3.delete(0,"end")


   def datasheet_inv(self,*args):
        inv_type=self.job_dict["jobComponents"]["invType"]
        inv_manufacturer=self.job_dict["jobComponents"]["invManufacturer"]
        inv_model=self.job_dict["jobComponents"]["invModel"]
        inv_serial=self.job_dict["jobComponents"]["invSerial"]
        url = self.inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Url"]
        webbrowser.open(url)

   def datasheet_panel(self,*args):
        panel_manufacturer=self.job_dict["jobComponents"]["panelManufacturer"]
        panel_model=self.job_dict["jobComponents"]["panelModel"]
        panel_serial=self.job_dict["jobComponents"]["panelSerial"]
        url = self.panel_dict[panel_manufacturer][panel_model][panel_serial]["Url"]
        webbrowser.open(url)

   def submit_inv_setup(self,job_dict,inv_dict):
       inv_model= job_dict["jobComponents"]["invModel"]
       job_dict["jobSetup"]["mpptA1"] = self.ent_string_1.get()
       job_dict["jobSetup"]["mpptA2"] = self.ent_string_2.get()
       job_dict["jobSetup"]["mpptA3"] = self.ent_string_3.get()

   def show_limits(self,job_dict,inv_dict,panel_dict):#shows the min and max number of panels in a String
        #list of parameters used to calculate the max and min number of panels
        #in a string (improves readability)
        panel_manu = job_dict["jobComponents"]["panelManufacturer"]
        panel_name = job_dict["jobComponents"]["panelModel"]
        panel_serial = job_dict["jobComponents"]["panelSerial"]
        inv_type = job_dict["jobComponents"]["invType"]
        inv_serial = job_dict["jobComponents"]["invSerial"]
        inv_manufacturer = job_dict["jobComponents"]["invManufacturer"]
        inv_model = job_dict["jobComponents"]["invModel"]

        #Calulates the min and max panels (note diff round and floor)
        self.max_panels_string = math.floor(float(inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["PmaxString"])/(float(panel_dict[panel_manu][panel_name][panel_serial]["P"])))
        self.max_total_panels = str(math.floor(int(inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["Pdcmax"])/int(panel_dict[panel_manu][panel_name][panel_serial]["P"])))
        self.max_panels_cec = str(math.floor((float(inv_dict[inv_type][inv_manufacturer][inv_model][inv_serial]["P"])*1000)/(float(panel_dict[panel_manu][panel_name][panel_serial]["P"])*constants.STC_AC_DC_LIMIT)))

        #Places the labels on screen
        lbl_min_string1 = ttk.Label(self.inv, text="Max per string = "+str(self.max_panels_string))
        self.inv.create_window(self.delta_x+390,constants.HEIGHT_STRING_SOLAREDGE_PGLAYOUT,window=lbl_min_string1)

        lbl_max_cec = ttk.Label(self.inv, text="Total max number of panels (" + str(constants.STC_AC_DC_LIMIT*100)+ "% AC/DC min ratio, CEC design guidelines 9.4) = " + self.max_panels_cec)
        self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT/2,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT,window=lbl_max_cec)
        lbl_max_tot = ttk.Label(self.inv, text="Total max number of panels (Maximum Input DC Power) = " + self.max_total_panels )
        self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_SOLAREDGE_PGLAYOUT/2,constants.HEIGHT_BOTTOM_TEXT_STRING_PGLAYOUT+20,window=lbl_max_tot)

        inv_model= job_dict["jobComponents"]["invModel"]
        #And finaly loads details from save file ( "" if new job)
        self.ent_string_1.delete(0, 'end')
        self.ent_string_1.insert(0,job_dict["jobSetup"]["mpptA1"])
        if job_dict["jobSetup"]["mpptA2"] != "":
            self.ent_string_2.delete(0, 'end')
            self.ent_string_2.insert(0,job_dict["jobSetup"]["mpptA2"])
            self.add_string_mpptA()
            if job_dict["jobSetup"]["mpptA3"] != "":
                self.ent_string_3.delete(0, 'end')
                self.ent_string_3.insert(0,job_dict["jobSetup"]["mpptA3"])
                self.add_string_mpptA()


class PageSonnen(Page):
   def __init__(self, *args, **kwargs,):
       Page.__init__(self, *args, **kwargs)
       self.inv= tk.Canvas(self, width=600, height=600, highlightthickness=0, bg='#ececec')
       #highlightthickness set to 0 to eliminate gap, width and height set bigger than window

       #Manually drawing the inverter and string schematics
       self.inv.create_line(10, 100 ,60, 100)
       self.inv.create_line(10, 100 ,10, 250)
       self.inv.create_line(60, 100,60, 250)
       self.inv.create_line(10, 250,60, 250)
       self.inv.create_line(10, 100,60, 250)
       self.inv.create_line(60, 130,300, 130)
       self.inv.create_line(60, 220,300, 220)

       #Adding the title and string entries
       lbl_title = ttk.Label(self.inv, text="Layout",font='Helvetica 14 bold')
       self.inv.create_window(270,30,window=lbl_title)
       self.ent_mppt_a_1 = ttk.Entry(self.inv,width =10,style="my.TEntry")
       self.inv.create_window(300,130,window=self.ent_mppt_a_1)
       self.ent_mppt_b_1 = ttk.Entry(self.inv,width =10,style="my.TEntry")
       self.inv.create_window(300,220,window=self.ent_mppt_b_1)
       self.inv.pack(side="top",fill="both", expand=True)

       self.butt_datasheet_inv = ttk.Button(self, text="Inverter Datasheet Link", command=self.datasheet_inv,style='my.TButton')
       self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/2 -150,400,window=self.butt_datasheet_inv)
       self.butt_datasheet_panel = ttk.Button(self, text="Panel Datasheet Link", command=self.datasheet_panel,style='my.TButton')
       self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/2 +150,400,window=self.butt_datasheet_panel)

   def datasheet_inv(self,*args):
        inv_type=self.job_dict["jobComponents"]["invType"]
        inv_manufacturer=self.job_dict["jobComponents"]["invManufacturer"]
        inv_model=self.job_dict["jobComponents"]["invModel"]
        url = self.inv_dict[inv_type][inv_manufacturer][inv_model]["Url"]
        webbrowser.open(url)


   def datasheet_panel(self,*args):
        panel_manufacturer=self.job_dict["jobComponents"]["panelManufacturer"]
        panel_model=self.job_dict["jobComponents"]["panelModel"]
        url = self.panel_dict[panel_manufacturer][panel_model]["Url"]
        webbrowser.open(url)

   def submit_inv_setup(self,job_dict):
       job_dict["jobSetup"]["mpptA1"] = self.ent_mppt_a_1.get()
       job_dict["jobSetup"]["mpptB1"] = self.ent_mppt_b_1.get()

   def show_limits(self,inv_dict,job_dict,panel_dict): # also loads saved data (end)

       #list of parameters used to calculate the max and min number of panels
       #in a string (improves readability)
       panel_manu = job_dict["jobComponents"]["panelManufacturer"]
       panel_name = job_dict["jobComponents"]["panelModel"]
       inv_manufacturer = job_dict["jobComponents"]["invManufacturer"]
       inv_type = job_dict["jobComponents"]["invType"]
       inv_model = job_dict["jobComponents"]["invModel"]

       #Calulates the min and max panels (note diff round and floor)
       max_panels_string = math.floor(float(inv_dict[inv_type][inv_manufacturer][inv_model]["Vmax"])/(float(panel_dict[panel_manu][panel_name]["Voc"])*1.1))
       min_panels_string = round(float(inv_dict[inv_type][inv_manufacturer][inv_model]["Vmin"])/float(panel_dict[panel_manu][panel_name]["Voc"]))

       #Places the result on the Canvas
       lbl_min_string1 = ttk.Label(self.inv, text="Min & Max in a string = "+str(min_panels_string)+" - "+str(max_panels_string))
       self.inv.create_window(450,130,window=lbl_min_string1)
       lbl_min_string2 = ttk.Label(self.inv, text="Min & Max in a string = "+str(min_panels_string)+" - "+str(max_panels_string))
       self.inv.create_window(450,220,window=lbl_min_string2)

       #Places other inverter specific limits
       lbl_mppt_a = ttk.Label(self.inv, text="Input: "+ inv_dict["Hybrid"]["Sonnen"][inv_model]["Mppt_a_input"] + " - Imax: "+ inv_dict["Hybrid"]["Sonnen"][inv_model]["Mppt_a_i_max"])
       self.inv.create_window(150,110,window=lbl_mppt_a)
       lbl_mppt_b = ttk.Label(self.inv, text="Input: "+ inv_dict["Hybrid"]["Sonnen"][inv_model]["Mppt_b_input"] + " - Imax: "+ inv_dict["Hybrid"]["Sonnen"][inv_model]["Mppt_b_i_max"])
       self.inv.create_window(150,200,window=lbl_mppt_b)

       #And finaly loads details from save file ( "" if new job)
       self.ent_mppt_a_1.insert(0,job_dict["jobSetup"]["mpptA1"])
       self.ent_mppt_b_1.insert(0,job_dict["jobSetup"]["mpptB1"])

class PageEnphase(Page):
   def __init__(self, *args, **kwargs,):
       Page.__init__(self, *args, **kwargs)
       self.inv= tk.Canvas(self, width=600, height=600, highlightthickness=0, bg='#ececec')
       #highlightthickness set to 0 to eliminate gap, width and height set bigger than window

       lbl_title = ttk.Label(self.inv, text="Layout",font='Helvetica 14 bold')
       self.inv.create_window(270,30,window=lbl_title)

       self.ent_string1_l1 = ttk.Entry(self.inv,width =5,style="my.TEntry")
       self.ent_string1_l2 = ttk.Entry(self.inv,width =5,style="my.TEntry")
       self.ent_string1_l3 = ttk.Entry(self.inv,width =5,style="my.TEntry")
       self.ent_string2_l1 = ttk.Entry(self.inv,width =5,style="my.TEntry")
       self.ent_string2_l2 = ttk.Entry(self.inv,width =5,style="my.TEntry")
       self.ent_string2_l3 = ttk.Entry(self.inv,width =5,style="my.TEntry")

       self.butt_datasheet_inv = ttk.Button(self, text="Inverter Datasheet Link", command=self.datasheet_inv,style='my.TButton')
       self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/2 -150,400,window=self.butt_datasheet_inv)
       self.butt_datasheet_panel = ttk.Button(self, text="Panel Datasheet Link", command=self.datasheet_panel,style='my.TButton')
       self.inv.create_window(constants.WIDTH_CANVAS_LAYOUT_STRING_PGLAYOUT/2 +150,400,window=self.butt_datasheet_panel)

   def datasheet_inv(self,*args):
        inv_type=self.job_dict["jobComponents"]["invType"]
        inv_manufacturer=self.job_dict["jobComponents"]["invManufacturer"]
        inv_model=self.job_dict["jobComponents"]["invModel"]
        url = self.inv_dict[inv_type][inv_manufacturer][inv_model]["Url"]
        webbrowser.open(url)


   def datasheet_panel(self,*args):
        panel_manufacturer=self.job_dict["jobComponents"]["panelManufacturer"]
        panel_model=self.job_dict["jobComponents"]["panelModel"]
        url = self.panel_dict[panel_manufacturer][panel_model]["Url"]
        webbrowser.open(url)

   def show_layout(self,job_dict):

       #String 1
       lbl_string1 = ttk.Label(self.inv, text="String 1")
       self.inv.create_window(40,200,window=lbl_string1)
       self.inv.create_line(50, 200 ,120, 200)
       self.inv.create_line(120, 130 ,120, 270)
       self.inv.create_line(120, 130 ,200, 130)
       self.inv.create_line(120, 200 ,200, 200)
       self.inv.create_line(120, 270 ,200, 270)
       self.inv.create_window(210,200,window=self.ent_string1_l2)


       if job_dict["jobExtra"]["gateway"]==0:
           #String 2
           lbl_string1 = ttk.Label(self.inv, text="String 2")
           self.inv.create_window(290,200,window=lbl_string1)
           self.inv.create_line(300, 200 ,450, 200)
           self.inv.create_line(370, 130 ,370, 270)
           self.inv.create_line(370, 130 ,450, 130)
           self.inv.create_line(370, 200 ,450, 200)
           self.inv.create_line(370, 270 ,450, 270)
           self.inv.create_window(470,200,window=self.ent_string2_l2)

       if job_dict["setupEnphase"]["qrelay"] != "1" and job_dict["jobInfo"]["numMsbPhases"] == "3": # if 3P qrelay selected
           self.inv.create_window(210,130,window=self.ent_string1_l1)
           self.inv.create_window(210,270,window=self.ent_string1_l3)
           if job_dict["jobExtra"]["gateway"]==0:
               self.inv.create_window(470,130,window=self.ent_string2_l1)
               self.inv.create_window(470,270,window=self.ent_string2_l3)

       #For loading existing projects:
       self.ent_string1_l1.insert(0,job_dict["setupEnphase"]["string1L1"])
       self.ent_string1_l2.insert(0,job_dict["setupEnphase"]["string1L2"])
       self.ent_string1_l3.insert(0,job_dict["setupEnphase"]["string1L3"])
       self.ent_string2_l1.insert(0,job_dict["setupEnphase"]["string2L1"])
       self.ent_string2_l2.insert(0,job_dict["setupEnphase"]["string2L2"])
       self.ent_string2_l3.insert(0,job_dict["setupEnphase"]["string2L3"])

       self.inv.pack(side="top",fill="both", expand=True)

   def submit_inv_setup(self,job_dict):
       job_dict["setupEnphase"]["string1L1"] = self.ent_string1_l1.get()
       job_dict["setupEnphase"]["string1L2"] = self.ent_string1_l2.get()
       job_dict["setupEnphase"]["string1L3"] = self.ent_string1_l3.get()
       if job_dict["jobExtra"]["gateway"] != "1":
           job_dict["setupEnphase"]["string2L1"] = self.ent_string2_l1.get()
           job_dict["setupEnphase"]["string2L2"] = self.ent_string2_l2.get()
           job_dict["setupEnphase"]["string2L3"] = self.ent_string2_l3.get()
