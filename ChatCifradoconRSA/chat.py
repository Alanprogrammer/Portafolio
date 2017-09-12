#-*- coding:utf-8 -*-
#Modulos
from PyQt4.QtGui import (QApplication
)
from module.main_window import Chat
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    with open("tema.qss","r") as f:
        tema = f.read()
    app.setStyleSheet(tema)

    w = Chat()
    w.show()
    sys.exit(app.exec_())
