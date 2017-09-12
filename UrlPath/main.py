import requests
import sys
import httplib


#Funciones
def banner():
    pass

def main(sitio,ruta_archivo):
    try:
        headers = {'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        conn = requests.get(sitio,headers=headers)
        with open(ruta_archivo,"r") as f:
            for i in f.readlines():
                aux = i.replace("\n","")

                conn = requests.get(sitio+aux,headers=headers)

                if conn.status_code == 200 and aux:
                    print "[+] {}".format(sitio+aux)
    except requests.exceptions.ConnectionError:
        print "Error Url {}".format(sitio)
        sys.exit(1)
    except requests.exceptions.MissingSchema:
        print "Url no Valida"




if __name__ == "__main__":
    try:
        if len(sys.argv) >= 3:
            main(sys.argv[1],sys.argv[2])
        else:
            raise IndexError


    except IndexError:
        print "Usage:python UrlPath.py http://facebook.com/ HOME/USER/LIST.TXT"
