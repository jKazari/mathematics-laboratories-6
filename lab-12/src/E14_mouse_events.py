''' 
E14_mouse_events.py
'''

import wx

class MainFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='Mouse events',
                            pos=(1000, 200),size=(400,400) )


        self.label_A = wx.StaticText(self,pos=(1,1),size=(20,20),label='A')
        self.label_A.SetBackgroundColour((125,50,200))

        self.label_B = wx.StaticText(self,pos=(380,380),size=(20,20),label='B')
        self.label_B.SetBackgroundColour((200,50,125))

        self.Bind(wx.EVT_LEFT_DOWN,self.OnMouseLeftDown)
        self.Bind(wx.EVT_LEFT_UP,self.OnMouseLeftUp)
        self.Bind(wx.EVT_LEFT_DCLICK,self.OnMouseLeftDCLickDown)
        self.Bind(wx.EVT_RIGHT_DOWN,self.OnMouseRightDown)
        self.Bind(wx.EVT_RIGHT_UP,self.OnMouseRightUp)

        # (STEP2)
        # self.Bind(wx.EVT_MOTION,self.OnMouseMove)


    def OnMouseLeftDown(self,event):
        print('OnMouseLeftDown')

        self.label_A.SetBackgroundColour((0,255,0))

        # (STEP4)
        # event.Skip()

    def OnMouseLeftUp(self,event):
        print('OnMouseLeftUp')

        self.label_A.SetBackgroundColour((0,255,255))

    def OnMouseLeftDCLickDown(self,event):
        print('OnMouseLeftDCLickDown')


    def OnMouseRightDown(self,event):
        # print('OnMouseRightDown')

        # (STEP1)
        # position = event.GetPosition()
        # print('OnMouseRightDown at {}'.format(position))
        # self.label_B.SetPosition(position)


    def OnMouseRightUp(self,event):
        print('OnMouseRightUp')


    # (STEP2)
    # def OnMouseMove(self,event):
    #
    #     print('OnMouseMove')
    #     if event.Dragging():
    #         self.label_B.SetPosition(event.GetPosition())
    #
class MyApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = MainFrame()
        frame.Show()


        # (STEP3)
        # self.Bind(wx.EVT_LEFT_DOWN,self.OnMouseLeftDown)

        return True

    # (STEP3)
    # def OnMouseLeftDown(self,event):
    #     print('App catch EVT_LEFT_DOWN')


if __name__ == "__main__":

    app = MyApp()
    app.MainLoop()
