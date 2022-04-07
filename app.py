from cv2 import QT_RADIOBOX
from pynput import keyboard
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsDropShadowEffect,QDesktopWidget
from PyQt5.QtCore import Qt
from groupBox import Ui_Form
from PyQt5 import QtGui,QtWidgets
from pynput.mouse import Button, Controller
from pynput import keyboard
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


        


if __name__ == '__main__':

    #Bu kısımda ileride şarta koyacağımız tuş kombinasyonunu belirtiyoruz
    current = set()
    COMBS = [
        {keyboard.Key.tab, keyboard.KeyCode(char='x')},
        {keyboard.Key.tab, keyboard.KeyCode(char='X')}
    ]

    def run(c):
        #programı ayağa kaldıran kısım
        print(" e: ", c)
        import sys
        app = QApplication(sys.argv)
        load = Open()
        load.show()
        app.exit(app.exec_())
    
   
    def onPress(key):
        #eğer key bizim kombinimizde belirtilenlerin içinde varsa
        if any([key in multi for multi in COMBS]):
             #key olayları gerçeleştiğinde bunları hafızaya alıyoruz
            current.add(key)
        if any(all(k in current for k in multi) for multi in COMBS):
            #eğer 2 key durumu da gerçekleşirse programı ayağa kaldıracak fonksiyonu çağrıyoruz
            run(current)
            print(current)

    def onRelease(key):
        #her seferinde aynı key olayı gelmesindiye eklenen keyleri siliyoruz
        if any([key in multi for multi in COMBS]):
            current.remove(key)
        if key == keyboard.Key.esc:
            return False 
    with keyboard.Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join() #joinleme

    


    