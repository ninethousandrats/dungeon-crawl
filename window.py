import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Dungeon Crawl'
        self.left = 20
        self.top = 50
        self.width = 1000
        self.height = 1000
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = PaintWidget(self)
        self.m.move(0,0)
        self.m.resize(self.width,self.height)

        self.show()

class PaintWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)

        qp.setPen(Qt.green)
        size = self.size()
        
        
        # Let's build our grid ʕ； •`ᴥ•´ʔ
      
        # Square that is close
        UL0x = 0
        UL0y = 0
        
        UR0x = self.width()
        UR0y = 0
        
        LL0x = 0
        LL0y = self.height()
        
        LR0x = self.width()
        LR0y = self.height()
        
        
        # Square that is... less close.
        
        UL1x = self.width() * 0.33
        UL1y = self.height() * 0.33
        
        UR1x = self.width() * 0.66
        UR1y = self.height() * 0.33
        
        LL1x = self.width() * 0.33
        LL1y = self.height() * 0.66
        
        LR1x = self.width() * 0.66
        LR1y = self.height() * 0.66
        
        qp.drawLine(UL0x, UL0y, UL1x, UL1y)  # \
        qp.drawLine(UR1x, UR1y, UR0x, UR0y)  # /
        
        qp.drawLine(UL1x, UL1y, UR1x, UR1y)  # _
        
        qp.drawLine(UL1x, UL1y, LL1x, LL1y)  # | <-
        qp.drawLine(UR1x, UR1y, LR1x, LR1y)  # -> |
        
        qp.drawLine(LL1x, LL1y, LR1x, LR1y)  # _
        
        qp.drawLine(LL1x, LL1y, LL0x, LL0y)  # /
        qp.drawLine(LR1x, LR1y, LR0x, LR0y)  # \
        
        # Move the bear sandwhich ʕ•ᴥ• ʔ☝

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())