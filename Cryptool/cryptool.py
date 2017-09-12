#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Cryptool 2015 #Alanprogramer
#Modulos
import sys,os,base64,hashlib
##################################
import CifradosClasicos.cesar
import CifradosClasicos.vigenere
##################################
import CifradosHash.diccionariomd5
import CifradosHash.forcebrutemd5
import CifradosHash.findhashmd5
##################################
import SistemaNum.redir
#Inicio de Software
#Home
def main():
    try:
        os.system('clear')
        print '''
    ###############################################################
                                          dP                     dP
                                          88                     88
    .d8888b. 88d888b. dP    dP 88d888b. d8888P .d8888b. .d8888b. 88
    88'  `"" 88'  `88 88    88 88'  `88   88   88'  `88 88'  `88 88
    88.  ... 88       88.  .88 88.  .88   88   88.  .88 88.  .88 88
    `88888P' dP       `8888P88 88Y888P'   dP   `88888P' `88888P' dP
                           .88 88
                       d8888P  dP
    ###############################################################
    \033[1;34mHecho por:\033[1;mAlanprogrammer \033[1;34mPara:\033[1;mHacking Publico
     \033[1;34mVersion:\033[1;mBeta 0.12
        '''
        def homeinicio():
            #Menu de Cryptool#
            while True:
                print "\033[1;95m+++++++Menu++++++++++++++++++++++++++++++++++++++++++++++++\033[1;m"
                print '''
\033[1;34m1->\033[1;mSistema de Numeracion(Binario,Octal,Base64,Decimal,Hexadecimal)
\033[1;34m2->\033[1;mCriptografia clasica
\033[1;34m3->\033[1;mHash

\033[1;34m99->\033[1;mExit

Seleccione una opcion
                '''
                menuOptions = raw_input('\033[1;32mCryptool-> \033[1;m')

                def sistemadenumerionmenu():
                    #Menu de sistema de numeracion#
                    while menuOptions == "1":
                        print "\033[1;95m+++++++Sistema de Numeracion+++++++++++++++++++++++++++++++\033[1;m"
                        print '''
\033[1;34m1->\033[1;mTexto
\033[1;34m2->\033[1;mBinario
\033[1;34m3->\033[1;mOctal
\033[1;34m4->\033[1;mBase64
\033[1;34m5->\033[1;mDecimal
\033[1;34m6->\033[1;mHexadecimal

\033[1;34m98->\033[1;mBack
\033[1;34m99->\033[1;mExit

Seleccione una Opcion:
                        '''
                        MenuSisnumOptions = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Sistema de Numeracion)\033[1;m\033[1;32m->\033[1;m')


                        #Texto
                        if MenuSisnumOptions == "1":
                            print "Texto que quiere Cifrar"
                            messageSistemaNum = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Sistema de Numeracion)\033[1;m\033[1;32m->\033[1;m')
                            if messageSistemaNum != "":
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                                SistemaNum.redir.RedirCryptool(SistemaNum.redir.data['a'],messageSistemaNum)
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                            else:
                                print "No puso nada"
                        #Binario
                        elif MenuSisnumOptions == "2":
                            print "Binario que quiere Traducir"
                            messageSistemaNum = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Sistema de Numeracion)\033[1;m\033[1;32m->\033[1;m')
                            if messageSistemaNum != "":
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                                SistemaNum.redir.RedirCryptool(SistemaNum.redir.data['b'],messageSistemaNum)
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                            else:
                                print "No puso nada"
                        #Octal
                        elif MenuSisnumOptions == "3":
                            print "Octal que quiere Traducir"
                            messageSistemaNum = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Sistema de Numeracion)\033[1;m\033[1;32m->\033[1;m')
                            if messageSistemaNum != "":
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                                SistemaNum.redir.RedirCryptool(SistemaNum.redir.data['f'],messageSistemaNum)
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                            else:
                                print "No puso nada"
                        #Base64
                        elif MenuSisnumOptions == "4":
                            print "Base64 que quiere Traducir"
                            messageSistemaNum = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Sistema de Numeracion)\033[1;m\033[1;32m->\033[1;m')
                            if messageSistemaNum != "":
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                                SistemaNum.redir.RedirCryptool(SistemaNum.redir.data['d'],messageSistemaNum)
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                            else:
                                print "No puso nada"
                        #Decimal
                        elif MenuSisnumOptions == "5":
                            print "Decimal que quiere Traducir"
                            messageSistemaNum = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Sistema de Numeracion)\033[1;m\033[1;32m->\033[1;m')
                            if messageSistemaNum != "":
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                                SistemaNum.redir.RedirCryptool(SistemaNum.redir.data['e'],messageSistemaNum)
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                            else:
                                print "No puso nada"
                        #Hexadecimal
                        elif MenuSisnumOptions == "6":
                            print "Hexadecimal que quiere Traducir"
                            messageSistemaNum = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Sistema de Numeracion)\033[1;m\033[1;32m->\033[1;m')
                            if messageSistemaNum != "":
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                                SistemaNum.redir.RedirCryptool(SistemaNum.redir.data['c'],messageSistemaNum)
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                            else:
                                print "No puso nada"

                        #Comandos generales
                        elif MenuSisnumOptions == "98":
                            homeinicio()
                        elif MenuSisnumOptions == "99":
                            os.system('clear')
                            sys.exit(1)

                def menucriptografiaclasica():
                    #Menu de criptografia Clasica
                    while menuOptions == "2":
                        print "\033[1;95m+++++++Criptografia Clasica+++++++++++++++++++++++++++++++\033[1;m"
                        print '''
\033[1;34m1->\033[1;mCifrado Cesar
\033[1;34m2->\033[1;mCifrado Vigenere

\033[1;34m98->\033[1;mBack
\033[1;34m99->\033[1;mExit

Seleccione una Opcion:
                        '''
                        MenuCripClasOptions = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Criptografia Clasica)\033[1;m\033[1;32m->\033[1;m')
                        if MenuCripClasOptions == "1":
                            print "Texto que quiere Cifrar"
                            cifradocesarmessage = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Cifrado Cesar)\033[1;m\033[1;32m->\033[1;m')
                            cifradocesarmessage = cifradocesarmessage.upper()
                            print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                            CifradosClasicos.cesar.CifradoCesarCryptool(cifradocesarmessage)
                            print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                        if MenuCripClasOptions == "2":
                            print '''
\033[1;34m1->\033[1;mCifrar
\033[1;34m2->\033[1;mDecifrar

Seleccione una Opcion
                            '''
                            optionsvigerene = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Cifrado Vigenere)\033[1;m\033[1;32m->\033[1;m')
                            if optionsvigerene == "1":
                                print "Texto que quiere Cifrar"
                                messagevigerene =   raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Cifrado Vigenere)\033[1;m\033[1;32m->\033[1;m')
                                print "Clave"
                                clavevigerene =  raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Cifrado Vigenere)\033[1;m\033[1;32m->\033[1;m')
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                                CifradosClasicos.vigenere.CifrarVigereneCryptool(messagevigerene.upper(),clavevigerene.upper())
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                            elif optionsvigerene == "2":
                                print "Texto que quiere Descifrar"
                                messagevigerene =   raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Cifrado Vigenere)\033[1;m\033[1;32m->\033[1;m')
                                print "Clave"
                                clavevigerene =  raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Cifrado Vigenere)\033[1;m\033[1;32m->\033[1;m')
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"
                                CifradosClasicos.vigenere.DescifrarVigereneCryptool(messagevigerene.upper(),clavevigerene.upper())
                                print "\033[1;34m+++++++Resultados++++++++++++++++++++++++++++++\033[1;m"


                        #Comandos generales
                        if MenuCripClasOptions == "98":
                            homeinicio()
                        elif MenuCripClasOptions == "99":
                            os.system('clear')
                            sys.exit(1)

                #Menu de Hash :p
                def menudehash():
                    while menuOptions == "3":
                        print "\033[1;95m+++++++Hash++++++++++++++++++++++++++++++++++++++++++++++++\033[1;m"
                        print '''
\033[1;34m1->\033[1;mMD5

\033[1;34m98->\033[1;mBack
\033[1;34m99->\033[1;mExit
Seleccione una Opcion:
                        '''
                        MenuHashoptions = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Hash)\033[1;m\033[1;32m->\033[1;m')
                        while MenuHashoptions == "1":
                            print '''
\033[1;34m1->\033[1;mCifrar
\033[1;31m--Descifrar--\033[1;m
\033[1;34m2->\033[1;mFuerza Bruta
\033[1;34m3->\033[1;mDiccionario
\033[1;34m4->\033[1;mBuscar Hash

\033[1;34m98->\033[1;mBack
\033[1;34m99->\033[1;mExit
Seleccione una Opcion
                            '''

                            md5options = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(HashMd5)\033[1;m\033[1;32m->\033[1;m')
                            if md5options == "1":
                                print "Texto que quiere Cifrar"
                                cifrartxt = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(CifrarMd5)\033[1;m\033[1;32m->\033[1;m')

                                print hashlib.md5(cifrartxt).hexdigest()



                            elif md5options == "2":
                                print " Selecciona Minimo de Caracteres"
                                logitud_min =  raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Fuerza Bruta)\033[1;m\033[1;32m->\033[1;m')
                                print "Selecciona Maximo de Caracteres"
                                logitud_max = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Fuerza Bruta)\033[1;m\033[1;32m->\033[1;m')
                                print "Seleccione un Hash"
                                hashmd5 = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Fuerza Bruta)\033[1;m\033[1;32m->\033[1;m')

                                print '''
Seleccione Caracteres para fuerza bruta
{'a':'abcdefghijklmnopqrstuvwxyz',
 'A':'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
 'b':'1234567890',
 'c':'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'}
                                '''
                                caracteres_input = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(Fuerza Bruta)\033[1;m\033[1;32m->\033[1;m')

                                if logitud_min  and logitud_max  and hashmd5  and caracteres_input:
                                    CifradosHash.forcebrutemd5.inicio = True
                                    CifradosHash.forcebrutemd5.ForceBruteCryptool(int(logitud_min),int(logitud_max),hashmd5,CifradosHash.forcebrutemd5.caracteres[caracteres_input])

                                else:
                                    pass

                            elif md5options == "3":
                                print "Seleccione un Diccionario"
                                dicmd5 = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(HashMd5Dic)\033[1;m\033[1;32m->\033[1;m')
                                print "Seleccione un Hash"
                                hashmd5 = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(HashMd5Dic)\033[1;m\033[1;32m->\033[1;m')
                                print "\033[1;34m+++++++Resultado++++++++++++++++++++++++++++++\033[1;m"

                                CifradosHash.diccionariomd5.dicmd5Cryptool(dicmd5,hashmd5)

                                print "\033[1;34m+++++++Resultado++++++++++++++++++++++++++++++\033[1;m"



                            elif md5options == "4":
                                print "Seleccione un Hash"
                                hashmd5 = raw_input('\033[1;32mCryptool\033[1;m\033[1;33m(HashMd5Find)\033[1;m\033[1;32m->\033[1;m')
                                print "\033[1;34m+++++++Resultado++++++++++++++++++++++++++++++\033[1;m"

                                CifradosHash.findhashmd5.Findmd5Crytool(hashmd5)

                                print "\033[1;34m+++++++Resultado++++++++++++++++++++++++++++++\033[1;m"

                            #Comandos generales
                            elif md5options == "98":
                                menudehash()

                            elif md5options == "99":
                                    os.system('clear')
                                    sys.exit(1)

                        #Comandos generales
                        if MenuHashoptions == "98":
                            homeinicio()
                        elif MenuHashoptions == "99":
                            os.system('clear')
                            sys.exit(1)

                #Cerrar
                if menuOptions == "99":
                    os.system('clear')

                    sys.exit(1)
                menudehash()
                menucriptografiaclasica()
                sistemadenumerionmenu()

        homeinicio()
    #Si hay un error
    except KeyboardInterrupt:
        print "Good bye"

#Inicia Todo el programa :p
try:
    if sys.argv[1] == "run":
        main()
    elif sys.argv[1] == "contacto":
        print "#"*50
        print "\033[1;34mTwitter:\033[1;m","@Alan_programmer"
        print "\033[1;34mEmail:\033[1;m","alanprogrammer@outlook.com"
        print "#"*50
except IndexError:
    os.system('clear')
    print '''
    ###############################################################
                                          dP                     dP
                                          88                     88
    .d8888b. 88d888b. dP    dP 88d888b. d8888P .d8888b. .d8888b. 88
    88'  `"" 88'  `88 88    88 88'  `88   88   88'  `88 88'  `88 88
    88.  ... 88       88.  .88 88.  .88   88   88.  .88 88.  .88 88
    `88888P' dP       `8888P88 88Y888P'   dP   `88888P' `88888P' dP
                           .88 88
                       d8888P  dP
    ###############################################################
    \033[1;34mHecho por:\033[1;mAlanprogrammer \033[1;34mPara:\033[1;mHacking Publico
      \033[1;34mVersion:\033[1;mBeta 0.12
    usage:python cryptool.py [Options] (run,contacto)
'''
