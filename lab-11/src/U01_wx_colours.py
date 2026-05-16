'''
U01_wx_colours

see
* https://docs.wxpython.org/wx.Colour.html#wx-colour
* https://docs.wxpython.org/wx.ColourDatabase.html#wx-colourdatabase

Obtain system theme equivalents of named colors in RGBA.
Sample output below.
'''

import wx

class ColorData(wx.ColourDatabase):

    named_colors = (
        'AQUAMARINE','FIREBRICK','MEDIUM FOREST GREEN','RED','BLACK','FOREST GREEN',
        'MEDIUM GOLDENROD','SALMON','BLUE','GOLD','MEDIUM ORCHID','SEA GREEN','BLUE VIOLET',
        'GOLDENROD','MEDIUM SEA GREEN','SIENNA','BROWN','GREY','MEDIUM SLATE BLUE',
        'SKY BLUE','CADET BLUE','GREEN','MEDIUM SPRING GREEN','SLATE BLUE','CORAL',
        'GREEN YELLOW','MEDIUM TURQUOISE','SPRING GREEN','CORNFLOWER BLUE','INDIAN RED',
        'MEDIUM VIOLET RED','STEEL BLUE','CYAN','KHAKI','MIDNIGHT BLUE','TAN','DARK GREY',
        'LIGHT BLUE','NAVY','THISTLE','DARK GREEN','LIGHT GREY','ORANGE','TURQUOISE',
        'DARK OLIVE GREEN','LIGHT STEEL BLUE','ORANGE RED','VIOLET','DARK ORCHID',
        'LIME GREEN','ORCHID','VIOLET RED','DARK SLATE BLUE','MAGENTA','PALE GREEN',
        'WHEAT','DARK SLATE GREY','MAROON','PINK','WHITE','DARK TURQUOISE','MEDIUM AQUAMARINE',
        'PLUM','YELLOW','DIM GREY','MEDIUM BLUE','PURPLE','YELLOW GREEN'
    )

    color_dictionary = {}

    def __init__(self):
        super().__init__()

        for color in self.named_colors:
            self.color_dictionary[color] = self.Find(color)

    def __str__(self):
        return str(self.color_dictionary)

    def GetColor(self,name):
        return color_dictionary[name]

class SampleFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='Colors',pos=(1000,100))

        grid_sizer = wx.GridSizer(25, 3, 10, 10)

        for k,v in ColorData.color_dictionary.items():

            tmp = wx.StaticText(self,label = k)
            tmp.SetBackgroundColour(v)

            grid_sizer.Add(tmp,0,0,0)

        grid_sizer.SetSizeHints(self)
        self.SetSizer(grid_sizer)

class MainApp(wx.App):


    def OnInit(self):
        """ Initialise the main GUI Application"""

        ColorData()

        frame = SampleFrame()
        self.SetTopWindow(frame)
        frame.Show()

        return True


if __name__ == "__main__":

    app = MainApp()

    print(ColorData.color_dictionary)

    app.MainLoop()



