
from ast import Set
from typing import List
from PyQt5.QtWidgets import *
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
        self.ui.close_button.clicked.connect(lambda: self.shutdown_p())
        

    
    def selected_item(self, isItem):
       
        pyperclip.copy(isItem.text())
        #print(isItem.text())
      
        

    def shutdown_p(self):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
                self.close()
                print('Window closed')
        else:
            pass


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
            self.listener.arr.connect(self.showPage)
   
    def showPage(self, val):
        
        #self.list = set()
        print("show page val type:", type(val))
        if type(val) == set:
            #collect copyied texts to show list in new window
            count = 0
            for txt in val:
                self.loader.ui.showList.addItem(txt)
                count += 1
            #val.remove(txt)
            self.loader.ui.showList.itemClicked.connect(self.selected_item)                  
            
        if type(val) == bool and val == True:
            self.loader = Open()          
            self.loader.show()
            self.loader.activateWindow()
            
        
        
    def listenerFinished(self):
        print("Listener Done!")
        self.listener.exit()


class Listener(QThread): #Thread
    copyiedVal =  set()
    val_bool = pyqtSignal(bool)
    arr = pyqtSignal(set)
    text = " "
    list_ = set()
    def run(self):
        while True:
            #check if ctrl+v is pressed
            if keyboard.is_pressed("ctrl+c"):
                self.text = pyperclip.paste()
                self.list_.add(self.text)
                print(self.list_) 
                
            if keyboard.is_pressed("ctrl+b"):
                self.val_bool.emit(True)
                self.arr.emit(self.list_)
                

            time.sleep(0.1)




    


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec())
    
   
                      
 