''' 
E06_button_panels_2.py
'''

import wx

# see also U01_wx_colours.py
WPA_COLORS = {
    'FIREBRICK': wx.Colour(142, 35, 35, 255),
    'RED': wx.Colour(255, 0, 0, 255),
    'BLACK': wx.Colour(0, 0, 0, 255),
    'FOREST GREEN': wx.Colour(35, 142, 35, 255),
    'BLUE': wx.Colour(0, 0, 255, 255),
    'GREY': wx.Colour(128, 128, 128, 255),
    'SKY BLUE': wx.Colour(50, 153, 204, 255),
    'GREEN': wx.Colour(0, 255, 0, 255),
    'STEEL BLUE': wx.Colour(35, 107, 142, 255),
    'CYAN': wx.Colour(0, 255, 255, 255),
    'DARK GREY': wx.Colour(47, 47, 47, 255),
    'NAVY': wx.Colour(35, 35, 142, 255),
    'DARK GREEN': wx.Colour(47, 79, 47, 255),
    'ORANGE': wx.Colour(204, 50, 50, 255),
    'VIOLET': wx.Colour(79, 47, 79, 255),
    'PINK': wx.Colour(255, 192, 203, 255),
    'WHITE': wx.Colour(255, 255, 255, 255),
    'YELLOW': wx.Colour(255, 255, 0, 255),
    'DIM GREY': wx.Colour(84, 84, 84, 255),
    'PURPLE': wx.Colour(176, 0, 255, 255)
    }

class OurWidget(wx.Panel):

    def __init__(self,parent,
                    color=WPA_COLORS['SKY BLUE'],
                    pos=wx.DefaultPosition):

        super().__init__(parent,wx.ID_ANY,pos,size = (220,80))

        self.SetBackgroundColour(color)

        # pole tekstowe z komunikatem na górze
        self.message = wx.StaticText(self,label='MESSAGE',pos=(1,1),size=(230,30),
                                     style=wx.ALIGN_CENTRE_HORIZONTAL)

        # dwa przyciski na dole
        self.left_button = wx.Button(self,label='LEFT',pos=(5,40),size=(100,30))
        self.right_button = wx.Button(self,label='RIGHT',pos=(115,40),size=(100,30))



class SampleFrame(wx.Frame):

    def __init__(self):
        
        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='Buttons', size=(400, 400),pos=(1000,100))
        
        # for reference
        self.ref_frame = wx.Panel(self,pos=(150,150),size=(100,100))
        self.ref_frame.SetBackgroundColour(WPA_COLORS['PINK'])

        # our widget with given size and position
        self.our_widget_1 = OurWidget(self)

        # our widget with given size and position
        self.our_widget_2 = OurWidget(self,color=WPA_COLORS['DARK GREEN'],pos=(175,200))


class MainApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = SampleFrame()
        frame.Show()
        
        return True


if __name__ == "__main__":

    app = MainApp()
    app.MainLoop()
