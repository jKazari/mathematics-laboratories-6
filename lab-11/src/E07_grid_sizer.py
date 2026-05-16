'''
E07_box_sizer.py
'''

import wx

# (STEP1)
import E06_button_panels_2 as WPA

class SampleFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='Box sizer', size=(100, 100),pos=(1000,100))

        self.grp_of_buttons = wx.GridSizer(3,3,0,0)

        self.grp_of_buttons.Add( wx.Button(self,id=wx.ID_OK),0,0,0  )

        self.our_button = wx.Button(self,id=wx.ID_CANCEL)
        self.grp_of_buttons.Add(self.our_button,0,0,0  )

        self.grp_of_buttons.Add( wx.Button(self,id=wx.ID_APPLY),0,0,0  )
        self.grp_of_buttons.Add( wx.Button(self,id=wx.ID_NO),0,0,0  )
        self.grp_of_buttons.Add( wx.Button(self,id=wx.ID_YES),0,0,0  )

        # (STEP1)
        self.our_widget_1 = WPA.OurWidget(self,color=WPA.WPA_COLORS['DARK GREEN'])
        self.grp_of_buttons.Add(self.our_widget_1,0,0,0  )

        self.grp_of_buttons.SetSizeHints(self)
        self.SetSizer(self.grp_of_buttons)


class MainApp(wx.App):

    def OnInit(self):
        """ Initialise the main GUI Application"""

        frame = SampleFrame()
        frame.Show()

        return True


if __name__ == "__main__":

    app = MainApp()
    app.MainLoop()
