import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='StaticText tasks', pos=(200, 100), size=(500, 400))

        self.centre_label = wx.StaticText(
            self, label='Napis na środku ramki',
            pos=(170, 170), size=(160, 30),
            style=wx.ALIGN_CENTRE_HORIZONTAL
        )
        self.centre_label.SetBackgroundColour(wx.Colour(0, 200, 0))

        self.corner_label = wx.StaticText(
            self, label='Napis na dole ramki',
            pos=(340, 340), size=(140, 30),
            style=wx.ALIGN_RIGHT
        )
        self.corner_label.SetBackgroundColour(wx.Colour(0, 200, 0))

        self.SetBackgroundColour(wx.Colour(0, 200, 0))

class MyApp(wx.App):
    def OnInit(self):
        frame = MainFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()