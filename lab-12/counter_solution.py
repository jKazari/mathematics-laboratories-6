import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Counter', pos=(1000, 200))

        self.n_clicks = 0

        self.st_counter = wx.StaticText(self, size=(200, 25),
                                        style=wx.ST_NO_AUTORESIZE | wx.ALIGN_CENTER)
        self.st_counter.SetLabel(str(self.n_clicks))
        self.st_counter.SetBackgroundColour((150, 120, 110))

        self.button_inc = wx.Button(self, id=wx.ID_UP,    label='Increment')
        self.button_dec = wx.Button(self, id=wx.ID_DOWN,  label='Decrement')
        self.button_reset = wx.Button(self, id=wx.ID_CLEAR, label='Clear')

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.st_counter,   0, wx.ALL | wx.ALIGN_CENTER, 10)
        self.sizer.Add(self.button_inc,   0, wx.ALL, 10)
        self.sizer.Add(self.button_dec,   0, wx.ALL, 10)
        self.sizer.Add(self.button_reset, 0, wx.ALL, 10)

        self.SetSizerAndFit(self.sizer)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick)

    def OnButtonClick(self, event):
        match event.GetId():
            case wx.ID_UP:
                self.n_clicks += 1
            case wx.ID_DOWN:
                self.n_clicks -= 1
            case wx.ID_CLEAR:
                self.n_clicks = 0
            case _:
                pass  # unknown button — do nothing
        self.st_counter.SetLabel(str(self.n_clicks))

class MyApp(wx.App):
    def OnInit(self):
        MainFrame().Show()
        return True

if __name__ == "__main__":
    MyApp().MainLoop()