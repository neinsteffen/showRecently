from pynput import keyboard
from PyQt5.QtWidgets import QMainWindow, QApplication,QGraphicsDropShadowEffect,QDesktopWidget
from page import Open
class Load(object):
    def __init__(self):
        super(Load, self).__init__()
      
    def execute(self):
        pass
        #self.loading = Open()
        #self.loading.show()
        


    
    
    

if __name__ == '__main__':
    
    
    COMBS = [
        {keyboard.Key.tab, keyboard.KeyCode(char='x')},
        {keyboard.Key.tab, keyboard.KeyCode(char='X')}
    ]
    current = set()
    def run(key):
        if any([key in multi for multi in COMBS]):
            #key olayları gerçekleştiğinde bunları hafızaya alıyoruz
            current.add(key)
        if any(all(k in current for k in multi) for multi in COMBS):
            import sys
            app = QApplication(sys.argv)
            load = Open()
            load.show()
            app.exit(app.exec_())
            
            
            
    def onRelease(key):
        if any([key in multi for multi in COMBS]):
            current.remove(key)
        if key == keyboard.Key.esc:
            return False     
    with keyboard.Listener(on_press=run, on_release=onRelease) as listener:
        
        listener.join()
    
        
    
     
    
    
    



    


    