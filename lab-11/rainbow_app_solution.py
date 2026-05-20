import wx

class RainbowFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Rainbow', pos=(200, 100), size=(700, 440))
        self.SetBackgroundColour((0, 0, 0))

        self.labels = []
        for i in range(10):
            for j in range(10):
                label = "({},{})".format(i, j)
                txt = wx.StaticText(
                    self,
                    label=label,
                    pos=(40 + 60*i, 30 + 38*j),
                    size=(55, 22),
                    style=wx.ALIGN_CENTRE_HORIZONTAL
                )

                txt.SetBackgroundColour((100, 25*j, 25*i))
                txt.SetForegroundColour((255, 255, 255))
                self.labels.append(txt)

class MyApp(wx.App):
    def OnInit(self):
        frame = RainbowFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()