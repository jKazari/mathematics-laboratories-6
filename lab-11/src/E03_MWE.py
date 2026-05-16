''' 
E03_MWE.py
'''

import wx

class MainFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='MWE',pos=(1000, 200),size=(400,400) )

        # create widgets
        # drink coffe if you like
        # but get things done



class MyApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = MainFrame()
        frame.Show()

        return True



if __name__ == "__main__":

    app = MyApp()
    app.MainLoop()
