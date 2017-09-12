#!/usr/bin/env python
#Cryptool 2015 #Alanprogramer
#-*- coding:utf-8 -*-
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def CifrarVigereneCryptool(mensaje,clave):
    i = 0
    txt_final = ""
    for letra in mensaje:
        if letra == "A" or letra == "B" or  letra == "C" or letra == "D" or letra == "E" or letra == "F" or letra == "G" or letra == "H" or letra == "I" or letra == "J" or letra == "K" or letra == "L" or letra == "M" or letra == "N" or letra == "O" or letra == "P" or letra == "Q" or letra == "R" or letra == "S"or letra == "T"or letra == "U"or letra == "V"or letra == "W" or letra == "X"or letra == "Y"or letra == "Z":
            suma =  abc.find(letra) + abc.find(clave[i % len(clave)])
            dato = int(suma)  % len(abc)

            txt_final =  txt_final + str(abc[dato])
            i = i+1


        else:
            txt_final+=letra

    print txt_final


def DescifrarVigereneCryptool(mensaje,clave):
        i = 0
        txt_final = ""
        for letra in mensaje:
            if letra == "A" or letra == "B" or  letra == "C" or letra == "D" or letra == "E" or letra == "F" or letra == "G" or letra == "H" or letra == "I" or letra == "J" or letra == "K" or letra == "L" or letra == "M" or letra == "N" or letra == "O" or letra == "P" or letra == "Q" or letra == "R" or letra == "S"or letra == "T"or letra == "U"or letra == "V"or letra == "W" or letra == "X"or letra == "Y"or letra == "Z":
                suma =  abc.find(letra) - abc.find(clave[i % len(clave)])
                dato = int(suma)  % len(abc)

                txt_final =  txt_final + str(abc[dato])
                i = i+1


            else:
                txt_final+=letra

        print txt_final
