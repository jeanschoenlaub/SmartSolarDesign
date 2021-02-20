import tkinter as tk
import tkinter.ttk as ttk

import databases.constants as constants
from gui.pages.pop_up_pages import ConfigBlockDiag, ConfigVrise

class SettingsPage(tk.Toplevel):

    def __init__(self, master = None):
        super().__init__(master = master)
        self.title("User settings")
        self.geometry(str(constants.WINDOW_SIZE_X_PGSETT)+"x"+str(constants.WINDOW_SIZE_Y_PGSETT)+"+300+200")

        self.background_image=tk.PhotoImage(file="/Users/jean/Documents/Dev/SmartSolarDesign/databases/Images/Backgrounds/BackgroundSettings.png")
        #self.background_label = tk.Label(self, image=self.background_image)
        #self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #variables to make the interactive border work
        self.line_butt1_exists = 0
        self.line_butt2_exists = 0
        self.line_butt3_exists = 0
        self.line_butt4_exists = 0


        self.canvas_settings = tk.Canvas(self, width=constants.WINDOW_SIZE_X_PGSETT, height=constants.WINDOW_SIZE_Y_PGSETT)
        self.canvas_settings.pack(fill="none", expand=True)
        self.canvas_settings.create_image(constants.WINDOW_SIZE_X_PGSETT/2, constants.WINDOW_SIZE_Y_PGSETT/2, image = self.background_image)

        self.canvas_settings.bind("<Button-1>", self.mouse_function)
        #self.canvas_settings.bind('<Motion>', self.mouse_butt_highlight)

    def passing_arguments(self, user_pref, job_dict):
        self.user_pref = user_pref
        self.job_dict = job_dict #If called from main menu this is emptz if called from a job as the real job dict


    def mouse_function(self,event,*args):
        on_click_pos_x = event.x
        on_click_pos_y = event.y


        if on_click_pos_x > constants.START_POSX_BUTT1_PGSETT and on_click_pos_x < constants.END_POSX_BUTT1_PGSETT:
            if on_click_pos_y > constants.START_POSY_BUTT1_PGSETT and on_click_pos_y < constants.END_POSY_BUTT1_PGSETT:
                pop_up = ConfigVrise(self)
                pop_up.show_layout(self.user_pref)

        if on_click_pos_x > constants.START_POSX_BUTT2_PGSETT and on_click_pos_x < constants.END_POSX_BUTT2_PGSETT:
            if on_click_pos_y > constants.START_POSY_BUTT1_PGSETT and on_click_pos_y < constants.END_POSY_BUTT1_PGSETT:
                pop_up_bd = ConfigBlockDiag(self)
                pop_up_bd.show_layout(self.job_dict,self.user_pref)

        if on_click_pos_x > constants.START_POSX_BUTT3_PGSETT and on_click_pos_x < constants.END_POSX_BUTT3_PGSETT:
            if on_click_pos_y > constants.START_POSY_BUTT1_PGSETT and on_click_pos_y < constants.END_POSY_BUTT1_PGSETT:
                print("Buttton 3")

        if on_click_pos_x > constants.START_POSX_BUTT_EXIT_PGSETT and on_click_pos_x < constants.END_POSX_BUTT_EXIT_PGSETT:
            if on_click_pos_y > constants.START_POSY_BUTT_EXIT_PGSETT and on_click_pos_y < constants.END_POSY_BUTT_EXIT_PGSETT:
                self.exit_app()


        #print(str(on_click_pos_x) + " - " + str(on_click_pos_y))

    def exit_app(self,*args):
       self.destroy()


       # def mouse_butt_highlight(self,event,*args):
       #     mouse_pos_x = event.x
       #     mouse_pos_y = event.y
       #
       #     if mouse_pos_x > constants.START_POSX_BUTT_PGSETT1 and mouse_pos_x < constants.END_POSX_BUTT_PGSETT:
       #         if mouse_pos_y > constants.START_POSY_BUTT1_PGSETT and mouse_pos_y < constants.END_POSY_BUTT1_PGSETT:
       #             if self.line_butt1_exists == 0:
       #                 self.line_butt1_exists = 1
       #                 self.line1_butt1=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.START_POSY_BUTT1_PGSETT-5 ,constants.END_POSX_BUTT_PGSETT, constants.START_POSY_BUTT1_PGSETT-5,width= 5, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line2_butt1=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.END_POSY_BUTT1_PGSETT+5 ,constants.END_POSX_BUTT_PGSETT, constants.END_POSY_BUTT1_PGSETT+5,width= 5, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line3_butt1=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.START_POSY_BUTT1_PGSETT-10 ,constants.START_POSX_BUTT_PGSETT1, constants.END_POSY_BUTT1_PGSETT+10,width= 5, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line4_butt1=self.canvas_settings.create_line(constants.END_POSX_BUTT_PGSETT-5, constants.START_POSY_BUTT1_PGSETT-10 ,constants.END_POSX_BUTT_PGSETT-5, constants.END_POSY_BUTT1_PGSETT+10,width= 5, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #         else:
       #             if self.line_butt1_exists == 1:
       #                 self.canvas_settings.delete(self.line1_butt1)
       #                 self.canvas_settings.delete(self.line2_butt1)
       #                 self.canvas_settings.delete(self.line3_butt1)
       #                 self.canvas_settings.delete(self.line4_butt1)
       #                 self.line_butt1_exists = 0
       #     else:
       #         if self.line_butt1_exists == 1:
       #             self.canvas_settings.delete(self.line1_butt1)
       #             self.canvas_settings.delete(self.line2_butt1)
       #             self.canvas_settings.delete(self.line3_butt1)
       #             self.canvas_settings.delete(self.line4_butt1)
       #             self.line_butt1_exists = 0
       #
       #     if mouse_pos_x > constants.START_POSX_BUTT_PGSETT1 and mouse_pos_x < constants.END_POSX_BUTT_PGSETT:
       #         if mouse_pos_y > constants.START_POSY_BUTT2_PGSETT and mouse_pos_y < constants.END_POSY_BUTT2_PGSETT:
       #             if self.line_butt2_exists == 0:
       #                 self.line_butt2_exists = 1
       #                 self.line1_butt2=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.START_POSY_BUTT2_PGSETT-5 ,constants.END_POSX_BUTT_PGSETT, constants.START_POSY_BUTT2_PGSETT-5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line2_butt2=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.END_POSY_BUTT2_PGSETT+5 ,constants.END_POSX_BUTT_PGSETT, constants.END_POSY_BUTT2_PGSETT+5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line3_butt2=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.START_POSY_BUTT2_PGSETT-10 ,constants.START_POSX_BUTT_PGSETT1, constants.END_POSY_BUTT2_PGSETT+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line4_butt2=self.canvas_settings.create_line(constants.END_POSX_BUTT_PGSETT, constants.START_POSY_BUTT2_PGSETT-10 ,constants.END_POSX_BUTT_PGSETT, constants.END_POSY_BUTT2_PGSETT+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #         else:
       #             if self.line_butt2_exists == 1:
       #                 self.canvas_settings.delete(self.line1_butt2)
       #                 self.canvas_settings.delete(self.line2_butt2)
       #                 self.canvas_settings.delete(self.line3_butt2)
       #                 self.canvas_settings.delete(self.line4_butt2)
       #                 self.line_butt2_exists = 0
       #     else:
       #         if self.line_butt2_exists == 1:
       #             self.canvas_settings.delete(self.line1_butt2)
       #             self.canvas_settings.delete(self.line2_butt2)
       #             self.canvas_settings.delete(self.line3_butt2)
       #             self.canvas_settings.delete(self.line4_butt2)
       #             self.line_butt2_exists = 0
       #
       #     if mouse_pos_x > constants.START_POSX_BUTT_PGSETT1 and mouse_pos_x < constants.END_POSX_BUTT_PGSETT:
       #         if mouse_pos_y > constants.START_POSY_BUTT3_PGSETT and mouse_pos_y < constants.END_POSY_BUTT3_PGSETT:
       #             if self.line_butt3_exists == 0:
       #                 self.line_butt3_exists = 1
       #                 self.line1_butt3=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.START_POSY_BUTT3_PGSETT-5 ,constants.END_POSX_BUTT_PGSETT, constants.START_POSY_BUTT3_PGSETT-5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line2_butt3=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.END_POSY_BUTT3_PGSETT+5 ,constants.END_POSX_BUTT_PGSETT, constants.END_POSY_BUTT3_PGSETT+5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line3_butt3=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.START_POSY_BUTT3_PGSETT-10 ,constants.START_POSX_BUTT_PGSETT1, constants.END_POSY_BUTT3_PGSETT+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line4_butt3=self.canvas_settings.create_line(constants.END_POSX_BUTT_PGSETT, constants.START_POSY_BUTT3_PGSETT-10 ,constants.END_POSX_BUTT_PGSETT, constants.END_POSY_BUTT3_PGSETT+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #         else:
       #             if self.line_butt3_exists == 1:
       #                 self.canvas_settings.delete(self.line1_butt3)
       #                 self.canvas_settings.delete(self.line2_butt3)
       #                 self.canvas_settings.delete(self.line3_butt3)
       #                 self.canvas_settings.delete(self.line4_butt3)
       #                 self.line_butt3_exists = 0
       #     else:
       #         if self.line_butt3_exists == 1:
       #             self.canvas_settings.delete(self.line1_butt3)
       #             self.canvas_settings.delete(self.line2_butt3)
       #             self.canvas_settings.delete(self.line3_butt3)
       #             self.canvas_settings.delete(self.line4_butt3)
       #             self.line_butt3_exists = 0
       #
       #     if mouse_pos_x > constants.START_POSX_BUTT_PGSETT1 and mouse_pos_x < constants.END_POSX_BUTT_PGSETT:
       #         if mouse_pos_y > constants.START_POSY_BUTT4_PGSETT and mouse_pos_y < constants.END_POSY_BUTT4_PGSETT:
       #             if self.line_butt4_exists == 0:
       #                 self.line_butt4_exists = 1
       #                 self.line1_butt4=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.START_POSY_BUTT4_PGSETT-5 ,constants.END_POSX_BUTT_PGSETT, constants.START_POSY_BUTT4_PGSETT-5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line2_butt4=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.END_POSY_BUTT4_PGSETT+5 ,constants.END_POSX_BUTT_PGSETT, constants.END_POSY_BUTT4_PGSETT+5,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line3_butt4=self.canvas_settings.create_line(constants.START_POSX_BUTT_PGSETT1, constants.START_POSY_BUTT4_PGSETT-10 ,constants.START_POSX_BUTT_PGSETT1, constants.END_POSY_BUTT4_PGSETT+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #                 self.line4_butt4=self.canvas_settings.create_line(constants.END_POSX_BUTT_PGSETT, constants.START_POSY_BUTT4_PGSETT-10 ,constants.END_POSX_BUTT_PGSETT, constants.END_POSY_BUTT4_PGSETT+10,width= 10, fill = constants.COLOR_BUTT_HIGHLIGHT_PGSETT)
       #         else:
       #             if self.line_butt4_exists == 1:
       #                 self.canvas_settings.delete(self.line1_butt4)
       #                 self.canvas_settings.delete(self.line2_butt4)
       #                 self.canvas_settings.delete(self.line3_butt4)
       #                 self.canvas_settings.delete(self.line4_butt4)
       #                 self.line_butt4_exists = 0
       #     else:
       #         if self.line_butt4_exists == 1:
       #             self.canvas_settings.delete(self.line1_butt4)
       #             self.canvas_settings.delete(self.line2_butt4)
       #             self.canvas_settings.delete(self.line3_butt4)
       #             self.canvas_settings.delete(self.line4_butt4)
       #             self.line_butt4_exists = 0
