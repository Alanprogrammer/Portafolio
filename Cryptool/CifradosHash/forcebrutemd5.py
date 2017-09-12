#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Cryptool 2015  #Alanprogramer
#Modulos
import hashlib
caracteres =  {'a':'abcdefghijklmnopqrstuvwxyz','A':'ABCDEFGHIJKLMNOPQRSTUVWXYZ','b':'1234567890','c':'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'}
#hash_md5 = "900150983cd24fb0d6963f7d28e17f72"
#logitudMinimo = 1
#logintud = 9
inicio = False
def ForceBruteCryptool(logintud,logintud_maxima,hash_md5,caracteres):
    if inicio == True:
        while logintud <= logintud_maxima:
            try:
                contadores = []
                for i in range(logintud):
                    contadores.append(0)
                final = False
                while not final:
                    palabra = []
                    for i in range(logintud):
                        palabra.append(caracteres[contadores[i]])
                    palabra_formada="".join(palabra)
                    if True:
                        HASH = hashlib.md5(palabra_formada).hexdigest()
                        if HASH == hash_md5:
                            print "HASH  :"+HASH
                            print "VALOR :"+palabra_formada
                            raise KeyboardInterrupt
                        else:
                            print HASH + "==" + palabra_formada
                    actual = logintud -1
                    contadores[actual] = contadores[actual]+ 1

                    while contadores[actual] == len(caracteres) and not final:
                        if(actual==0):
                            final=True
                        else:
                            contadores[actual] = 0
                            actual = actual-1
                            contadores[actual] = contadores[actual] + 1
                logintud =  logintud +1

            except KeyboardInterrupt:
                print "\033[1;34mGood bye\033[1;m"
                final = True
                logintud = logintud_maxima +1
#ForceBruteCryptool(logitudMinimo,logintud,hash_md5,caracteres['a'])
