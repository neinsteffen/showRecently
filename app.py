
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5 import QtCore
from page import Open
from mainWindow import Ui_MainWindow
from PyQt5.Qt import Qt
import keyboard,pyperclip,time


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
        print("listener closed")
        sys.exit(app.exec_())
    def open(self):
        #Giving information to user
        self.ui.lbl_info.setText('Running')
        self.ui.open_button.setStyleSheet("background-color : green")
        self.ui.close_button.setStyleSheet("background-color : midlight")

        print("listener working")
        #if program is run, the process will execute
        if self.ui.lbl_info.text() == "Running":
            #start another thread
            self.listener = Listener()
            self.listener.start()
            self.listener.finished.connect(self.listenerFinished)
            self.listener.val_bool.connect(self.showPage)
            self.listener.val_str.connect(self.showPage)
   
    def showPage(self, val):
        self.list = set()
        print("show page val type:", type(val))
        if type(val) == str:
            #collect copyied texts to show list in new window
            self.list.add(val)
            self.loader = Open()
            self.loader.ui.groupBox.setTitle(val)
        if type(val) == bool and val == True:
            self.loader = Open()          
            self.loader.show()
        
    def listenerFinished(self):
        print("Listener Done!")
        self.listener.exit()


class Listener(QThread): #Thread
    copyiedVal =  set()
    val_bool = pyqtSignal(bool)
    val_str = pyqtSignal(str)
    text = ""
    def run(self):
        while True:
            #check if ctrl+v is pressed
            if keyboard.is_pressed("ctrl+c"):
                self.text = pyperclip.paste()
                self.copyiedVal.add(self.text)
                #self.write()
                print(self.text) 
                
            if keyboard.is_pressed("ctrl+v"):
                self.val_bool.emit(True)
                self.val_str.emit(self.text)
                

            time.sleep(0.1)
        

    def write(self):
        #This side will not run, just for checking
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
    
   
                      
 