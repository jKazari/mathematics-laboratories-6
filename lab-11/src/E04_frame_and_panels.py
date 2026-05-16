''' 
E04_frame_and_panel.py
'''

import wx

class MainFrame(wx.Frame):

    def __init__(self):

        super().__init__(parent=None,title='04',pos=(1000, 200),size=(400,400) )

        # Set up the first Panel to be at position 1, 1 (the default)
        # and of size 300 by 100
        # with a blue background
        self.top_panel = wx.Panel(self)   # means parent = self i.e. an instance of MainFrame
        self.top_panel.SetSize(1, 1, 150, 100)
        self.top_panel.SetBackgroundColour(wx.Colour(0, 0, 255))

        # Set up the first Panel to be at position 1, 100
        # and of size 150 by 100
        # with a blue background
        self.center_panel = wx.Panel(self)
        self.center_panel.SetSize(1, 100, 150, 100)
        self.center_panel.SetBackgroundColour(wx.Colour(255, 0, 0))

        # Set up the third Panel to be at position 150, 200
        # and of size 150 by 100 with a green background
        self.bottom_panel = wx.Panel(self)
        self.bottom_panel.SetSize(150, 200, 150, 100)
        self.bottom_panel.SetBackgroundColour(wx.Colour(0, 255,0))

class MyApp(wx.App):

    def OnInit(self):
        """ Initialise the main GUI Application"""

        frame = MainFrame()
        frame.Show()

        return True

if __name__ == "__main__":

    app = MyApp()
    app.MainLoop()
