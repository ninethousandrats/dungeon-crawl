import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
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
        self.height = 600
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

        qp.setPen(QPen(Qt.green, 2, Qt.SolidLine))
       # qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        size = self.size()


        #room0
        qp.drawRect(0, 0, self.width(), self.height())
        qp.drawRect(self.width()*0.2, self.height()*0.2, self.width()*0.6, self.height()*0.6)
        
        #draw diag lines
        qp.drawLine(0, 0, self.width()*0.2, self.height()*0.2)                         # \  /
        qp.drawLine(self.width(), 0, self.width()*0.8, self.height()*0.2)
  
        qp.drawLine(self.width()*0.2, self.height()*0.8, 0, self.height())             # /  \
        qp.drawLine(self.width()*0.8, self.height()*0.8, self.width(), self.height())
        
        
        #room1
        qp.drawRect(self.width()*0.3, self.height()*0.3, self.width()*0.4, self.height()*0.4)
        
        #draw diag lines
        qp.drawLine(self.width()*0.2, self.height()*0.2, self.width()*0.3, self.height()*0.3)
        qp.drawLine(self.width()*0.8, self.height()*0.2, self.width()*0.7, self.height()*0.3)
  
        qp.drawLine(self.width()*0.2, self.height()*0.8, self.width()*0.3, self.height()*0.7)
        qp.drawLine(self.width(), self.height(),self.width()*0.7, self.height()*0.7)
        
        #room2
        qp.drawRect(self.width()*0.35, self.height()*0.35, self.width()*0.3, self.height()*0.3)
        
        #draw diag lines
        qp.drawLine(self.width()*0.3, self.height()*0.3, self.width()*0.35, self.height()*0.35)
        qp.drawLine(self.width()*0.7, self.height()*0.3, self.width()*0.65, self.height()*0.35)
  
        qp.drawLine(self.width()*0.3, self.height()*0.7, self.width()*0.35, self.height()*0.65)
        qp.drawLine(self.width()*0.7, self.height()*0.7, self.width()*0.65, self.height()*0.65)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
