
from PyQt5.QtWidgets import QMainWindow, QApplication
from page import Open
from mainWindow import Ui_MainWindow
from PyQt5.Qt import Qt

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.COMBINATIONS = [
        {Qt.Key_Control, Qt.Key_X}
        ]
        self.current = set()
        
        
    
    def keyPressEvent(self, event):
        if any([event.key() in COMBO for COMBO in self.COMBINATIONS]):
                self.current.add(event.key())
        if any(all(k in self.current for k in COMBO) for COMBO in self.COMBINATIONS):
            self.prnt(event.key())
        if event.key() == Qt.Key_Escape:
            return False
                

    def prnt(self, key):
        self.load = Open()
        self.load.show()
        self.showMinimized()
        #self.hide()

        self.current.clear()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    app.exit(app.exec_())
    
    
    
    
   
                      
 