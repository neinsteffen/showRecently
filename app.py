
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QEvent
from PyQt5 import QtCore
from page import Open
from mainWindow import Ui_MainWindow
import cpProcess,time
import pyautogui as pya
from PyQt5.Qt import Qt



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.copyiedVal =  set()

        ###FUNCS
        self.ui.open_button.clicked.connect(self.switch)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.cond = False
        
            
    def keyPressEvent(self, event):
        self.cond;
        if self.ui.open_button.text() == 'Close':
            self.cond = True
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_V and event.modifiers() == Qt.ControlModifier and self.cond:
                    self.setCopyied() 
                    self.load = Open()
                    self.load.show()
                    self.showMinimized()
                                
                else:
                    if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
                        self.getCopyied()
                    
    def switch(self):
        if self.ui.open_button.text() == 'Open':
            self.ui.open_button.setText('Close')
            self.ui.lbl_info.setText('Running')
            return True
        else:
            self.ui.open_button.setText('Open')
            self.ui.lbl_info.setText('Closed')
            self.cond = False
            
    def getCopyied(self):
        self.copyiedVal.add(cpProcess.paste_windows())
        print(self.copyiedVal)

    def setCopyied(self):
        with open("./test.txt",'a',encoding = 'utf-8') as f:
            for txt in self.copyiedVal:
                f.write(txt+"\n")
            

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exit(app.exec_())
    
    
    
    
   
                      
 