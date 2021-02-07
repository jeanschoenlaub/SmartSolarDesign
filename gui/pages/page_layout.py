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
       self.inv= tk.Canvas(self, width=750, height=600, highlightthickness=0)#highlightthickness set to 0 to eliminate gap, width and height set bigger than window
       #Starts by setting canvas in middle
       if (constants.WINDOW_SIZE_X-constants.LAYOUT_STRING_WIDTH_PGLAYOUT) > 0:#530 is the measured size of drawing
           centered_canvas_x = (constants.WINDOW_SIZE_X-constants.LAYOUT_STRING_WIDTH_PGLAYOUT)/2
       else:
           centered_canvas_x = (constants.WINDOW_SIZE_X-constants.LAYOUT_STRING_WIDTH_PGLAYOUT)/2
       if (constants.WINDOW_SIZE_Y-constants.LAYOUT_STRING_HEIGHT_PGLAYOUT) > 0:#530 is the measured size of drawing
           centered_canvas_y = (constants.WINDOW_SIZE_Y-constants.LAYOUT_STRING_HEIGHT_PGLAYOUT)/2
       else:
           centered_canvas_y = (constants.WINDOW_SIZE_Y-constants.LAYOUT_STRING_HEIGHT_PGLAYOUT)/2
       self.inv.grid(row=0,columnspan=4,sticky="nsew", padx=centered_canvas_x,pady=centered_canvas_y)

       #Manually drawing the inverter and string schematics
       #Inverter
       self.inv.create_line(10, 100 ,60, 100)
       self.inv.create_line(10, 100 ,10, 250)
       self.inv.create_line(60, 100,60, 250)
       self.inv.create_line(10, 250,60, 250)
       self.inv.create_line(10, 100,60, 250)
       #mpptA2
       self.inv.create_line(200, 80,200, 130)
       self.inv.create_line(200, 80,300, 80)
       self.ent_mppt_a_2 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(300,80,window=self.ent_mppt_a_2)
       #mpptA1
       self.inv.create_line(60, 130,300, 130)
       self.ent_mppt_a_1 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(300,130,window=self.ent_mppt_a_1)
       #mpptB1
       self.inv.create_line(60, 210,300, 210)
       self.ent_mppt_b_1 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(300,210,window=self.ent_mppt_b_1)
       #mpptB2
       self.inv.create_line(200, 210 ,200, 260)
       self.inv.create_line(200, 260,300, 260)
       self.ent_mppt_b_2 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(300,260,window=self.ent_mppt_b_2)

       #Adding the title
       lbl_title = ttk.Label(self.inv, text="Layout",font='Helvetica 16 bold',)
       self.inv.create_window(constants.LAYOUT_STRING_WIDTH_PGLAYOUT/2,constants.Y_POS_CANV_TITLE_PGLAYOUT,window=lbl_title)

   def submit_inv_setup(self,job_dict): #Called when next paged is pressed
       error_parra_string = True
       if self.ent_mppt_a_2.get() != "" and self.ent_mppt_a_1.get()=="":
           error_parra_string=tk.messagebox.askyesno("Layout Error","You have inputed a parrallel string, but the main string is empty, are you sure you want to continue ?",icon="warning")
       elif self.ent_mppt_a_2.get() != self.ent_mppt_a_1.get() and self.ent_mppt_a_2.get() != "":
           error_parra_string=tk.messagebox.askyesno("Layout Error","You have inputed parrallel strings of different lenghts, are you sure you want to continue ?",icon="warning")


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
        inv_type = job_dict["jobComponents"]["invType"]
        inv_manufacturer = job_dict["jobComponents"]["invManufacturer"]
        inv_model = job_dict["jobComponents"]["invModel"]


        #Calulates the min and max panels (note diff round and floor)
        self.max_panels_string = math.floor(float(inv_dict[inv_type][inv_manufacturer][inv_model]["Vmax"])/(float(panel_dict[panel_manu][panel_name]["Voc"])*1.1))
        self.min_panels_string = round(float(inv_dict[inv_type][inv_manufacturer][inv_model]["Vmin"])/float(panel_dict[panel_manu][panel_name]["Voc"]))
        self.max_total_panels = str(math.floor(int(inv_dict[inv_type][inv_manufacturer][inv_model]["Pdcmax"])/int(panel_dict[panel_manu][panel_name]["P"])))
        self.max_panels_cec = str(math.floor((float(inv_dict[inv_type][inv_manufacturer][inv_model]["P"])*1000)/(float(panel_dict[panel_manu][panel_name]["P"])*constants.STC_AC_DC_LIMIT)))

        #Places the result on the Canvas
        lbl_min_string1 = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
        lbl_min_string2 = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
        lbl_min_string3 = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
        lbl_min_string4 = ttk.Label(self.inv, text="Min & Max per string = "+str(self.min_panels_string)+" - "+str(self.max_panels_string))
        self.inv.create_window(420,80,window=lbl_min_string1)
        self.inv.create_window(420,130,window=lbl_min_string2)
        self.inv.create_window(420,210,window=lbl_min_string3)
        self.inv.create_window(420,260,window=lbl_min_string4)

        #Places other inverter specific limits
        lbl_mppt_a = ttk.Label(self.inv, text="Input: "+ inv_dict[inv_type][inv_manufacturer][inv_model]["Mppt_a_input"] + " - Imax: "+ inv_dict[inv_type][inv_manufacturer][inv_model]["Mppt_a_i_max"])
        self.inv.create_window(130,120,window=lbl_mppt_a)
        lbl_mppt_b = ttk.Label(self.inv, text="Input: "+ inv_dict[inv_type][inv_manufacturer][inv_model]["Mppt_b_input"] + " - Imax: "+ inv_dict[inv_type][inv_manufacturer][inv_model]["Mppt_b_i_max"])
        self.inv.create_window(130,221,window=lbl_mppt_b)
        lbl_max_cec = ttk.Label(self.inv, text="Total max number of panels (" + str(constants.STC_AC_DC_LIMIT*100)+ "% AC inverter capacity of array DC max power - CEC design guidelines 9.4) = " + self.max_panels_cec)
        self.inv.create_window(constants.LAYOUT_STRING_WIDTH_PGLAYOUT/2,320,window=lbl_max_cec)
        lbl_max_tot = ttk.Label(self.inv, text="Total max number of panels (Maximum Input DC Power) = " + self.max_total_panels )
        self.inv.create_window(constants.LAYOUT_STRING_WIDTH_PGLAYOUT/2,340,window=lbl_max_tot)


        #And finaly loads details from save file ( "" if new job)
        self.ent_mppt_a_1.delete(0,'end')
        self.ent_mppt_a_1.insert(0,job_dict["jobSetup"]["mpptA1"])
        self.ent_mppt_a_2.delete(0,'end')
        self.ent_mppt_a_2.insert(0,job_dict["jobSetup"]["mpptA2"])
        self.ent_mppt_b_1.delete(0,'end')
        self.ent_mppt_b_1.insert(0,job_dict["jobSetup"]["mpptB1"])
        self.ent_mppt_b_2.delete(0,'end')
        self.ent_mppt_b_2.insert(0,job_dict["jobSetup"]["mpptB2"])

