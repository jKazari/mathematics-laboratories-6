''' 
E15_kbd_events.py
'''

import wx

class MainFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='Keyboard events',
                            pos=(400, 200),size=(400,400) )


        self.label_A = wx.StaticText(self,pos=(1,1),size=(20,20),label='A')
        self.label_A.SetBackgroundColour((125,50,200))

        self.label_B = wx.StaticText(self,pos=(200,380),size=(100,20),label='B')
        self.label_B.SetBackgroundColour((200,50,125))

        #ALERT
        # this is a dirty trick needed in Linux
        # for unknown reason w.Frame does not catch kbd event
        # but some other widgets do
        # on Windows you may safely use only first part

        if wx.GetOsDescription().startswith('Windows'):
            pass
            self.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown,self)

        else:
            self.panel = wx.Panel(self,pos=(200,200))
            self.panel.SetFocus()
            self.panel.Bind(wx.EVT_KEY_DOWN,self.OnKeyDown)


    def OnKeyDown(self, event):

        Ukeycode = event.GetUnicodeKey()
        keycode = event.GetKeyCode()

        print('In Frame OnKeyDown {}/{}'.format(keycode,Ukeycode))

        # (STEP1)
#         if Ukeycode != wx.WXK_NONE:
#
#             if event.HasAnyModifiers():
#                 pass
#                 # (STEP2)
#                 # MOD_SHIFT_CTRL = wx.MOD_SHIFT & wx.MOD_CONTROL
#                 # match event.GetModifiers():
#                 #     case wx.MOD_ALT:
#                 #         self.label_A.SetLabel( "Alt+%c"%Ukeycode )
#                 #     case wx.MOD_CONTROL:
#                 #         self.label_A.SetLabel( "Ctrl+%c"%Ukeycode )
#                 #     case wx.MOD_SHIFT:
#                 #         self.label_A.SetLabel( "Shift+%c"%Ukeycode )
#                 #     case MOD_SHIFT_CTRL:
#                 #         self.label_A.SetLabel( "Shift+Ctrl+%c"%Ukeycode )
#             else:
#                 # It's a printable character
#                 self.label_A.SetLabel( "%c"%Ukeycode )
#
#         else:
#             # It's a special key, deal with all the known ones:
#             if event.IsKeyInCategory(wx.WXK_CATEGORY_ARROW):
#
#                 match keycode:
#                     case wx.WXK_LEFT:
#                         self.label_B.SetLabel('left arrow')
#                     case wx.WXK_RIGHT:
#                         self.label_B.SetLabel('right arrow')
#                     case wx.WXK_UP:
#                         self.label_B.SetLabel('up arrow')
#                     case wx.WXK_DOWN:
#                         self.label_B.SetLabel('down arrow')
#
#             elif keycode == wx.WXK_F1:
#                 # give help ...
#                 self.label_B.SetLabel('F1')


class MyApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        self.frame = MainFrame()
        self.frame.Show()

        return True

if __name__ == "__main__":

    app = MyApp()



    app.MainLoop()
