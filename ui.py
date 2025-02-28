import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QDate
class View(QWidget):
    
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self)
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Message', self)
        self.btn2 = QPushButton('Clear', self)
        
        hbox = QVBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)    
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl1)

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('이상우사진.jpg'))
        self.resize(256, 256)
        self.show()

    def activateMessage(self):
        self.te1.appendPlainText('Button clicked!')

    def clearMessage(self):
        self.te1.clear()