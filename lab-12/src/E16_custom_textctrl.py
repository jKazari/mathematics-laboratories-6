''' 
E16_textctrl.py
'''

import wx

# (STEP2)
# class OurTextCtrl(wx.TextCtrl):
#
#     def __init__(self,parent, pos):
#         super().__init__(parent,pos=pos)
#
#         self.SetValue(''   <--<">-->   '')
#
#         self.Bind(wx.EVT_LEFT_DOWN,self.OnMouseLeftDown)
#
#     def OnMouseLeftDown(self,event):
#
#         self.SetValue( )
#
#         event.Skip()



class MainFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='TextCtrl',pos=(1000, 200),size=(400,400) )

        self.text_input = wx.TextCtrl(self,pos=(1,1),size=(200,20) )
        self.text_input.SetBackgroundColour((50,100,50))

        self.text_output = wx.StaticText(self,pos=(1,50),
                                         style=wx.ST_NO_AUTORESIZE|wx.ALIGN_CENTER
                                         )
        self.text_output.SetLabel('Hello ')
        self.text_output.SetSize(200,  self.text_output.GetSize()[1] )
        self.text_output.SetBackgroundColour((50,50,100))

        self.button = wx.Button(self,pos=(1,100),label='Proceed')

        # (STEP1)
        # self.text_input.Bind(wx.EVT_LEFT_DOWN,self.ClearText)

        # (STEP2)
        # self.out_input = OurTextCtrl(self,pos=(1,200))


        self.Bind(wx.EVT_BUTTON,self.OnButtonClick)
        self.Bind(wx.EVT_TEXT,self.OnText)
        self.Bind(wx.EVT_LEFT_DOWN,self.OnMouseLeftDown)

    def OnButtonClick(self,event):
        self.text_output.SetLabel( self.text_input.GetValue()  )
        self.text_input.SetValue('Wpisz jakiś tekst...')

    def OnText(self,event):
        self.text_output.SetLabel( self.text_input.GetValue()  )

    def OnMouseLeftDown(self,event):
        print(event.GetId())
        self.text_output.SetLabel( 'Mouse at {}'.format(event.GetPosition()) )
        # event.Skip()

    # (STEP1)
#     def ClearText(self,event):
#         self.text_input.SetValue( '' )
#
#         event.Skip()

class MyApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = MainFrame()
        frame.Show()

        return True

if __name__ == "__main__":

    app = MyApp()
    app.MainLoop()
