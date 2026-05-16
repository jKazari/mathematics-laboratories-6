'''
E07_box_sizer.py
'''

import wx

class RowOfButtons(wx.Panel):

    def __init__(self,parent,labels,pos=wx.DefaultPosition,size=wx.DefaultSize):
        super().__init__(parent,wx.ID_ANY,pos,size)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)

        for l in labels:
            self.sizer.Add( wx.Button(self,label=l),0,wx.ALL,5)

        self.SetSizer(self.sizer)



class SampleFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='Box sizer', size=(100, 100),pos=(1000,100))


        self.outer_sizer = wx.BoxSizer(wx.VERTICAL)

        self.outer_sizer.Add(RowOfButtons(self,'123456'),0,0,0)
        self.outer_sizer.Add(RowOfButtons(self,'ABCDEFGH'),0,0,0)
        self.outer_sizer.Add(RowOfButtons(self,['Ala','Ola','Ela','Ula','Ila','Yla']),0,0,0)


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
