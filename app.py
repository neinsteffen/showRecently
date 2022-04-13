

from PyQt5.QtWidgets import QMainWindow, QMessageBox,QApplication
#from PyQt5 import QtWidgets
from PyQt5 import QtCore,QtGui
from page import Open
from mainWindow import Ui_MainWindow
from PyQt5.Qt import Qt
import keyboard,pyperclip,time

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        ###FUNCS
        self.ui.open_button.clicked.connect(self.open)
        self.ui.close_button.clicked.connect(lambda: self.shutdown_p())
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.btn_close.clicked.connect(self.close_a)
        self.ui.btn_minimize.clicked.connect(lambda: self.minimized_p())
        
        def moveWindow(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos()- self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        self.ui.label.mouseMoveEvent = moveWindow
    
    def minimized_p(self):
        self.showMinimized()
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    def selected_item(self, isItem):
        pyperclip.copy(isItem.text())

        self.loader.close()    
    def shutdown_p(self):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
                self.close()
                print('Window closed')
        else:
            pass
    def close_a(self):
        self.close()

    def open(self):
        #Giving information to user
            self.ui.lbl_info.setText('Running')
            self.ui.open_button.setStyleSheet("background-color : green")
            self.ui.close_button.setStyleSheet("background-color : midlight")
            print("listener working")
            #if program is run, the process will execute
            #start another thread
            self.listener = Listener()
            
            self.listener.start()
            self.listener.finished.connect(self.listenerFinished)
            self.listener.val_bool.connect(self.showPage)
            self.listener.arr.connect(self.showPage)
   
    def showPage(self, val):
        print("show page val type:", type(val))
        if type(val) == set:
            #collect copyied texts to show list in new window
            count = 0
            for txt in val:
                self.loader.ui.showList.addItem(txt)
                count += 1
            self.loader.ui.showList.itemClicked.connect(self.selected_item)                  
            
        if type(val) == bool and val == True:
            self.loader = Open()    
            self.loader.show()
            self.loader.activateWindow()
            
        
    def listenerFinished(self):
        self.listener = Listener()
        print("Listener Done!")
        self.listener.kill()


class Listener(QtCore.QThread): #Thread
    copyiedVal =  set()
    val_bool = QtCore.pyqtSignal(bool)
    arr = QtCore.pyqtSignal(set)
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
    from sys import exit,argv
    app = QApplication(argv)
    main = Main()
    main.show()
    exit(app.exec())
    
   
                      
 