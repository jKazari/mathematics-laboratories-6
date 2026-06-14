import math
import wx
import backend

# Button labels arranged in a grid
LAYOUT = [
    'xʸ', '√',  'log', '÷',
    '7',  '8',  '9',   '×',
    '4',  '5',  '6',   '-',
    '1',  '2',  '3',   '+',
    'C',  '0',  '.',   '=',
]

# Each button label gets a unique wx ID so we can tell which was clicked
BUTTON_IDS = {label: wx.NewIdRef() for label in LAYOUT}

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Calculator', pos=(650, 200))
        self._reset_state()
        self._build_ui()

    def _build_ui(self):
        self.display = wx.StaticText(
            self, size=(212, 50),
            style=wx.ST_NO_AUTORESIZE | wx.ALIGN_RIGHT
        )
        self.display.SetLabel('0')
        self.display.SetBackgroundColour(wx.BLACK)
        self.display.SetForegroundColour(wx.WHITE)
        
		# Change display font size
        font = self.display.GetFont()
        font.SetPointSize(20)
        self.display.SetFont(font)

        # Button grid (5 rows x 4 columns, 4px gaps)
        self.grid = wx.GridSizer(5, 4, 4, 4)
        for label in LAYOUT:
            btn = wx.Button(self, id=BUTTON_IDS[label], label=label, size=(50, 50))

            # Change button font size
            btn_font = btn.GetFont()
            btn_font.SetPointSize(14)
            btn.SetFont(btn_font)

            # Color-code buttons by category
            if label in ('=', '÷', '×', '-', '+'):
                btn.SetBackgroundColour('#FF9500')
                btn.SetForegroundColour(wx.WHITE)
            elif label in ('xʸ', '√', 'log'):
                btn.SetBackgroundColour('#1C1C1C')
                btn.SetForegroundColour(wx.WHITE)
            elif label == 'C':
                btn.SetBackgroundColour('#505050')
                btn.SetForegroundColour(wx.WHITE)

            self.grid.Add(btn)

        # Stack display and grid vertically with 8px padding around each
        outer = wx.BoxSizer(wx.VERTICAL)
        outer.Add(self.display, 0, wx.ALL | wx.EXPAND, 8)
        outer.Add(self.grid, 0, wx.ALL, 8)

        self.SetSizerAndFit(outer)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick)

    def _reset_state(self):
        # Called on startup and when C is pressed
        self._current = '0'       		# number shown on display
        self._stored = None       		# first operand waiting for second
        self._pending_op = None   		# which operator was pressed
        self._just_evaluated = False	# True right after pressing = or unary operators

    def _update_display(self):
        self.display.SetLabel(self._current)
        
        # Shrink font for long numbers so they fit the display
        font_size = 20 if len(self._current) <= 8 else 16
        font = self.display.GetFont()
        font.SetPointSize(font_size)
        self.display.SetFont(font)

    def _safe_float(self, s):
        # Convert string to float. Returns 0.0 if conversion fails
        try:
            return float(s)
        except ValueError:
            return 0.0

    def _format(self, val):
        # Turn a float into a clean string for the display
        if math.isnan(val) or math.isinf(val):
            return 'Undefined'
        if val == int(val) and abs(val) < 1e15:
            return str(int(val))
        return str(val)

    def _compute(self):
        # Apply the pending binary operator to stored and current values
        if self._pending_op is None or self._stored is None:
            return

        a = self._stored
        b = self._safe_float(self._current)

        try:
            if self._pending_op == '+':
                result = backend.add(a, b)
            elif self._pending_op == '-':
                result = backend.subtract(a, b)
            elif self._pending_op == '×':
                result = backend.multiply(a, b)
            elif self._pending_op == '÷':
                result = backend.divide(a, b)
            elif self._pending_op == 'xʸ':
                result = backend.power(a, b)
            else:
                return

            self._current = self._format(result)
            self._stored = result
            self._just_evaluated = True

        except (ValueError, OverflowError):
            self._current = 'Undefined'
            self._stored = None
            self._just_evaluated = True

    def OnButtonClick(self, event):
        # Find which button was clicked by matching the event ID
        label = None
        for k, v in BUTTON_IDS.items():
            if v == event.GetId():
                label = k
                break
        
        if label is None:
            return

        if label.isdigit():
            # Replace display if starting fresh, otherwise append the digit
            if self._current == 'Undefined' or self._just_evaluated or self._current == '0':
                self._current = label
                self._just_evaluated = False
            else:
                self._current += label

        elif label == '.':
            # Add decimal point only if there isn't one already
            if '.' not in self._current and self._current != 'Undefined':
                if self._just_evaluated:
                    self._current = '0.'
                    self._just_evaluated = False
                else:
                    self._current += '.'

        elif label in ('+', '-', '×', '÷', 'xʸ'):
            # Chain calculations: compute previous op before storing new one
            if self._pending_op is not None and not self._just_evaluated:
                self._compute()
            if self._current != 'Undefined':
                self._stored = self._safe_float(self._current)
                self._pending_op = label
                self._just_evaluated = True

        elif label == '√':
            if self._current != 'Undefined':
                try:
                    result = backend.sqrt(self._safe_float(self._current))
                    self._current = self._format(result)
                except ValueError:
                    self._current = 'Undefined'
                self._just_evaluated = True

        # elif label == 'log':
        #     if self._current != 'Undefined':
        #         try:
        #             result = backend.logarithm(self._safe_float(self._current))
        #             self._current = self._format(result)
        #         except ValueError:
        #             self._current = 'Undefined'
        #         self._just_evaluated = True

        elif label == '=':
            self._compute()
            self._pending_op = None

        elif label == 'C':
            self._reset_state()

        self._update_display()

class MyApp(wx.App):
    def OnInit(self):
        MainFrame().Show()
        return True
