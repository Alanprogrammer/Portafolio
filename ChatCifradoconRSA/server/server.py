
import socket
from threading import Thread
import cPickle as pickle

import rsa
class Servidor:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 5555
        self.clientes_socket = []
        self.escuchar_cliente()

    def escuchar_cliente(self):
        try:
            socket_server = socket.socket()
            socket_server.bind((self.host,self.port))
            socket_server.listen(5)
            while True:
                (sck,addr)= socket_server.accept()
                if not sck in self.clientes_socket:
                    self.clientes_socket.append(sck)
                    Thread(target=self.Conexion_cliente,args=(sck,addr)).start()
        except KeyboardInterrupt:
            print "Good bye"
            socket_server.close()
            return


    def Conexion_cliente(self,sck,addr):
        try:
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
            cifrado = rsa.encrypt("Conectado al servidor",cla_pub)
            direccion = "%s:%i" % addr
            print "Conectado a :"+direccion
            sck.send(pickle.dumps(("Servidor",cifrado )))
            while True:
                buffer_ = sck.recv(10024).strip()
                print buffer_

                if not len(buffer_):
                    print direccion + "\tDesconectado"
                    self.clientes_socket.remove(sck)
                    sck.close()
                    return
                else:
                    for i in self.clientes_socket:
                        if i != sck:
                            print i.send(buffer_)

        except:
            print "Hubo Un error Por Favor de reiniciar el server"
            sck.close()
            return




Servidor()
