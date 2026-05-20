import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Mouse events', pos=(1000, 200), size=(400, 400))

        self.label_A = wx.StaticText(self, pos=(1, 1), size=(20, 20), label='A')
        self.label_A.SetBackgroundColour((125, 50, 200))
        self.color_A_original = (125, 50, 200)

        self.label_B = wx.StaticText(self, pos=(380, 380), size=(20, 20), label='B')
        self.label_B.SetBackgroundColour((200, 50, 125))

        self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnMouseLeftUp)
        self.Bind(wx.EVT_LEFT_DCLICK, self.OnMouseLeftDClick)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRightDown)
        self.Bind(wx.EVT_RIGHT_UP, self.OnMouseRightUp)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)

    def OnMouseLeftDown(self, event):
        self.label_A.SetBackgroundColour((0, 255, 0))
        self.label_A.Refresh()
        event.Skip()

    def OnMouseLeftUp(self, event):
        self.label_A.SetBackgroundColour(self.color_A_original)
        self.label_A.Refresh()

    def OnMouseLeftDClick(self, event):
        print('double click')

    def OnMouseRightDown(self, event):
        position = event.GetPosition()
        print('OnMouseRightDown at {}'.format(position))
        self.label_B.SetPosition(position)

    def OnMouseRightUp(self, event):
        y = event.GetPosition()[1]
        self.label_A.SetPosition((1, y))

    def OnMouseMove(self, event):
        if event.Dragging() and event.RightIsDown():
            self.label_B.SetPosition(event.GetPosition())

class MyApp(wx.App):
    def OnInit(self):
        MainFrame().Show()
        return True

if __name__ == "__main__":
    MyApp().MainLoop()