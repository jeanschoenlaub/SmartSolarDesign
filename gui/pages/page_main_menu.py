class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, **kwargs, bg=constants.set_baground_for_theme())


class PageMainMenu(Page):
   def __init__(self, *args, **kwargs):
       #Initialie the Frame
       Page.__init__(self, *args, **kwargs)
