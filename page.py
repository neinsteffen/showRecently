from cv2 import QT_RADIOBOX
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsDropShadowEffect,QDesktopWidget
from PyQt5.QtCore import Qt
from groupBox import Ui_Form
from PyQt5 import QtGui,QtWidgets
from pynput.mouse import Button, Controller

class Open(QMainWindow):
    
    def __init__(self):
        super(Open, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.show()
        self.setPageLocation()

    def setPageLocation(self):
        mouse = Controller()
        current_mouse_position = mouse.position
        av = QDesktopWidget().availableGeometry()
        sc = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = av.width() - widget.width()
        y = 2 * sc.height() - sc.height() - widget.height()
        self.move(current_mouse_position[0],current_mouse_position[1])




