#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Cryptool 2015 #Alanprogramer
#Modulos
from bs4 import BeautifulSoup
import requests

data = {'a':'ascii',
'b':'bin',
'c':'hex',
'd':'b64',
'e':'char',
'f':'oct'

}

def RedirCryptool(data,value):
    try:
        parametros =  {data:value}
        r = requests.post("http://redir.dasumo.com/hex/",parametros)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text,"html.parser")
            txt = soup.find_all("form")
            for lst in txt:
                print lst.get_text()
        else:
            print "Error"
    except:
        print "Error"
