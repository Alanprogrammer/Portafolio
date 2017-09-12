#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Cryptool 2015  #Alanprogramer
#Modulos
#25565
import hashlib
import requests
import urllib2
import urllib
import json
import base64
from bs4 import BeautifulSoup
#hashmd5 = "21232f297a57a5a743894a0e4a801fc3" #admin #21232f297a57a5a743894a0e4a801fc3

#Lista de sitios#
######################################
#md5.rednoize.com(hashtoolkit.com)
#http://md5.gromweb.com
#http://md5decrypt.net
#http://www.cloudcracker.net
#http://www.websec.it/md5-encrypt-decrypt/
#https://isc.sans.edu/tools/reversehash.html/
#http://www.md5decrypt.org/index/process
#http://md5decryption.com
#http://md5cracker.org
#http://www.md5.net
#http://md5online.net
#http://md5.my-addr.com
#http://md5crack.com
#http://www.netmd5crack.com
#http://md5pass.info
############################
#Clase
class findmd5:
    def __init__(self,md5):
        self.md5 = md5




    # http://md5decryption.com - http://md5cracker.org - http://www.md5.net - http://md5online.net - http://md5.my-addr.com - http://md5crack.com - http://www.netmd5crack.com - http://md5pass.info
    def findmd5cracker(self):
         listdemd5cracket = ['md5cracker.org','md5.net','md5online.net','md5.my-addr.com','md5decryption.com','md5crack','md5pass','netmd5crack']
         try:
            for sitios in listdemd5cracket:
                r = urllib2.urlopen("http://"+"md5cracker.org/api/api.cracker.php?r=5562&database=%s&hash=%s"  %(sitios,self.md5))
                d = json.loads(r.read())
                print d['result'] , "-->",self.md5 , sitios
         except:
             print "not found"



    #http://md5.gromweb.com
    def findgromweb(self):
        try:
            r = urllib2.urlopen('http://'+'md5.gromweb.com/query/%s' % (self.md5))
            print r.read(),"-->",self.md5 ,  "md5.gromweb.com"
        except:
            print "not found"


    #md5.rednoize.com(hashtoolkit.com)
    def findmd5rednoize(self):
        try:
            r = requests.get('http://'+'hashtoolkit.com/reverse-hash?hash=%s'%(self.md5))

            soup = BeautifulSoup(r.text,"html.parser") #html.parser es para que no muestre el mensaje de BeautifulSoup

            txt =soup.find('td',{'class':'res-text'}).span

            print txt.get_text() ,"-->",self.md5 , "md5.rednoize.com"
        except:
            print "not found"

    #http://md5decrypt.net
    def findmd5decryptnet(self):
        try:
            parametros = {'hash':self.md5,'decrypt':''}
            data = urllib.urlencode(parametros)

            request = urllib2.Request("http://md5decrypt.net/",data)

            r = urllib2.urlopen(request)

            soup = BeautifulSoup(r.read(),"html.parser")

            txt = soup.find('fieldset',{"class":"trouve"}).b

            print txt.get_text() ,"-->",self.md5,"md5decrypt.net"
        except:
            print "not found"
    #http://www.cloudcracker.net
    def findmd5cloudcracker(self):
        try:
            parametros = {'inputbox':self.md5 ,'submit':''}
            data = urllib.urlencode(parametros)
            request = urllib2.Request("http://www.cloudcracker.net/",data)
            r  = urllib2.urlopen(request)
            soup = BeautifulSoup(r.read(),"html.parser")
            txt = soup.find('div',{'class':'result'}).input['value']
            print txt ,"-->" ,self.md5 ,"cloudcracker.net"
        except:
            print "not found"
    #http://www.websec.it/md5-encrypt-decrypt/
    def findmd5websecit(self):
        try:
            parametros = {'phrase':self.md5,'task':'Decrypt'}
            data = urllib.urlencode(parametros)
            request = urllib2.Request("http://www.websec.it/md5-encrypt-decrypt/",data)
            r = urllib2.urlopen(request)
            soup = BeautifulSoup(r.read(),"html.parser")
            txt = soup.find('font')
            print txt.get_text() ,"-->",self.md5,"www.websec.it"
        except:
            print "not found"


    #http://www.md5decrypt.org/index/process
    def findmd5md5decryptorg(self):
        #'jscheck':'1448088600_d6cb4a550b6cb661d2b97ac9c5f74e46'
        try:
            r = requests.get('http://www.md5decrypt.org')
            soup = BeautifulSoup(r.text,'html.parser')
            jscheck = soup.find_all('script')
            jscheck = jscheck[6].get_text()
            jscheck = jscheck.replace("var jscheck=","")
            jscheck = jscheck.replace("'","")
            jscheck = jscheck.replace(";","")
            ##############################################
            parametros = {'jscheck':jscheck,'value':base64.b64encode(self.md5),'operation':'MD5D'}
            r = requests.post('http://www.md5decrypt.org/index/process',parametros)
            d = json.loads(r.text)
            print d['body'] , "-->" , self.md5 , "www.md5decrypt.org"
        except:
            print "not found"


            '''
    #https://isc.sans.edu/tools/reversehash.html/
    def findmd5iscsansedu(self):

        try:
            #Cookie :guestkey=202abde87dcbf03fd238b5f413383d19; dshield=7vlafp8bhdev8d4jg031evug35
            parametros = {'token':'f71a85472988cbeda04a2cf6fe3c4933e08641ef','text':self.md5}
            data = urllib.urlencode(parametros)
            opener = urllib2.build_opener()
            opener.addheaders.append(('Cookie','guestkey=202abde87dcbf03fd238b5f413383d19; dshield=7vlafp8bhdev8d4jg031evug35'))
            r = opener.open('https://isc.sans.edu/tools/reversehash.html',data)
            #request = urllib2.Request("https://isc.sans.edu/tools/reversehash.html/")
            #r = urllib2.urlopen(request)
            soup = BeautifulSoup(r.read(),'html.parser')
            txt = soup.find_all('p')

            txt = txt[3].get_text()
            txt =txt.replace('md5 hash','')
            txt =txt.replace(self.md5,'')
            txt =txt.replace('=','')
            txt = txt.replace(' ','')
            print txt, "-->" ,self.md5
        except:
            print 'not found'

            '''





def Findmd5Crytool(hashmd5):
    #ejecucion -*-
    findcrack =findmd5(hashmd5)
    findcrack.findmd5cracker()
    findcrack.findgromweb()
    findcrack.findmd5rednoize()
    findcrack.findmd5decryptnet()
    findcrack.findmd5cloudcracker()
    findcrack.findmd5websecit()
    findcrack.findmd5md5decryptorg()
    #findcrack.findmd5iscsansedu()
