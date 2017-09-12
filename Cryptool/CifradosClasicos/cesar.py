#!/usr/bin/env python
#Cryptool 2015 #Alanprogramer
#-*- coding:utf-8 -*-
def CifradoCesarCryptool(mensaje):
    alfabeto = "ZYXWVUTSRQPONMLKJIHGFEDCBA" #
    for llave in range(len(alfabeto)):

    	CifradoTerminadoCesar = ''

    	for simbolo in mensaje:
    		if simbolo in alfabeto:
    			num = alfabeto.find(simbolo)
    			num = num - llave

    			if num < 0:
    				num + len(alfabeto)
    			CifradoTerminadoCesar = CifradoTerminadoCesar + alfabeto[num]
    		else:
    			CifradoTerminadoCesar =  CifradoTerminadoCesar +   simbolo

    	print ("\033[1;31mROT-%s:\n\033[1;m  %s" %(llave,CifradoTerminadoCesar))
