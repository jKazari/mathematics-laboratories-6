''' 
E11_on_button_click.py
'''

import wx

class MainFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='MWE',pos=(1000, 200),size=(400,400) )

        self.n_clicks = 0;

        self.st_counter = wx.StaticText(self)
        self.st_counter.SetLabel(str(self.n_clicks))
        self.st_counter.SetBackgroundColour((150,120,110))

        self.button = wx.Button(self,label = 'Click Me')

        self.sizer = wx.BoxSizer(wx.VERTICAL)

        self.sizer.Add(self.st_counter,0,wx.ALL,10)
        self.sizer.Add(self.button,0,wx.ALL,25)
        self.sizer.Add( 200,25,0 )

        self.sizer.SetSizeHints(self)
        self.SetSizer(self.sizer)

        # (STEP1)
        self.Bind(wx.EVT_BUTTON,self.OnButtonClick)


    # (STEP1)
    def OnButtonClick(self,event):

        self.n_clicks += 1
        self.st_counter.SetLabel( str(self.n_clicks) )

class MyApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = MainFrame()
        frame.Show()

        return True



if __name__ == "__main__":

    app = MyApp()
    app.MainLoop()
