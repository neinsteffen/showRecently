
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QEvent
from page import Open
from mainWindow import Ui_MainWindow
from PyQt5.Qt import Qt

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
            
    def keyPressEvent(self, event):
        if event.type() == QEvent.KeyPress:      
            if event.key() == Qt.Key_X and event.modifiers() == Qt.ControlModifier:
                print("ctrl+x")
                self.load = Open()
                self.load.show()
                self.showMinimized()
            else: 
                if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
                    print("ctrl+c")
                    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exit(app.exec_())
    
    
    
    
   
                      
 