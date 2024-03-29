import tkinter as tk
from tkinter import filedialog




from gui.save_manager import save_job,load_user_pref,save_user_pref
from gui.pages.page_info import PageInfo
from gui.pages.page_vrise import PageVrise
from gui.pages.page_layout import PageString,PageSonnen,PageSolarEdge,PageEnphase
from gui.pages.pop_up_pages import ConfigBlockDiag, ConfigVrise
from gui.pages.page_settings import SettingsPage


from databases.my_dictionaries import job_dict,empty_job_dict,batt_dict
from databases.inverter_dictionaries import inv_dict
from databases.panel_dictionaries import panel_dict
import databases.constants as constants

from excel.run_excel import print_string_inverter,print_hybrid_inverter,print_enphase_inverter,print_gateway


class MainViewSld(tk.Frame):
    def __init__(self,*args, **kwargs):
        tk.Frame.__init__(self, **kwargs,bg=constants.set_baground_for_theme())

        #Variables
        self.current_page = 1 # for navigating between pages
        self.var_save = 0 #for making sure user saves before going bacvk to menu

        #Initilising the 2 frames ( 1 for pages 1 for buttons)
        self.buttonframe = tk.Frame(self,bg=constants.set_baground_for_theme())
        self.container = tk.Frame(self,bg=constants.set_baground_for_theme())
        self.buttonframe.pack(side="bottom", fill="x", expand=False)
        self.container.pack(side="bottom", fill="both", expand=True)

        self.right_arrow_image = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Buttons/RightButt.png")
        self.left_arrow_image = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Buttons/LeftButt.png")
        self.menu_image = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Buttons/MenuButt.png")
        self.settings_image = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Buttons/SettButt.png")
        self.save_image = tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Buttons/SaveButt.png")

        #All the pages we initialize - maybe could improve p3
        self.page_info = PageInfo(self)
        self.page_layout_string = PageString(self)
        self.page_layout_sonnen = PageSonnen(self)
        self.page_layout_solaredge = PageSolarEdge(self)
        self.page_layout_enphase= PageEnphase(self)
        self.page_info.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.page_layout_string.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.page_layout_sonnen.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.page_layout_solaredge.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.page_layout_enphase.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        self.create_ribbon_menu()

        #packing the next and previous buttons
        b1 = tk.Button(self.buttonframe,image=self.right_arrow_image, highlightthickness=0,bd=0, pady=0, padx=0, command=self.next_page)
        b1.pack(side="right", expand=True)
        b2 = tk.Button(self.buttonframe,image=self.left_arrow_image, command=self.previous_page,borderwidth=0)
        b2.pack(side="left", expand=True)
        b3 = tk.Button(self.buttonframe,image=self.settings_image, command=self.settings_page,borderwidth=0)
        b3.pack(side="left", expand=True)
        b4 = tk.Button(self.buttonframe,image=self.menu_image, command=self.exit_sld,borderwidth=0)
        b4.pack(side="left", expand=True)
        b5 = tk.Button(self.buttonframe,image=self.save_image, command=self.save_job_plus_current_page,borderwidth=0)
        b5.pack(side="right", expand=True)


        #Initialising page 1
        self.job_dict = job_dict
        self.page_info.show_entries(self.job_dict,panel_dict,inv_dict,batt_dict) #function that setup the user friendly entry form (empty) on page 1
        self.page_info.lift() #puts page 1 on top of the stack

        self.user_pref = load_user_pref()#loads the stored user preferences from user_prefs.txt



    def next_page(self,*args):
        #if args == 2:
            #self.current_page = args
        if self.current_page == 3:
            if self.user_pref["Paths"]["outputSld"] == "":
                output_loc= filedialog.askdirectory(title = "Select s location to output the SLD and Vrise pdfs",initialdir = "/Users")
                self.user_pref["Paths"]["outputSld"] = output_loc
                save_user_pref(self.user_pref)
                self.next_page()
            t = "good"
            if self.job_dict["jobComponents"]["invManufacturer"] == "Sonnen":
                self.page_layout_sonnen.submit_inv_setup(self.job_dict)
                print_hybrid_inverter(self.job_dict,panel_dict,inv_dict)
            elif self.job_dict["jobComponents"]["invManufacturer"] == "SolarEdge":
                self.page_layout_solaredge.submit_inv_setup(self.job_dict,inv_dict)
                if self.job_dict["jobExtra"]["gateway"]==1:
                    print_gateway(self.job_dict,panel_dict,inv_dict)
                else:
                    print_string_inverter(self.job_dict,panel_dict,inv_dict)
            elif self.job_dict["jobComponents"]["invManufacturer"] == "Enphase":
                self.page_layout_enphase.submit_inv_setup(self.job_dict)
                if self.job_dict["jobExtra"]["gateway"]==0:
                    print_enphase_inverter(self.job_dict,panel_dict,inv_dict)
                elif self.job_dict["jobExtra"]["gateway"]==1:
                    print_gateway(self.job_dict,panel_dict,inv_dict)
            else:
                t=self.page_layout_string.submit_inv_setup(self.job_dict)
                if t=="rollback":
                    self.current_page = 2
                    self.next_page()
                elif self.job_dict["jobExtra"]["gateway"]==0:
                    print_string_inverter(self.job_dict,panel_dict,inv_dict)
                elif self.job_dict["jobExtra"]["gateway"]==1:
                    print_gateway(self.job_dict,panel_dict,inv_dict)
            save_job(self.job_dict)
            if t != "rollback":
                self.destroy()#Closes tkinter window

        if self.current_page == 2:

            self.current_page = 3
            if self.page_v_rise.submit_Vrise(self.job_dict) == True: #If no problem with the Vrise page
                if self.job_dict["jobComponents"]["invManufacturer"] == "Sonnen":
                    self.page_layout_sonnen.lift()
                    self.page_layout_sonnen.show_limits(inv_dict,self.job_dict,panel_dict)
                elif self.job_dict["jobComponents"]["invManufacturer"] == "SolarEdge":
                    self.page_layout_solaredge.lift()
                    self.page_layout_solaredge.show_limits(self.job_dict,inv_dict,panel_dict)
                elif self.job_dict["jobComponents"]["invManufacturer"] == "Enphase":
                    self.page_layout_enphase.lift()
                    self.page_layout_enphase.show_layout(self.job_dict)
                else:
                    self.page_layout_string.lift()
                    self.page_layout_string.show_limits(inv_dict,self.job_dict,panel_dict)
            else:  #If problem with the Vrise page
                self.current_page=2



        if self.current_page == 1:

            self.current_page = 2
            self.job_dict = self.page_info.submit_job_info()
            if self.job_dict == "rollback":
                self.current_page = 1
            else:
                self.page_v_rise = PageVrise(self)
                self.page_v_rise.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
                self.page_v_rise.lift()
                self.page_v_rise.show_entries(self.job_dict,self.user_pref,inv_dict)
                self.page_v_rise.fill_Vrise(self.job_dict,inv_dict,self.user_pref)



    def previous_page(self,*args):
        if self.current_page == 1:
            print("No previous pages")

        if self.current_page == 2:
            self.page_info.lift()
            self.current_page = 1

        if self.current_page == 3:
            # self.page_v_rise = PageVrise(self)
            # self.page_v_rise.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
            # self.page_v_rise.show_entries(self.job_dict,self.user_pref,inv_dict)
            # self.page_v_rise.fill_Vrise(self.job_dict,inv_dict,self.user_pref)
            self.page_v_rise.lift()
            self.current_page = 2

    def new_job(self,*args):
        self.job_dict=empty_job_dict
        self.current_page = 1
        self.page_info.delete_entries()
        self.page_info.show_entries(panel_dict,inv_dict,batt_dict) #function that setup the user friendly entry form (empty) on page 1
        self.page_info.insert_values(self.job_dict) #function that inputs information retrieved from the textffile
        self.page_info.lift()

    def fast_print(self,*args):
        self.save_job_plus_current_page()
        self.current_page = 3
        self.next_page()

    def create_ribbon_menu(self,*args):
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        top['menu'] = self.menuBar

        #The File menu
        self.subMenuFile = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label='File', menu=self.subMenuFile)
        self.subMenuFile.add_command(label='New',  accelerator="Command-N",command=self.new_job)
        self.subMenuFile.add_command(label='Save', accelerator="Command-S",command=self.save_job_plus_current_page)
        self.subMenuFile.add_command(label='Quit', command=self.exit_sld)
        self.subMenuFile.add_command(label='Print', accelerator="Command-P", command=self.fast_print)

        #The window menu
        self.subMenuWindow = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label='Window', menu=self.subMenuWindow)
        self.subMenuWindow.add_command(label='Full Screen View', command=self.full_screen_view)
        self.subMenuWindow.add_command(label='Window View', command=self.window_view)

        #The Advanced menu
        self.subMenuAdvanced = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label='Advanced', menu=self.subMenuAdvanced)
        self.subMenuAdvanced.add_command(label='Block Diagram', command= self.call_config_block_diag)
        self.subMenuAdvanced.add_command(label='Voltage Rise Settings', command= self.call_config_Vrise)

        #The help menu
        self.subMenuHelp = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label='Help', menu=self.subMenuHelp)
        self.subMenuHelp.add_command(label='About')


        #List of all bindings
        self.bind("<Meta_L><n>", self.new_job)
        self.bind("<Meta_L><p>", self.fast_print)
        self.bind("<Meta_L><s>", self.save_job_plus_current_page)


    def settings_page(self,*args):
        settings = SettingsPage(self)
        settings.passing_arguments(self.user_pref,self.job_dict)

    def save_job_plus_current_page(self,*args):
        self.var_save = 1
        if self.current_page == 1:
            self.job_dict=self.page_info.submit_job_info()
        elif self.current_page == 2:
            self.page_v_rise.submit_Vrise(self.job_dict)
        elif self.current_page == 3:
            if self.job_dict["jobComponents"]["invManufacturer"] == "Sonnen":
                self.page_layout_sonnen.submit_inv_setup(self.job_dict)
            elif self.job_dict["jobComponents"]["invManufacturer"] == "SolarEdge":
                self.page_layout_solaredge.submit_inv_setup(self.job_dict,inv_dict)
            elif self.job_dict["jobComponents"]["invManufacturer"] == "Enphase":
                self.page_layout_enphase.submit_inv_setup(self.job_dict)
            else:
                t=self.page_layout_string.submit_inv_setup(self.job_dict)
        save_job(self.job_dict)

    def call_config_block_diag(self,*args): #Rest of the code in pop-up pages
        bd = ConfigBlockDiag(self)
        bd.show_layout(self.job_dict,self.user_pref)

    def call_config_Vrise(self,*args): #Rest of the code in pop-up pages
        vr = ConfigVrise(self)
        vr.show_layout(self.user_pref)

    def window_view(self,*args):
        self.wm_geometry("550x500+%d+%d" % (self.x_offset,self.y_offset))

    def full_screen_view(self,*args):
        #getting screen width and height of display
        width= self.winfo_screenwidth()
        height= self.winfo_screenheight()
        #saving the current windowed position for when the user wants to revert
        self.x_offset = self.winfo_x()
        self.y_offset = self.winfo_y()
        #setting tkinter window size
        self.geometry("%dx%d+0+0" % (width, height))

    def exit_sld(self,*args):
        if self.var_save == 0:
            MsgBox = tk.messagebox.askquestion (parent= self,title='Quit SLD',message='The job you are currently editing has not been saved. Are you sure you want to quit without saving?',icon = 'warning')
            if MsgBox == 'yes':
               self.destroy()
            else:
               pass
        else:
            self.destroy()
