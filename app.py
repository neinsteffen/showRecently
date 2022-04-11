

    
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5 import QtCore
from page import Open
from mainWindow import Ui_MainWindow
import cpProcess,time
import pyautogui as pya
from PyQt5.Qt import Qt
import subprocess
import logging
import threading, keyboard,pyperclip


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
         

        ###FUNCS
        self.ui.open_button.clicked.connect(self.open)
        self.ui.close_button.clicked.connect(self.close)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
    def close(self):
        self.listener = Listener()
        self.listener.finished.connect(self.listenerFinished)
        print("listener closed")
        #self.ui.lbl_info.setText('Closed')
        sys.exit(app.exec_())
    def open(self):
        self.ui.lbl_info.setText('Running')
        self.ui.open_button.setStyleSheet("background-color : green")
        self.ui.close_button.setStyleSheet("background-color : midlight")
        print("lister working")
        if self.ui.lbl_info.text() == "Running":
            self.listener = Listener()
            self.listener.start()
        self.listener.finished.connect(self.listenerFinished)
            
        
    def listenerFinished(self):
        print("Listener Done!")
    def showRecently(self):
        self.listener = Listener()
        val = self.listener.val
        print("val:", val)
        if val:
            print("showa girdi")
            self.load = Open()
            self.load.show()
            self.showMinimized()
            pass
class Listener(QThread):
    copyiedVal =  set()
    val = False
    def run(self):
        while True:
            if keyboard.is_pressed("ctrl+c"):
                text = pyperclip.paste()
                self.copyiedVal.add(text)
                self.write()
            time.sleep(0.1)

    def write(self):
        with open("./test.txt",'a',encoding = 'utf-8') as f:
            for txt in self.copyiedVal:
                f.write(txt+"\n")
        self.copyiedVal.clear()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exit(app.exec_())
    
   
                      
 