class PageSolarEdge(Page):
   def __init__(self, *args, **kwargs,):
       Page.__init__(self, *args, **kwargs)
       self.inv= tk.Canvas(self, width=constants.LAYOUT_SE_WIDTH_PGLAYOUT, height=600,highlightthickness=0, bg='#ececec')#highlightthickness set to 0 to eliminate gap, width and height set bigger than window
       self.inv.grid(row=0,columnspan=4,sticky="nsew")

       #Manually drawing the inverter and string schematics
       #Inverter
       self.inv.create_line(10, 100 ,60, 100)
       self.inv.create_line(10, 100 ,10, 250)
       self.inv.create_line(60, 100,60, 250)
       self.inv.create_line(10, 250,60, 250)
       self.inv.create_line(10, 100,60, 250)
       #Common part
       self.inv.create_line(60, 130,200, 130)
       self.inv.create_line(200, 100,200, 160)
       #String A
       self.inv.create_line(200, 100,300, 100)
       self.ent_string_1 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(300,100,window=self.ent_string_1)
       #String B
       self.inv.create_line(200, 160,300, 160)
       self.ent_string_2 = ttk.Entry(self.inv,width =4,style="my.TEntry")
       self.inv.create_window(300,160,window=self.ent_string_2)

       #Adding the title
       lbl_title = ttk.Label(self.inv, text="Layout",font='Helvetica 16 bold')
       self.inv.create_window(constants.WINDOW_SIZE_X/2,30,window=lbl_title)

   def submit_inv_setup(self,job_dict,inv_dict):
       inv_model= job_dict["jobComponents"]["invModel"]
       job_dict["jobSetup"]["mpptA1"] = self.ent_string_1.get()

       if inv_dict["String"]["SolarEdge"][inv_model]["Phases"] == "1":  # Condition so that 3P SE inverters use both mppt
           job_dict["jobSetup"]["mpptA2"] = self.ent_string_2.get()
       else:
           job_dict["jobSetup"]["mpptB1"] = self.ent_string_2.get()

   def show_limits(self,job_dict,inv_dict,panel_dict):#shows the min and max number of panels in a String
        #list of parameters used to calculate the max and min number of panels
        #in a string (improves readability)
        panel_manu = job_dict["jobComponents"]["panelManufacturer"]
        panel_name = job_dict["jobComponents"]["panelModel"]
        inv_type = job_dict["jobComponents"]["invType"]
        inv_manufacturer = job_dict["jobComponents"]["invManufacturer"]
        inv_model = job_dict["jobComponents"]["invModel"]

        #Calulates the min and max panels (note diff round and floor)
        self.max_panels_string = math.floor(float(inv_dict[inv_type][inv_manufacturer][inv_model]["PmaxString"])/(float(panel_dict[panel_manu][panel_name]["P"])))
        self.max_total_panels = str(math.floor(int(inv_dict[inv_type][inv_manufacturer][inv_model]["Pdcmax"])/int(panel_dict[panel_manu][panel_name]["P"])))
        self.max_panels_cec = str(math.floor((float(inv_dict[inv_type][inv_manufacturer][inv_model]["P"])*1000)/(float(panel_dict[panel_manu][panel_name]["P"])*constants.STC_AC_DC_LIMIT)))

        #Places the labels on screen
        lbl_min_string1 = ttk.Label(self.inv, text="Max per string = "+str(self.max_panels_string))
        self.inv.create_window(420,100,window=lbl_min_string1)
        lbl_min_string2 = ttk.Label(self.inv, text="Max per string = "+str(self.max_panels_string))
        self.inv.create_window(420,160,window=lbl_min_string2)
        lbl_max_cec = ttk.Label(self.inv, text="Total max number of panels (" + str(constants.STC_AC_DC_LIMIT*100)+ "% AC inverter capacity of array DC max power - CEC design guidelines 9.4) = " + self.max_panels_cec)
        self.inv.create_window(constants.LAYOUT_SE_WIDTH_PGLAYOUT/2,320,window=lbl_max_cec)
        lbl_max_tot = ttk.Label(self.inv, text="Total max number of panels (Maximum Input DC Power) = " + self.max_total_panels )
        self.inv.create_window(constants.LAYOUT_SE_WIDTH_PGLAYOUT/2,340,window=lbl_max_tot)

        #And finaly loads details from save file ( "" if new job)
        self.ent_string_1.delete(0, 'end')
        self.ent_string_2.delete(0, 'end')
        self.ent_string_1.insert(0,job_dict["jobSetup"]["mpptA1"])
        inv_model= job_dict["jobComponents"]["invModel"]
        if inv_dict["String"]["SolarEdge"][inv_model]["Phases"] == "1":  # Condition so that 3P SE inverters use both mppt
            self.ent_string_2.insert(0,job_dict["jobSetup"]["mpptA2"])
            job_dict["jobSetup"]["mpptB1"] = "" #Prevents a bug, should be useless with new dict
        else:
            self.ent_string_2.insert(0,job_dict["jobSetup"]["mpptB1"])
            job_dict["jobSetup"]["mpptA2"] = "" #Prevents a bug, should be useless with new dict

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
