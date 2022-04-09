from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QFont
from final_win import *
txt_title = 'Здоровье'
win_x, win_y = 200, 100
win_width, win_height = 1000, 600
class Experiment():
    pass
class TestWin(QWidget):
    def next_click(self):
        self.hide()
        self.exp = Experiment(self.line_age.text(),self.line_test1.text(),self.line_test2.text(),self.line_test3.text())
        self.tw = FinalWin(self.exp)
    def __init__(self):
        super().__init__()
        self.set_appear()

        self.iniyUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def iniyUI(self):
        metka1 = QLabel('мшыры')
        metka2 = QLabel('ириш')
        metka3 = QLabel('иnsриш')
        metka4 = QLabel('ирbsgиш')
        metka5 = QLabel('ирaиш')
        self.metka6 = QLabel('иdbfш')
        self.bas1 = QPushButton('nsndh')
        self.bas2 = QPushButton('nvf')
        self.bas3 = QPushButton('bci')
        self.bas4 = QPushButton('vsv')
        lon1 = QLineEdit('bd')
        lon2 = QLineEdit('njsd')
        lon3 = QLineEdit('mpqk')
        lon4 = QLineEdit('mwcd')
        lon5 = QLineEdit('sd')
        self.vv = QVBoxLayout()
        self.cn = QHBoxLayout()
        self.lin = QVBoxLayout()
        self.lin.addWidget(metka1, alignment=Qt.AlignLeft)
        self.lin.addWidget(lon1, alignment=Qt.AlignLeft)
        self.lin.addWidget(metka2, alignment=Qt.AlignLeft)
        self.lin.addWidget(lon2, alignment=Qt.AlignLeft)
        self.lin.addWidget(metka3, alignment=Qt.AlignLeft)
        self.lin.addWidget(self.bas1, alignment=Qt.AlignLeft)
        self.lin.addWidget(metka4, alignment=Qt.AlignLeft)
        self.lin.addWidget(self.bas2, alignment=Qt.AlignLeft)
        self.lin.addWidget(metka5, alignment=Qt.AlignLeft)
        self.lin.addWidget(self.bas3, alignment=Qt.AlignLeft)
        self.lin.addWidget(lon3, alignment=Qt.AlignLeft)
        self.lin.addWidget(lon4, alignment=Qt.AlignLeft)
        self.lin.addWidget(self.bas4, alignment=Qt.AlignCenter)
        self.vv.addWidget(self.metka6, alignment=Qt.AlignRight)
        self.cn.addLayout(self.lin)
        self.cn.addLayout(self.vv)
        self.setLayout(self.cn)
    def connects(self):
        self.bas4.clicked.connect(self.next)
        self.bas1.clicked.connect(self.timer_test)
        self.bas2.clicked.connect(self.timer_sits)
        self.bas3.clicked.connect(self.timer_final)
    def next(self):
        self.hide()
        self.vdf = FinalWin()
    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)    
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.metka6.setText(time.toString("hh:mm:ss"))
        self.metka6.setFont(QFont("Times", 36, QFont.Bold))
        self.metka6.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.metka6.setText(time.toString("hh:mm:ss")[6:8])
        self.metka6.setFont(QFont("Times", 36, QFont.Bold))
        self.metka6.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.metka6.setText(time.toString("hh:mm:ss"))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.metka6.setStyleSheet("color:rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.metka6.setStyleSheet("color:rgb(0,255,0)")
        else:
            self.metka6.setStyleSheet("color:rgb(0,0,0)")
        self.metka6.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()        
up = QApplication([])
asd = TestWin()
up.exec_()