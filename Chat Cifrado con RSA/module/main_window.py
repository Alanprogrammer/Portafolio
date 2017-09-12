#-*- coding:utf-8 -*-
#Modulos
from PyQt4.QtGui import (QLabel,
QTextEdit,
QWidget,
QVBoxLayout,
QHBoxLayout,
QPushButton,
QTextBrowser,
QDialog,
QLineEdit,
QIcon,
QMessageBox
)
from PyQt4.QtCore import SIGNAL,QThread
import socket,sys
import cPickle as pickle
import time
import rsa
class Chat(QWidget):
    def __init__(self):
        super(Chat,self).__init__()
        self.setWindowTitle("Chat Alanprogrammer")
        self.setMinimumSize(100,300)

        self.setWindowIcon(QIcon("imagenes/icon.jpg"))

        #Valores globales Boleanos
        self.StartSocket = True

        #Widget#
        '''Chat'''
        self.Mostrarmessage = QTextEdit()
        self.Mostrarmessage.setReadOnly(True)
        self.Mostrarmessage.setEnabled(False)
        self.bt_mensaje_enviar = QPushButton("Enviar mesanje")
        self.bt_mensaje_enviar.setEnabled(False)
        self.text_message= QTextEdit()
        self.text_message.setEnabled(False)
        '''Login'''
        self.user = QLineEdit()
        self.userText = QLabel("User:")
        self.password =QLineEdit()
        self.passwordText = QLabel("Password:")
        self.host =  QLineEdit()
        self.hostText =QLabel("Host:")
        self.port =QLineEdit()
        self.portText = QLabel("Port:")
        self.enviar_login = QPushButton("Conectar")

        #Layout
        vbox_nivel_uno = QHBoxLayout(self)
        hbox_nivel_uno = QVBoxLayout()
        #----------Horizontal----------------#
        hbox_nivel_uno.addWidget(self.userText)
        hbox_nivel_uno.addWidget(self.user)
        hbox_nivel_uno.addWidget(self.passwordText)
        hbox_nivel_uno.addWidget(self.password)
        hbox_nivel_uno.addWidget(self.hostText)
        hbox_nivel_uno.addWidget(self.host)
        hbox_nivel_uno.addWidget(self.portText)
        hbox_nivel_uno.addWidget(self.port)
        hbox_nivel_uno.addWidget(self.enviar_login)
        vbox_nivel_uno.addLayout(hbox_nivel_uno)
        #-------------------------------------#
        vbox_nivel_uno.addWidget(self.Mostrarmessage)
        hbox_nivel_uno.addWidget(self.bt_mensaje_enviar)
        hbox_nivel_uno.addWidget(self.text_message)
        #conexiones
        #self.bt_mensaje_enviar
        self.enviar_login.clicked.connect(self._login_)
        #enviar_login
        self.bt_mensaje_enviar.clicked.connect(self._enviar_)
    def _enviar_(self):

        load_pub= {
        "e":65537,
        "n":75092918374993288490854852486725400851918220355483413898302263898496363820439
        }
        load_priv ={
        "d":7992021387393048006831447824815137563760967270209602902505756204915768553473,
        "p":61063583869282968813158442010912342579201,
        "q":1229749608796996037048496678684511639
        }
        cla_pub = rsa.PublicKey(n=load_pub['n'],e=load_pub['e'])
        cla_priv = rsa.PrivateKey(n=load_pub['n'],e=load_pub['e'],d=load_priv['d'],p=load_priv['p'],q=load_priv['q'])

        data = str(self.text_message.toPlainText().toAscii())
        clave = str(self.password.text().toAscii())
        cifrado_xor = ""
        for index,val in enumerate(data):
            ci = ord(val) ^ ord(clave[0])
            cifrado_xor+=str(chr(ci))

        cifrado_rsa = rsa.encrypt(cifrado_xor,cla_pub)


        paquete = (self.user.text(),cifrado_rsa)
        paquete = pickle.dumps(paquete)
        if data:
            self.sock_client.send(paquete)
            self.text_message.clear()
            self.mensaje((self.user.text(),cifrado_rsa))


    def _login_(self):
        intentos= 0
        if self.StartSocket:
            '''Conexion '''
            try:
                if self.user.text() and self.password.text() and self.host.text()  and self.port.text():
                    self.sock_client = socket.socket()
                    host,port = str(self.host.text().toAscii()),int(self.port.text().toAscii())
                    self.sock_client.connect((host,port))
                    '''aqui'''
                    self.qthread = Escuchar(self.sock_client)
                    self.connect(self.qthread, SIGNAL("MENSAJE"), self.mensaje)
                    self.qthread.start()
                    #########################################
                    self.user.setEnabled(False)
                    self.password.setEnabled(False)
                    self.host.setEnabled(False)
                    self.port.setEnabled(False)
                    self.enviar_login.setText("Salir")
                    self.bt_mensaje_enviar.setEnabled(True)
                    self.Mostrarmessage.setEnabled(True)
                    self.text_message.setEnabled(True)
                    self.StartSocket = False
                else:
                    error = "User:"+self.user.text()+"\n"+"Password:"+self.password.text()+"\n"+"Host:"+self.host.text()+"\n"+"Port:"+self.port.text()+"\n"
                    QMessageBox.critical(None,"Campos Vacios",error)
            except:
                error =  self.host.text() +":"+ self.port.text()


                QMessageBox.critical(None,"Error de Conexion",error)

        else:
            #Close
            sys.exit(1)

    def mensaje(self,data):
        load_pub= {
        "e":65537,
        "n":75092918374993288490854852486725400851918220355483413898302263898496363820439
        }
        load_priv ={
        "d":7992021387393048006831447824815137563760967270209602902505756204915768553473,
        "p":61063583869282968813158442010912342579201,
        "q":1229749608796996037048496678684511639
        }
        cla_pub = rsa.PublicKey(n=load_pub['n'],e=load_pub['e'])
        cla_priv = rsa.PrivateKey(n=load_pub['n'],e=load_pub['e'],d=load_priv['d'],p=load_priv['p'],q=load_priv['q'])


        nick,mensaje = data
        descifrado_rsa = rsa.decrypt(mensaje,cla_priv)
        clave = str(self.password.text().toAscii())
        descifrado_uno = ""
        for index,val in enumerate(descifrado_rsa):
            de  = ord(val) ^ ord(clave[0])
            descifrado_uno+=str(chr(de))
        mensaje =  '<font color="#00BFFF">%s: </font>%s' % (nick,descifrado_uno)
        self.Mostrarmessage.append(mensaje)
#Dialogo de Reglas
class Acerca_De(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle("Acerca de.")
        q = QLabel('''
        Reglas:utf
        ''')
class Escuchar(QThread):
    def __init__(self,sck):
        QThread.__init__(self)
        self.socket = sck


    def run(self):
        try:
            while True:
                buffer_ = self.socket.recv(10024).strip()
                mensaje = pickle.loads(buffer_)
                time.sleep(0.5)
                self.emit(SIGNAL("MENSAJE"),mensaje)
        except:
            sys.exit(1)

    def __del__(self):
        self.wait()