'''
Sample output:

For example
{'AQUAMARINE': wx.Colour(112, 219, 147, 255),
'FIREBRICK': wx.Colour(142, 35, 35, 255)
MEDIUM FOREST GREEN': wx.Colour(107, 142, 35, 255)
RED': wx.Colour(255, 0, 0, 255)
BLACK': wx.Colour(0, 0, 0, 255)
FOREST GREEN': wx.Colour(35, 142, 35, 255)
MEDIUM GOLDENROD': wx.Colour(234, 234, 173, 255)
SALMON': wx.Colour(111, 66, 66, 255)
BLUE': wx.Colour(0, 0, 255, 255)
GOLD': wx.Colour(204, 127, 50, 255)
MEDIUM ORCHID': wx.Colour(147, 112, 219, 255)
SEA GREEN': wx.Colour(35, 142, 107, 255)
BLUE VIOLET': wx.Colour(159, 95, 159, 255)
GOLDENROD': wx.Colour(219, 219, 112, 255)
MEDIUM SEA GREEN': wx.Colour(66, 111, 66, 255)
SIENNA': wx.Colour(142, 107, 35, 255)
BROWN': wx.Colour(165, 42, 42, 255)
GREY': wx.Colour(128, 128, 128, 255)
MEDIUM SLATE BLUE': wx.Colour(127, 0, 255, 255)
SKY BLUE': wx.Colour(50, 153, 204, 255)
CADET BLUE': wx.Colour(95, 159, 159, 255)
GREEN': wx.Colour(0, 255, 0, 255)
MEDIUM SPRING GREEN': wx.Colour(127, 255, 0, 255)
SLATE BLUE': wx.Colour(0, 127, 255, 255)
CORAL': wx.Colour(255, 127, 0, 255)
GREEN YELLOW': wx.Colour(147, 219, 112, 255)
MEDIUM TURQUOISE': wx.Colour(112, 219, 219, 255)
SPRING GREEN': wx.Colour(0, 255, 127, 255)
CORNFLOWER BLUE': wx.Colour(66, 66, 111, 255)
INDIAN RED': wx.Colour(79, 47, 47, 255)
MEDIUM VIOLET RED': wx.Colour(219, 112, 147, 255)
STEEL BLUE': wx.Colour(35, 107, 142, 255)
CYAN': wx.Colour(0, 255, 255, 255)
KHAKI': wx.Colour(159, 159, 95, 255)
MIDNIGHT BLUE': wx.Colour(47, 47, 79, 255)
TAN': wx.Colour(219, 147, 112, 255)
DARK GREY': wx.Colour(47, 47, 47, 255)
LIGHT BLUE': wx.Colour(191, 216, 216, 255)
NAVY': wx.Colour(35, 35, 142, 255)
THISTLE': wx.Colour(216, 191, 216, 255)
DARK GREEN': wx.Colour(47, 79, 47, 255)
LIGHT GREY': wx.Colour(192, 192, 192, 255)
ORANGE': wx.Colour(204, 50, 50, 255)
TURQUOISE': wx.Colour(173, 234, 234, 255)
DARK OLIVE GREEN': wx.Colour(79, 79, 47, 255)
LIGHT STEEL BLUE': wx.Colour(143, 143, 188, 255)
ORANGE RED': wx.Colour(255, 0, 127, 255)
VIOLET': wx.Colour(79, 47, 79, 255)
DARK ORCHID': wx.Colour(153, 50, 204, 255)
LIME GREEN': wx.Colour(50, 204, 50, 255)
ORCHID': wx.Colour(219, 112, 219, 255)
VIOLET RED': wx.Colour(204, 50, 153, 255)
DARK SLATE BLUE': wx.Colour(107, 35, 142, 255)
MAGENTA': wx.Colour(255, 0, 255, 255)
PALE GREEN': wx.Colour(143, 188, 143, 255)
WHEAT': wx.Colour(216, 216, 191, 255)
DARK SLATE GREY': wx.Colour(47, 79, 79, 255)
MAROON': wx.Colour(142, 35, 107, 255)
PINK': wx.Colour(255, 192, 203, 255)
WHITE': wx.Colour(255, 255, 255, 255)
DARK TURQUOISE': wx.Colour(112, 147, 219, 255)
MEDIUM AQUAMARINE': wx.Colour(50, 204, 153, 255)
PLUM': wx.Colour(234, 173, 234, 255)
YELLOW': wx.Colour(255, 255, 0, 255)
DIM GREY': wx.Colour(84, 84, 84, 255)
MEDIUM BLUE': wx.Colour(50, 50, 204, 255)
PURPLE': wx.Colour(176, 0, 255, 255)
YELLOW GREEN': wx.Colour(153, 204, 50, 255)
}

'''
