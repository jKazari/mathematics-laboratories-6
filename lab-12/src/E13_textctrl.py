''' 
E13_textctrl.py
'''

import wx

class MainFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='TextCtrl',pos=(1000, 200),size=(400,400) )

        self.text_input = wx.TextCtrl(self,pos=(1,1)
                                      # (STEP3)
                                      ,style = wx.TE_PROCESS_ENTER,
                                      )
        self.text_input.SetSize(200,  self.text_input.GetSize()[1] )

        self.text_input.SetBackgroundColour((50,100,50))

        self.text_output = wx.StaticText(self,pos=(1,50),
                                         style=wx.ST_NO_AUTORESIZE|wx.ALIGN_CENTER
                                         )
        self.text_output.SetLabel('Hello ')
        self.text_output.SetSize(200,  self.text_output.GetSize()[1] )

        self.text_output.SetBackgroundColour((50,50,100))

        self.button = wx.Button(self,pos=(1,100),label='Proceed')



        self.Bind(wx.EVT_BUTTON,self.OnButtonClick)

        # (STEP2)
        self.Bind(wx.EVT_TEXT,self.OnText)

        # (STEP3)
        self.Bind(wx.EVT_TEXT_ENTER,self.OnTextEnter)

    def OnButtonClick(self,event):
        pass
        # (STEP1)
        # self.text_output.SetLabel( self.text_input.GetValue()  )

        # zadanie
        # self.text_input.SetValue('Wpisz jakiś tekst...')


    # (STEP2)
    def OnText(self,event):

        self.text_output.SetLabel( self.text_input.GetValue()  )

    # (STEP3)
    def OnTextEnter(self,event):

        self.text_output.SetLabel( self.text_input.GetValue().upper()  )



class MyApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = MainFrame()
        frame.Show()

        return True

if __name__ == "__main__":

    app = MyApp()
    app.MainLoop()
