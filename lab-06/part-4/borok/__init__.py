"""This file (borok/__init__.py) is a part of borok package"""

# packages borok.<bajtel|knefel|pieron>
from . import bajtel
from . import knefel
from . import pieron

# module borok.hasiok
from . import hasiok
    

def Greetings():
    print('Hello from ' + __name__ + '.\n\tMy file is ' + __file__)
