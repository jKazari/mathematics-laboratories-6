import wx

class RowOfButtons(wx.Panel):
    def __init__(self, parent, labels, pos=wx.DefaultPosition, size=wx.DefaultSize):
        super().__init__(parent, wx.ID_ANY, pos, size)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        for l in labels:
            self.sizer.Add(wx.Button(self, label=l, size=(60, 60)), 0, wx.ALL, 3)
        self.SetSizer(self.sizer)

class NumpadWidget(wx.Panel):
    def __init__(self, parent, pos=wx.DefaultPosition):
        super().__init__(parent, wx.ID_ANY, pos)

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.Add(RowOfButtons(self, ['7', '8', '9']), 0, wx.ALL, 0)
        self.sizer.Add(RowOfButtons(self, ['4', '5', '6']), 0, wx.ALL, 0)
        self.sizer.Add(RowOfButtons(self, ['1', '2', '3']), 0, wx.ALL, 0)

        self.zero_row = wx.Panel(self)
        self.zero_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.zero_btn = wx.Button(self.zero_row, label='0', size=(198, 60))
        self.zero_sizer.Add(self.zero_btn, 0, wx.ALL, 3)
        self.zero_row.SetSizer(self.zero_sizer)

        self.sizer.Add(self.zero_row, 0, wx.ALL, 0)
        self.SetSizer(self.sizer)

class SampleFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Numpad', pos=(500, 200))

        self.outer_sizer = wx.BoxSizer(wx.VERTICAL)
        self.numpad = NumpadWidget(self)
        self.outer_sizer.Add(self.numpad, 0, wx.ALL, 10)

        self.SetSizerAndFit(self.outer_sizer)

class MyApp(wx.App):
    def OnInit(self):
        frame = SampleFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()