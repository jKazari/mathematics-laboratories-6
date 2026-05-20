import wx

NUMPAD_IDS = {str(k): wx.NewIdRef() for k in range(10)}
NUMPAD_IDS['C'] = wx.NewIdRef()

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Numpad', pos=(500, 200))

        self.display = wx.StaticText(self, size=(180, 30),
                                     style=wx.ST_NO_AUTORESIZE | wx.ALIGN_RIGHT)
        self.display.SetLabel('')
        self.display.SetBackgroundColour((30, 30, 30))
        self.display.SetForegroundColour((0, 255, 0))

        self.grid = wx.GridSizer(4, 3, 4, 4)
        for label in ['7','8','9', '4','5','6', '1','2','3', 'C','0','']:
            if label == '':
                self.grid.Add((0, 0))
            else:
                self.grid.Add(
                    wx.Button(self, id=NUMPAD_IDS[label], label=label, size=(55, 45)),
                    0, wx.EXPAND
                )

        self.outer = wx.BoxSizer(wx.VERTICAL)
        self.outer.Add(self.display, 0, wx.ALL | wx.EXPAND, 8)
        self.outer.Add(self.grid,    0, wx.ALL, 8)

        self.SetSizerAndFit(self.outer)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick)

    def OnButtonClick(self, event):
        eid = event.GetId()
        if eid == NUMPAD_IDS['C']:
            self.display.SetLabel('')
        else:
            for digit, ref in NUMPAD_IDS.items():
                if eid == ref and digit != 'C':
                    self.display.SetLabel(self.display.GetLabel() + digit)
                    break

class MyApp(wx.App):
    def OnInit(self):
        MainFrame().Show()
        return True

if __name__ == "__main__":
    MyApp().MainLoop()