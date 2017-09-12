#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Cryptool 2015 #Alanprogramer
 #Modulos
import hashlib
final =0
def dicmd5Cryptool(diccionario,md5):
	global final

	try:
		dic = open(diccionario,"r")
		if len(md5) == 32:
			for lines in dic.xreadlines():
				palabra = lines.replace("\n","")
				dicmd5 = hashlib.md5(palabra).hexdigest()
                #Comparacion entre hash == hash(txt)
				if md5 == dicmd5:
					print "\033[1;34mHash:\033[1;m ",md5,"\033[1;34m---->\033[1;m",palabra
					final = 1
			if final == 0:
				print "No hubo resultado"

		else:
			print "\033[1;31mSeguro que es un hash md5:\033[1;m ",md5

	except IOError:
		print "\033[1;31No existe el diccionario:\033[1;m ",diccionario
