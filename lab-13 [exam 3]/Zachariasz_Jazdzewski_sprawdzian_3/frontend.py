import math
import wx
import backend

LAYOUT = [
    'xʸ', '√',  'log', '÷',
    '7',  '8',  '9',   '×',
    '4',  '5',  '6',   '-',
    '1',  '2',  '3',   '+',
    'C',  '0',  '.',   '=',
]

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
        
        font = self.display.GetFont()
        font.SetPointSize(20)
        self.display.SetFont(font)

        self.grid = wx.GridSizer(5, 4, 4, 4)
        for label in LAYOUT:
            btn = wx.Button(self, id=BUTTON_IDS[label], label=label, size=(50, 50))

            btn_font = btn.GetFont()
            btn_font.SetPointSize(14)
            btn.SetFont(btn_font)

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

        outer = wx.BoxSizer(wx.VERTICAL)
        outer.Add(self.display, 0, wx.ALL | wx.EXPAND, 8)
        outer.Add(self.grid, 0, wx.ALL, 8)

        self.SetSizerAndFit(outer)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick)

    def _reset_state(self):
        self._current = '0'
        self._stored = None
        self._pending_op = None
        self._just_evaluated = False

    def _update_display(self):
        self.display.SetLabel(self._current)
        
        font_size = 20 if len(self._current) <= 8 else 16
        font = self.display.GetFont()
        font.SetPointSize(font_size)
        self.display.SetFont(font)

    def _safe_float(self, s):
        try:
            return float(s)
        except ValueError:
            return 0.0

    def _format(self, val):
        if math.isnan(val) or math.isinf(val):
            return 'Undefined'
        if val == int(val) and abs(val) < 1e15:
            return str(int(val))
        return str(val)

    def _compute(self):
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
        label = None
        for k, v in BUTTON_IDS.items():
            if v == event.GetId():
                label = k
                break
        
        if label is None:
            return

        if label.isdigit():
            if self._current == 'Undefined' or self._just_evaluated or self._current == '0':
                self._current = label
                self._just_evaluated = False
            else:
                self._current += label

        elif label == '.':
            if '.' not in self._current and self._current != 'Undefined':
                if self._just_evaluated:
                    self._current = '0.'
                    self._just_evaluated = False
                else:
                    self._current += '.'

        elif label in ('+', '-', '×', '÷', 'xʸ'):
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

        elif label == 'log':
            if self._current != 'Undefined':
                try:
                    result = backend.logarithm(self._safe_float(self._current))
                    self._current = self._format(result)
                except ValueError:
                    self._current = 'Undefined'
                self._just_evaluated = True

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
