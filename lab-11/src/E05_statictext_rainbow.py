''' 
E05_statictext_rainbow.py
'''

import wx

class SampleFrame(wx.Frame):

    def __init__(self):
        
        self.labels = []

        for i in range(0,10):
            for j in range(0,10):

                l = "({},{})".format(i,j)

                self.labels.append( wx.StaticText(self,pos=(100+50*i,100+30*j), label = l  )  )

                self.labels[-1].SetBackgroundColour((100,25*j,25*i))

        self.SetBackgroundColour((0,0,0))
       

class MainApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = SampleFrame()
        frame.Show()
        
        return True


if __name__ == "__main__":

    app = MainApp()
    app.MainLoop()
