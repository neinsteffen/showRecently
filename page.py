
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsDropShadowEffect,QDesktopWidget
from PyQt5.QtCore import Qt
from groupBox import Ui_Form
from pynput.mouse import Controller
from PyQt5 import QtCore,QtGui
class Open(QMainWindow):
    
    def __init__(self):
        super(Open, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        self.setPageLocation()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.btn_close.clicked.connect(lambda: self.shutdown_p())
        self.ui.btn_minimize.clicked.connect(lambda: self.minimized_p())
        self.setWindowIcon(QtGui.QIcon('logo.png'))
                    
        
    
    def shutdown_p(self):
        self.close()
    def minimized_p(self):
        self.showMinimized()
    def setPageLocation(self):
        mouse = Controller()
        current_mouse_position = mouse.position
        av = QDesktopWidget().availableGeometry()
        sc = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = av.width() - widget.width()
        y = 2 * sc.height() - sc.height() - widget.height()
        self.move(current_mouse_position[0],current_mouse_position[1])

    




