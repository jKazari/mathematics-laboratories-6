import wx

COLORS_ALT = [
    (255,0,0),(255,100,0),(255,200,0),(0,255,0),(0,200,100),
    (0,100,255),(0,0,255),(128,0,255),(255,0,200),(80,80,80)
]

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Keyboard events', pos=(400, 200), size=(400, 400))

        self.label_A = wx.StaticText(self, pos=(1, 1), size=(80, 20), label='A')
        self.label_A.SetBackgroundColour((125, 50, 200))

        self.label_B = wx.StaticText(self, pos=(200, 190), size=(20, 20), label='B')
        self.label_B.SetBackgroundColour((200, 50, 125))

        self.label_B_origin = (200, 190)

        if wx.GetOsDescription().startswith('Windows'):
            self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        else:
            self.panel = wx.Panel(self, pos=(0, 0), size=(400, 400))
            self.panel.SetFocus()
            self.panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

    def OnKeyDown(self, event):
        Ukeycode = event.GetUnicodeKey()
        keycode  = event.GetKeyCode()

        if Ukeycode != wx.WXK_NONE:
            self.label_A.SetLabel('%c' % Ukeycode)

            if event.HasAnyModifiers():
                match event.GetModifiers():
                    case wx.MOD_ALT:
                        digit = Ukeycode - ord('0')
                        if 0 <= digit <= 9:
                            self.label_A.SetBackgroundColour(COLORS_ALT[digit])
                            self.label_A.Refresh()
                    case wx.MOD_CONTROL:
                        self.label_A.SetLabel('Ctrl+%c' % Ukeycode)
                    case wx.MOD_SHIFT:
                        self.label_A.SetLabel('Shift+%c' % Ukeycode)
        else:
            if event.IsKeyInCategory(wx.WXK_CATEGORY_ARROW):
                x, y = self.label_B.GetPosition()
                step = 5
                match keycode:
                    case wx.WXK_LEFT: self.label_B.SetPosition((x - step, y))
                    case wx.WXK_RIGHT: self.label_B.SetPosition((x + step, y))
                    case wx.WXK_UP: self.label_B.SetPosition((x, y - step))
                    case wx.WXK_DOWN: self.label_B.SetPosition((x, y + step))

            elif keycode == wx.WXK_ESCAPE:
                self.label_A.SetBackgroundColour((125, 50, 200))
                self.label_A.SetLabel('A')
                self.label_B.SetPosition(self.label_B_origin)
                self.label_A.Refresh()

class MyApp(wx.App):
    def OnInit(self):
        MainFrame().Show()
        return True

if __name__ == "__main__":
    MyApp().MainLoop()