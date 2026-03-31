"""
Ten skrypt ma służyć jako demonstracja modułu borok

Zadanie: zaimportuj moduł borok
"""

import borok

print(borok.__doc__\
	,borok.hasiok.__doc__\
	,borok.bajtel.__doc__\
		,borok.bajtel.flek.__doc__\
		,borok.bajtel.larmo.__doc__\
	,borok.knefel.__doc__\
	,borok.pieron.__doc__\
		,
borok.pieron.giboj.__doc__\
,sep='\n')


borok.Greetings()
borok.bajtel.Greetings()
borok.bajtel.larmo.Greetings()
