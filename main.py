import sys
import tkinter as tk
import tkinter.ttk as ttk
import math
from ttkthemes import ThemedStyle
from tkinter import filedialog
from tkinter import messagebox


from gui.pages.master_sld import MainViewSld
from gui.pages.page_settings import SettingsPage
from gui.pages.page_account import AccountPage
from gui.save_manager import load_user_pref

import databases.constants as constants
from databases.my_dictionaries import empty_job_dict






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



        self.background_image=tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Backgrounds/BackgroundMenu.png")
        #self.background_label = tk.Label(self, image=self.background_image)
        #self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.canvas_menu = tk.Canvas(self, width=constants.WINDOW_SIZE_X, height=constants.WINDOW_SIZE_Y)
        self.canvas_menu.pack(side="top", anchor= "nw")
        self.canvas_menu.create_image(constants.WINDOW_SIZE_X/2, constants.WINDOW_SIZE_Y/2, image = self.background_image)

        #variables to make the interactive border work
        self.line_butt1_exists = 0
        self.line_butt2_exists = 0
        self.line_butt3_exists = 0
        self.line_butt4_exists = 0

        self.canvas_menu.bind("<Button-1>", self.mouse_function)
        self.canvas_menu.bind('<Motion>', self.mouse_butt_highlight)

        self.user_pref = load_user_pref()

    def mouse_butt_highlight(self,event,*args):
        mouse_pos_x = event.x
        mouse_pos_y = event.y

        if mouse_pos_x > constants.START_POSX_BUTT_PGMENU and mouse_pos_x < constants.END_POSX_BUTT_PGMENU:
            if mouse_pos_y > constants.START_POSY_BUTT1_PGMENU and mouse_pos_y < constants.END_POSY_BUTT1_PGMENU:
                if self.line_butt1_exists == 0:
                    self.line_butt1_exists = 1
                    self.line1_butt1=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.START_POSY_BUTT1_PGMENU-5 ,constants.END_POSX_BUTT_PGMENU, constants.START_POSY_BUTT1_PGMENU-5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line2_butt1=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.END_POSY_BUTT1_PGMENU+5 ,constants.END_POSX_BUTT_PGMENU, constants.END_POSY_BUTT1_PGMENU+5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line3_butt1=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.START_POSY_BUTT1_PGMENU-10 ,constants.START_POSX_BUTT_PGMENU, constants.END_POSY_BUTT1_PGMENU+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line4_butt1=self.canvas_menu.create_line(constants.END_POSX_BUTT_PGMENU, constants.START_POSY_BUTT1_PGMENU-10 ,constants.END_POSX_BUTT_PGMENU, constants.END_POSY_BUTT1_PGMENU+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
            else:
                if self.line_butt1_exists == 1:
                    self.canvas_menu.delete(self.line1_butt1)
                    self.canvas_menu.delete(self.line2_butt1)
                    self.canvas_menu.delete(self.line3_butt1)
                    self.canvas_menu.delete(self.line4_butt1)
                    self.line_butt1_exists = 0
        else:
            if self.line_butt1_exists == 1:
                self.canvas_menu.delete(self.line1_butt1)
                self.canvas_menu.delete(self.line2_butt1)
                self.canvas_menu.delete(self.line3_butt1)
                self.canvas_menu.delete(self.line4_butt1)
                self.line_butt1_exists = 0
        if mouse_pos_x > constants.START_POSX_BUTT_PGMENU and mouse_pos_x < constants.END_POSX_BUTT_PGMENU:
            if mouse_pos_y > constants.START_POSY_BUTT2_PGMENU and mouse_pos_y < constants.END_POSY_BUTT2_PGMENU:
                if self.line_butt2_exists == 0:
                    self.line_butt2_exists = 1
                    self.line1_butt2=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.START_POSY_BUTT2_PGMENU-5 ,constants.END_POSX_BUTT_PGMENU, constants.START_POSY_BUTT2_PGMENU-5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line2_butt2=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.END_POSY_BUTT2_PGMENU+5 ,constants.END_POSX_BUTT_PGMENU, constants.END_POSY_BUTT2_PGMENU+5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line3_butt2=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.START_POSY_BUTT2_PGMENU-10 ,constants.START_POSX_BUTT_PGMENU, constants.END_POSY_BUTT2_PGMENU+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line4_butt2=self.canvas_menu.create_line(constants.END_POSX_BUTT_PGMENU, constants.START_POSY_BUTT2_PGMENU-10 ,constants.END_POSX_BUTT_PGMENU, constants.END_POSY_BUTT2_PGMENU+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
            else:
                if self.line_butt2_exists == 1:
                    self.canvas_menu.delete(self.line1_butt2)
                    self.canvas_menu.delete(self.line2_butt2)
                    self.canvas_menu.delete(self.line3_butt2)
                    self.canvas_menu.delete(self.line4_butt2)
                    self.line_butt2_exists = 0
        else:
            if self.line_butt2_exists == 1:
                self.canvas_menu.delete(self.line1_butt2)
                self.canvas_menu.delete(self.line2_butt2)
                self.canvas_menu.delete(self.line3_butt2)
                self.canvas_menu.delete(self.line4_butt2)
                self.line_butt2_exists = 0

        if mouse_pos_x > constants.START_POSX_BUTT_PGMENU and mouse_pos_x < constants.END_POSX_BUTT_PGMENU:
            if mouse_pos_y > constants.START_POSY_BUTT3_PGMENU and mouse_pos_y < constants.END_POSY_BUTT3_PGMENU:
                if self.line_butt3_exists == 0:
                    self.line_butt3_exists = 1
                    self.line1_butt3=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.START_POSY_BUTT3_PGMENU-5 ,constants.END_POSX_BUTT_PGMENU, constants.START_POSY_BUTT3_PGMENU-5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line2_butt3=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.END_POSY_BUTT3_PGMENU+5 ,constants.END_POSX_BUTT_PGMENU, constants.END_POSY_BUTT3_PGMENU+5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line3_butt3=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.START_POSY_BUTT3_PGMENU-10 ,constants.START_POSX_BUTT_PGMENU, constants.END_POSY_BUTT3_PGMENU+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line4_butt3=self.canvas_menu.create_line(constants.END_POSX_BUTT_PGMENU, constants.START_POSY_BUTT3_PGMENU-10 ,constants.END_POSX_BUTT_PGMENU, constants.END_POSY_BUTT3_PGMENU+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
            else:
                if self.line_butt3_exists == 1:
                    self.canvas_menu.delete(self.line1_butt3)
                    self.canvas_menu.delete(self.line2_butt3)
                    self.canvas_menu.delete(self.line3_butt3)
                    self.canvas_menu.delete(self.line4_butt3)
                    self.line_butt3_exists = 0
        else:
            if self.line_butt3_exists == 1:
                self.canvas_menu.delete(self.line1_butt3)
                self.canvas_menu.delete(self.line2_butt3)
                self.canvas_menu.delete(self.line3_butt3)
                self.canvas_menu.delete(self.line4_butt3)
                self.line_butt3_exists = 0

        if mouse_pos_x > constants.START_POSX_BUTT_PGMENU and mouse_pos_x < constants.END_POSX_BUTT_PGMENU:
            if mouse_pos_y > constants.START_POSY_BUTT4_PGMENU and mouse_pos_y < constants.END_POSY_BUTT4_PGMENU:
                if self.line_butt4_exists == 0:
                    self.line_butt4_exists = 1
                    self.line1_butt4=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.START_POSY_BUTT4_PGMENU-5 ,constants.END_POSX_BUTT_PGMENU, constants.START_POSY_BUTT4_PGMENU-5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line2_butt4=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.END_POSY_BUTT4_PGMENU+5 ,constants.END_POSX_BUTT_PGMENU, constants.END_POSY_BUTT4_PGMENU+5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line3_butt4=self.canvas_menu.create_line(constants.START_POSX_BUTT_PGMENU, constants.START_POSY_BUTT4_PGMENU-10 ,constants.START_POSX_BUTT_PGMENU, constants.END_POSY_BUTT4_PGMENU+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
                    self.line4_butt4=self.canvas_menu.create_line(constants.END_POSX_BUTT_PGMENU, constants.START_POSY_BUTT4_PGMENU-10 ,constants.END_POSX_BUTT_PGMENU, constants.END_POSY_BUTT4_PGMENU+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGMENU)
            else:
                if self.line_butt4_exists == 1:
                    self.canvas_menu.delete(self.line1_butt4)
                    self.canvas_menu.delete(self.line2_butt4)
                    self.canvas_menu.delete(self.line3_butt4)
                    self.canvas_menu.delete(self.line4_butt4)
                    self.line_butt4_exists = 0
        else:
            if self.line_butt4_exists == 1:
                self.canvas_menu.delete(self.line1_butt4)
                self.canvas_menu.delete(self.line2_butt4)
                self.canvas_menu.delete(self.line3_butt4)
                self.canvas_menu.delete(self.line4_butt4)
                self.line_butt4_exists = 0



    def mouse_function(self,event,*args):
        on_click_pos_x = event.x
        on_click_pos_y = event.y


        if on_click_pos_x > constants.START_POSX_BUTT_PGMENU and on_click_pos_x < constants.END_POSX_BUTT_PGMENU:
            if on_click_pos_y > constants.START_POSY_BUTT1_PGMENU and on_click_pos_y < constants.END_POSY_BUTT1_PGMENU:
                self.sld_page()

        if on_click_pos_x > constants.START_POSX_BUTT_PGMENU and on_click_pos_x < constants.END_POSX_BUTT_PGMENU:
            if on_click_pos_y > constants.START_POSY_BUTT2_PGMENU and on_click_pos_y < constants.END_POSY_BUTT2_PGMENU:
                tk.messagebox.showinfo(parent=self,title="Error - Not Yet Implemented",message = "The load job interface has not yet been implemented but your jobs are still saved. To access them use the job number and the FIND button", icon="warning")

        if on_click_pos_x > constants.START_POSX_BUTT_PGMENU and on_click_pos_x < constants.END_POSX_BUTT_PGMENU:
            if on_click_pos_y > constants.START_POSY_BUTT3_PGMENU and on_click_pos_y < constants.END_POSY_BUTT3_PGMENU:
                tk.messagebox.showinfo(parent=self,title="Error - Not Yet Implemented",message = "This will be implemented down the line", icon="warning")

        if on_click_pos_x > constants.START_POSX_BUTT_PGMENU and on_click_pos_x < constants.END_POSX_BUTT_PGMENU:
            if on_click_pos_y > constants.START_POSY_BUTT4_PGMENU and on_click_pos_y < constants.END_POSY_BUTT4_PGMENU:
                self.exit_app()

        if on_click_pos_x > constants.START_POSX_BUTT_ACC_PGMENU and on_click_pos_x < constants.END_POSX_BUTT_ACC_PGMENU:
            if on_click_pos_y > constants.START_POSY_SETT_PGMENU and on_click_pos_y < constants.END_POSY_SETT_PGMENU:
                settings = SettingsPage(self)
                settings.passing_arguments(self.user_pref,empty_job_dict)

        if on_click_pos_x > constants.START_POSX_BUTT_SETT_PGMENU and on_click_pos_x < constants.END_POSX_BUTT_SETT_PGMENU:
            if on_click_pos_y > constants.START_POSY_SETT_PGMENU and on_click_pos_y < constants.END_POSY_SETT_PGMENU:
                account = AccountPage(self)


        #print(str(on_click_pos_x) + " - " + str(on_click_pos_y))

    def sld_page(self,*args):
        self.new_container = MainViewSld(root)
        self.new_container.place(in_=self, x=0, y=0, relwidth=1, relheight=1)

    def exit_app(self,*args):
        root.destroy()

    def motion(event,*args):
        x, y = event.x, event.y
        print('{}, {}'.format(x, y))


if __name__ == "__main__":
    # Will returned the saved job if it exists, otherwise the value from get_txtfile_info
    root = tk.Tk(className=constants.APP_NAME)
    root.configure(bg=constants.set_baground_for_theme())

    #root.option_add('*TCombobox*Listbox.selectBackground', 'yellow') # change highlight color
    #root.option_add('*TCombobox*Listbox.selectForeground', 'black') # change text color
    #root.option_add('*TCombobox*Listbox.fieldbackground', 'blue')

    #Setting the theme
    style = ThemedStyle(root)
    style.set_theme(constants.APP_THEME)
    s = ttk.Style()
    s.configure('my.TButton', font=('Arial', 14))
    style.configure("my.TEntry", background=constants.set_entries_background_for_darkmode())

    index = 1 #first argument

    if check_arg(index):
        main = MainViewSld(root)
        main.place(in_=root, x=0, y=0, relwidth=1, relheight=1)
        root.wm_geometry(str(constants.WINDOW_SIZE_X)+"x"+str(constants.WINDOW_SIZE_Y)+"+350+200")
        root.mainloop()
    else:
        main = MainView(root)
        main.pack(side="top", fill="none", expand=True)
        root.wm_geometry(str(constants.WINDOW_SIZE_X)+"x"+str(constants.WINDOW_SIZE_Y)+"+350+200")
        root.mainloop()

    #Initiliasing window self.container
