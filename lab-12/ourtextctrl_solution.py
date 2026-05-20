import wx

PLACEHOLDER = 'Wpisz jakiś tekst...'

class OurTextCtrl(wx.TextCtrl):
    def __init__(self, parent, pos=wx.DefaultPosition):
        super().__init__(parent, pos=pos, size=(200, -1))
        self.SetValue(PLACEHOLDER)
        self.SetBackgroundColour((50, 100, 50))
        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)

    def OnMouseLeftDown(self, event):
        if self.GetValue() == PLACEHOLDER:
            self.SetValue('')
        else:
            self.SetValue(PLACEHOLDER)
        event.Skip()


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Custom TextCtrl', pos=(1000, 200), size=(400, 400))

        self.text_input = OurTextCtrl(self, pos=(1, 1))

        self.text_output = wx.StaticText(self, pos=(1, 50),
                                         style=wx.ST_NO_AUTORESIZE | wx.ALIGN_CENTER)
        self.text_output.SetLabel('Hello')
        self.text_output.SetSize(200, self.text_output.GetSize()[1])
        self.text_output.SetBackgroundColour((50, 50, 100))

        self.button = wx.Button(self, pos=(1, 100), label='Proceed')

        self.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        self.Bind(wx.EVT_TEXT,   self.OnText)

    def OnButtonClick(self, event):
        self.text_output.SetLabel(self.text_input.GetValue())

    def OnText(self, event):
        self.text_output.SetLabel(self.text_input.GetValue())

class MyApp(wx.App):
    def OnInit(self):
        MainFrame().Show()
        return True

if __name__ == "__main__":
    MyApp().MainLoop()