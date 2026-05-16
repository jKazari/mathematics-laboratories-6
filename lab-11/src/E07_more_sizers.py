'''
E07_box_sizer.py
'''

import wx

# (STEP2)
import E06_button_panels_2 as WPA

class SampleFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='Box sizer', size=(100, 100),pos=(1000,100))

        self.outer_sizer = wx.BoxSizer(wx.VERTICAL)

        self.inner_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        # add inner sizer as the first element of outer
        self.outer_sizer.Add(self.inner_sizer_1,0,0,0)

        # fill inner sizer with widgets
        self.inner_sizer_1.Add( wx.Button(self,id=wx.ID_OK),0,0,0  )
        self.inner_sizer_1.Add( wx.Button(self,id=wx.ID_APPLY),0,0,0  )
        self.inner_sizer_1.Add( wx.Button(self,id=wx.ID_CANCEL),0,0,0  )


        # (STEP1)
        # self.inner_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        # self.outer_sizer.Add(self.inner_sizer_2,0,0,0)
        #
        # self.inner_sizer_2.Add( wx.Button(self,id=wx.ID_NO),0,0,0  )
        # self.inner_sizer_2.Add( wx.Button(self,id=wx.ID_YES),0,0,0  )


        # (STEP2)
        # self.inner_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        # self.outer_sizer.Add(self.inner_sizer_3,0,0,0)
        #
        # self.our_widget_1 = WPA.OurWidget(self,color=WPA.WPA_COLORS['DARK GREEN'])
        # self.inner_sizer_3.Add(self.our_widget_1,0,0,0  )
        #
        # self.our_widget_2 = WPA.OurWidget(self,color=WPA.WPA_COLORS['SKY BLUE'])
        # self.inner_sizer_3.Add(self.our_widget_2,0,0,0  )

        self.outer_sizer.SetSizeHints(self)
        self.SetSizer(self.outer_sizer)



class MainApp(wx.App):

    def OnInit(self):
        """ Initialise the main GUI Application"""

        frame = SampleFrame()
        frame.Show()

        return True


if __name__ == "__main__":

    app = MainApp()
    app.MainLoop()
