import sys
import tkinter as tk
import tkinter.ttk as ttk
import math
from ttkthemes import ThemedStyle

from gui.save_manager import save_job,load_user_pref
from gui.pages.page_info import PageInfo
from gui.pages.page_vrise import PageVrise
from gui.pages.page_layout import PageString,PageSonnen,PageSolarEdge,PageEnphase
from gui.pages.pop_up_pages import ConfigBlockDiag, ConfigVrise

from databases.my_dictionaries import job_dict,empty_job_dict,batt_dict
from databases.inverter_dictionaries import inv_dict
from databases.panel_dictionaries import panel_dict

from excel.run_excel import print_string_inverter,print_hybrid_inverter,print_enphase_inverter,print_gateway

import databases.constants as constants

def check_arg(index):
    try:
        sys.argv[index]
    except IndexError:
        return False
    else:
        return True

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, **kwargs,bg=constants.set_baground_for_theme())

        #Variables
        self.current_page = 1 # for navigating between pages

        #Initilising the 2 frames ( 1 for pages 1 for buttons)
        buttonframe = tk.Frame(self,bg=constants.set_baground_for_theme())
        container = tk.Frame(self,bg=constants.set_baground_for_theme())
        buttonframe.pack(side="bottom", fill="x", expand=False)
        container.pack(side="bottom", fill="both", expand=True)

        #All the pages we initialize - maybe could improve p3
        self.page_info = PageInfo(self)
        self.page_v_rise = PageVrise(self)
        self.page_layout_string = PageString(self)
        self.page_layout_sonnen = PageSonnen(self)
        self.page_layout_solaredge = PageSolarEdge(self)
        self.page_layout_enphase= PageEnphase(self)
        self.page_info.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.page_v_rise.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.page_layout_string.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.page_layout_sonnen.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.page_layout_solaredge.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.page_layout_enphase.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.create_ribbon_menu()

        #packing the next and previous buttons
        s = ttk.Style()
        s.configure('my.TButton', font=('Arial', 14))
        style.configure("my.TEntry", background=constants.set_entries_background_for_darkmode())
        b1 = ttk.Button(buttonframe, text="Next", command=self.next_page).pack(side="right",padx=20)
        b2 = ttk.Button(buttonframe, text="Previous", command=self.previous_page,style='my.TButton').pack(side="left",padx=20)
        b3 = ttk.Button(buttonframe, text="Quit", command=self.exit_app,style='my.TButton').pack(side="left", expand=True)
        b3 = ttk.Button(buttonframe, text="Save", command=self.save_job_plus_current_page,style='my.TButton').pack(side="right", expand=True)


        #Initialising page 1
        self.page_info.show_entries(job_dict,panel_dict,inv_dict,batt_dict) #function that setup the user friendly entry form (empty) on page 1
        self.page_info.lift() #puts page 1 on top of the stack

        self.user_pref = load_user_pref()#loads the stored user preferences from user_prefs.txt

    def next_page(self,*args):
        #if args == 2:
            #self.current_page = args
        if self.current_page == 3:
            t = "good"
            if job_dict["jobComponents"]["invManufacturer"] == "Sonnen":
                self.page_layout_sonnen.submit_inv_setup(job_dict)
                print_hybrid_inverter(job_dict,panel_dict,inv_dict)
            elif job_dict["jobComponents"]["invManufacturer"] == "SolarEdge":
                self.page_layout_solaredge.submit_inv_setup(job_dict,inv_dict)
                if job_dict["jobExtra"]["gateway"]==1:
                    print_gateway(job_dict,panel_dict,inv_dict)
                else:
                    print_string_inverter(job_dict,panel_dict,inv_dict)
            elif job_dict["jobComponents"]["invManufacturer"] == "Enphase":
                self.page_layout_enphase.submit_inv_setup(job_dict)
                if job_dict["jobExtra"]["gateway"]==0:
                    print_enphase_inverter(job_dict,panel_dict,inv_dict)
                elif job_dict["jobExtra"]["gateway"]==1:
                    print_gateway(job_dict,panel_dict,inv_dict)
            else:
                t=self.page_layout_string.submit_inv_setup(job_dict)
                if t=="rollback":
                    self.current_page = 2
                    self.next_page()
                elif job_dict["jobExtra"]["gateway"]==0:
                    print_string_inverter(job_dict,panel_dict,inv_dict)
                elif job_dict["jobExtra"]["gateway"]==1:
                    print_gateway(job_dict,panel_dict,inv_dict)
            save_job(job_dict)
            if t != "rollback":
                root.destroy()#Closes tkinter window

        if self.current_page == 2:

            self.current_page = 3
            self.page_v_rise.submit_Vrise(job_dict)

            if job_dict["jobComponents"]["invManufacturer"] == "Sonnen":
                self.page_layout_sonnen.lift()
                self.page_layout_sonnen.show_limits(inv_dict,job_dict,panel_dict)
            elif job_dict["jobComponents"]["invManufacturer"] == "SolarEdge":
                self.page_layout_solaredge.lift()
                self.page_layout_solaredge.show_limits(job_dict,inv_dict,panel_dict)
            elif job_dict["jobComponents"]["invManufacturer"] == "Enphase":
                self.page_layout_enphase.lift()
                self.page_layout_enphase.show_layout(job_dict)
            else:
                self.page_layout_string.lift()
                self.page_layout_string.show_limits(inv_dict,job_dict,panel_dict)

        if self.current_page == 1:
            self.current_page = 2
            self.page_info.submit_job_info(job_dict)
            self.page_v_rise.lift()
            self.page_v_rise.show_entries()
            self.page_v_rise.fill_Vrise(job_dict,inv_dict,self.user_pref)



    def previous_page(self,*args):
        if self.current_page == 1:
            print("No previous pages")

        if self.current_page == 2:
            self.page_info.lift()
            self.current_page = 1

        if self.current_page == 3:
            self.page_v_rise.lift()
            self.current_page = 2

    def new_job(self,*args):
        job_dict=empty_job_dict
        self.current_page = 1
        self.page_info.delete_entries()
        self.page_info.show_entries(panel_dict,inv_dict,batt_dict) #function that setup the user friendly entry form (empty) on page 1
        self.page_info.insert_values(job_dict) #function that inputs information retrieved from the textffile
        self.page_info.lift()

    def fast_print(self,*args):
        self.current_page =3
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
        self.subMenuFile.add_command(label='Quit', command=self.exit_app)
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
        root.bind("<Meta_L><n>", self.new_job)
        root.bind("<Meta_L><p>", self.fast_print)
        root.bind("<Meta_L><s>", self.save_job_plus_current_page)

    def save_job_plus_current_page(self,*args):
        if self.current_page == 1:
            self.page_info.submit_job_info(job_dict)
        elif self.current_page == 2:
            self.page_v_rise.submit_Vrise(job_dict)
        elif self.current_page == 3:
            if job_dict["jobComponents"]["invManufacturer"] == "Sonnen":
                self.page_layout_sonnen.submit_inv_setup(job_dict)
            elif job_dict["jobComponents"]["invManufacturer"] == "SolarEdge":
                self.page_layout_solaredge.submit_inv_setup(job_dict,inv_dict)
            elif job_dict["jobComponents"]["invManufacturer"] == "Enphase":
                self.page_layout_enphase.submit_inv_setup(job_dict)
            else:
                t=self.page_layout_string.submit_inv_setup(job_dict)
        save_job(job_dict)

    def call_config_block_diag(self,*args): #Rest of the code in pop-up pages
        bd = ConfigBlockDiag(root)
        bd.show_layout(job_dict,self.user_pref)

    def call_config_Vrise(self,*args): #Rest of the code in pop-up pages
        vr = ConfigVrise(root)
        vr.show_layout(self.user_pref)

    def window_view(self,*args):
        root.wm_geometry("550x500+%d+%d" % (self.x_offset,self.y_offset))

    def full_screen_view(self,*args):
        #getting screen width and height of display
        width= root.winfo_screenwidth()
        height= root.winfo_screenheight()
        #saving the current windowed position for when the user wants to revert
        self.x_offset = root.winfo_x()
        self.y_offset = root.winfo_y()
        #setting tkinter window size
        root.geometry("%dx%d+0+0" % (width, height))

    def exit_app(self,*args):
        root.destroy()

if __name__ == "__main__":
    # Will returned the saved job if it exists, otherwise the value from get_txtfile_info
    root = tk.Tk(className=constants.APP_NAME)
    root.configure(bg=constants.set_baground_for_theme())

    root.option_add('*TCombobox*Listbox.selectBackground', 'yellow') # change highlight color
    root.option_add('*TCombobox*Listbox.selectForeground', 'black') # change text color
    root.option_add('*TCombobox*Listbox.fieldbackground', 'blue')

    #Setting the theme
    style = ThemedStyle(root)
    style.set_theme(constants.APP_THEME)

    #Initiliasing window container
    main = MainView(root)



    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry(str(constants.WINDOW_SIZE_X)+"x"+str(constants.WINDOW_SIZE_Y)+"+350+200")
    root.mainloop()
