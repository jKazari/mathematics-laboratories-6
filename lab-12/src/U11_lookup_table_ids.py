''' 
U11_lookup_table_ids.py
'''

import wx

# jako słownik
wpa_id_numbers = {
        'ID_1': wx.NewIdRef(),
        'ID_2': wx.NewIdRef(),
        'ID_3': wx.NewIdRef(),
        'ID_4': wx.NewIdRef(),
}

# jako klasa
class wpa_id_letters:

    ID_A = wx.NewIdRef()
    ID_X = wx.NewIdRef()
    ID_Y = wx.NewIdRef()
    ID_Z = wx.NewIdRef()

# jako lista
wpa_id_list = wx.NewIdRef(5)


# jeszcze inna wersją jest staromodne zdefiniowanie jako wolnych zmiennych

class MainFrame(wx.Frame):

    def __init__(self):

        # pass argument to the constructor os the base class
        super().__init__(parent=None,title='MWE',pos=(1000, 200))

        self.st_counter = wx.StaticText(self,size=(200,25),
                                        style=wx.ST_NO_AUTORESIZE|wx.ALIGN_CENTER)
        self.st_counter.SetLabel('No events yet')
        self.st_counter.SetBackgroundColour((150,120,110))


        self.sizer = wx.GridSizer(3,3,10,10)

        self.sizer.Add(wx.Button(self,id = wpa_id_numbers['ID_1'],label = '1'))
        self.sizer.Add(wx.Button(self,id = wpa_id_numbers['ID_2'],label = '2'))
        self.sizer.Add(wx.Button(self,id = wpa_id_numbers['ID_3'],label = '3'))

        self.sizer.Add(wx.Button(self,id = wpa_id_letters.ID_X,label = 'X'))
        self.sizer.Add(wx.Button(self,id = wpa_id_letters.ID_Y,label = 'Y'))
        self.sizer.Add(wx.Button(self,id = wpa_id_letters.ID_Z,label = 'Z'))


        self.sizer.Add(wx.Button(self,id = wpa_id_list[0],label = 'l0'))
        self.sizer.Add(wx.Button(self,id = wpa_id_list[1],label = 'l1'))
        self.sizer.Add(wx.Button(self,id = wpa_id_list[2],label = 'l2'))


        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.main_sizer.Add(self.st_counter,0,wx.ALL | wx.ALIGN_CENTER,10)
        self.main_sizer.Add(self.sizer)

        self.sizer.SetSizeHints(self)
        self.SetSizer(self.main_sizer)


        self.Bind(wx.EVT_BUTTON,self.OnButtonClick)


    def OnButtonClick(self,event):

        self.st_counter.SetLabel( 'GetId() ={}'.format(event.GetId()) )

        print( 'GetId() ={}'.format(event.GetId())  )


        id = event.GetId()

        if id == wpa_id_numbers['ID_1']:
             self.st_counter.SetBackgroundColour((255,50,0))
        elif id == wpa_id_numbers['ID_2']:
             self.st_counter.SetBackgroundColour((255,100,0))
        elif id == wpa_id_numbers['ID_3']:
             self.st_counter.SetBackgroundColour((255,150,0))
        else:
            self.st_counter.SetBackgroundColour((150,120,110))

        # w tym programi mamy pewne ograniczenie gdyż
        # tylko wersja używająca klasy może by użyta w match
        # pozostałe też możnaby użyć z match
        # ale trzeba je najpierw schować w scope (np.: w module) normalnei nie jest to problem
        # ćwiczenie: sprawdzić, ze po schowaniu do moduły każdy sposób działa z match
        #
        # problemem jest sposób działania konstrukcji match która stara się dopasować
        # to co jest w case do wzorca podanego w match
        # i rozumie napisy dosłownie
        # https://peps.python.org/pep-0636/#matching-multiple-values

        match id:
            case wpa_id_letters.ID_X:
                self.st_counter.SetBackgroundColour((0,255,50))
            case wpa_id_letters.ID_Y:
                self.st_counter.SetBackgroundColour((0,255,100))
            case wpa_id_letters.ID_Z:
                self.st_counter.SetBackgroundColour((0,255,150))

        if id == wpa_id_list[0]:
            self.st_counter.SetBackgroundColour((0,50,255))
        elif id == wpa_id_list[1]:
            self.st_counter.SetBackgroundColour((0,100,255))
        elif id == wpa_id_list[2]:
            self.st_counter.SetBackgroundColour((0,150,255))


class MyApp(wx.App):
    
    def OnInit(self):
        """ Initialise the main GUI Application"""
    
        frame = MainFrame()
        frame.Show()

        return True



if __name__ == "__main__":

    app = MyApp()

    print('--- wpa_id_numbers ---')
    print(wpa_id_numbers)
    print(wpa_id_numbers['ID_1'])
    print( int(wpa_id_numbers['ID_1']) )

    print('--- wpa_id_letters ---')
    print( wpa_id_letters)
    print( int(wpa_id_letters.ID_Z) )

    print('--- wpa_id_list ---')
    print( wpa_id_list)
    print( wpa_id_list[0] )
    print( int(wpa_id_list[0]) )

    app.MainLoop()
