''' 
E01_hello_word.py
'''

import wx

# Create the Application Object
app = wx.App()

# Now create a Frame (representing the top-level window)
frame = wx.Frame(parent=None, title=' Hello World')
# And add a text label to it
text = wx.StaticText(parent=frame, label= 'Hello Python')

# Display the window (frame)
frame.Show()
# Start the event loop
app.MainLoop()

