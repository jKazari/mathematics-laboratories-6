'''
E02_hello_word_bis.py
'''

import wx

class MyApp(wx.App):
    def OnInit(self):
        """ Initialise the main GUI Application"""

        # create a Frame (representing the top-level window)
        frame = wx.Frame(parent=None, title=' Hello World')

        # add a text label to it
        text = wx.StaticText(parent=frame, label= 'Hello Python')

        frame.Show()
        # Indicate whether processing should continue or not
        return True

if __name__ == "__main__":

    # This class can now be instantiated and the MainLoop started
    app = MyApp()

    # Run the GUI application
    app.MainLoop()
