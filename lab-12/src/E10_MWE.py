''' 
E03_MWE.py
'''

import wx

class MainFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='MWE',pos=(1000, 200),size=(400,400) )

        self.left_button = wx.Button(self,id=wx.ID_OK)
        self.right_button = wx.Button(self,id=wx.ID_CANCEL)

        self.left_label = wx.StaticText(self,label = '|-|')

        self.right_label = wx.StaticText(self,label = '|-|')

        self.sizer = wx.GridSizer(2,2,10,10)

        self.sizer.Add(self.left_label,0,0,0)
        self.sizer.Add(self.right_label,0,0,0)
        self.sizer.Add(self.left_button,0,0,0)
        self.sizer.Add(self.right_button,0,0,0)

        self.sizer.SetSizeHints(self)
        self.SetSizer(self.sizer)


        self.Bind(wx.EVT_BUTTON,self.OnButtonClick)

        self.Bind(wx.EVT_LEFT_DOWN,self.OnMouseLeftDown)

    def OnButtonClick(self,event):

        match event.GetId():
            case wx.ID_CANCEL:
                self.left_label.SetLabel('wx.ID_CANCEL')
            case wx.ID_OK:
                self.right_label.SetLabel('wx.ID_OK')
            case _:
                self.left_label.SetLabel(  str( event.GetId() ) )

    def OnMouseLeftDown(self,event):
        print(event.GetPosition())

        # event.Skip()


class MyApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = MainFrame()
        frame.Show()

        return True



if __name__ == "__main__":

    app = MyApp()
    app.MainLoop()
