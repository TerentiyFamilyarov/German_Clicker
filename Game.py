import sys
from math import ceil, sqrt

from PyQt6.QtCore import Qt, QTimer, QThread, QRect
from PyQt6.QtGui import QColor, QFont, QImage, QPainter, QPixmap
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QLabel


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,700)
        self.setStyleSheet('background-color:rgb(100,150,100);border:none')

        self.rangs = {
            'Beginner': 'silver',
            'Starter' : 'paleturquoise',
            'Dude' : 'olivedrab',
            'Man' : 'navy',
            'Gigachad' : 'lightsteelblue',
            'German' : 'lightgreen',
            'MGerman' : 'lawngreen',
            'GGerman' : 'deeppink',
            'EarthEaterGerman': 'darkorange',
            'StarGerman' : 'goldenrod',
            'GalaxyGerman' : 'midnightblue',
            'UniverseGerman' : 'darkslateblue',
            'InfinityGerman' : 'plum',
            'CelestialGerman' : 'coral',
            'EndsGerman' : 'sandybrown',
            'RealBreakerGerman': 'salmon',
            '???German' : 'seashell',
        }
        self.list_rangs_keys = list(self.rangs.keys())
        print(self.list_rangs_keys)

        self.backgr = QLabel(self)
        self.backgr.setGeometry(0,0,self.width(),self.height())
        self.backgr.setStyleSheet(f'background-color:rgba(0,0,0,10);border:none')
        self.backgr.show()

        self.exa_text = QLabel('Press G for ReGermanth',self)
        self.exa_text.setGeometry(0,int(self.height()*1)-50,self.width(),25)
        self.exa_text.setFont(QFont('Luminari, fantasy',15))
        self.exa_text.setStyleSheet('background-color:rgba(255,0,0,0);border:none;color:black')
        self.exa_text.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        self.exa_text.show()

        self.exa_text2 = QLabel('Press I for increase GermanPower',self)
        self.exa_text2.setGeometry(0,int(self.height()*1)-25,self.width(),25)
        self.exa_text2.setFont(QFont('Luminari, fantasy',15))
        self.exa_text2.setStyleSheet('background-color:rgba(255,0,0,0);border:none;color:black')
        self.exa_text2.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        self.exa_text2.show()

        self.backgr2 = QLabel(self)
        self.backgr2.setGeometry(0,0,self.width(),self.height())
        self.backgr2.setStyleSheet(f'background-color:rgba(0,0,0,90);border:none')
        self.backgr2.show()

        self.text = QLabel('IQ \n Rank: None',self)
        self.text.setFont(QFont('Luminari, fantasy',40))
        self.text.setStyleSheet('background-color:rgba(0,0,0,255);border:none;color:white')
        self.text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text.setGeometry(0,0,self.width(),int(self.height()))
        self.text.show()

        self.button = QPushButton(self)
        self.button.setGeometry(0,0,self.width(),self.height())
        self.button.setStyleSheet('QPushButton{background-color:rgba(10,10,10,50);border:none}'
                                  'QPushButton:pressed{background-color:rgba(0,0,0,50)}')
        self.button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.IQ = -1
        self.rank = self.list_rangs_keys[int(self.IQ)-1]
        self.timer = QTimer()
        self.auto_click_koef = 0
        self.tap_power = 0
        self.limit = -1
        self.end = False
        self.IQkoef = 0
        def auto_click():
            self.IQ += 1*self.auto_click_koef
            self.IQkoef = int(0.05 * sqrt(self.IQ))
            self.exa_text.setText(f'Press G for ReGermanth                      AutoClick: {self.auto_click_koef}')
            self.exa_text2.setText(f'Press I for increase GermanPower        FapPower: {self.tap_power+1}')
            if self.IQkoef <= len(self.list_rangs_keys)-1:
                self.rank = self.list_rangs_keys[self.IQkoef]
            elif self.rank == self.list_rangs_keys[-1]:
                    self.limit = self.IQ
            else:
                self.rank = self.list_rangs_keys[-1]
            self.text.setText(f'{round(self.IQ, 6)} IQ\nRank: {self.rank}')
            self.setStyleSheet(f'background-color:{self.rangs[self.rank]};border:none')
            self.text.setStyleSheet(f'background-color:rgba(0,0,0,0);border:none;color:{self.rangs[self.rank]}')
            self.exa_text.setStyleSheet(f'background-color:rgba(255,0,0,0);border:none;color:{self.rangs[self.rank]}')
            self.exa_text2.setStyleSheet(f'background-color:rgba(255,0,0,0);border:none;color:{self.rangs[self.rank]}')
            if self.IQ >= 4*self.limit > 0:
                self.text.setText(f'{round(self.IQ, 6)} IQ\nRank: {self.rank}\nThis is the and game\nCongratulations!\nPress F to pay respect...')
                self.end = True
                self.setStyleSheet(f'background-color:white;border:none')
                self.text.setStyleSheet(f'background-color:rgba(0,0,0,0);border:none;color:black')
                self.exa_text.setStyleSheet(
                    f'background-color:rgba(255,0,0,0);border:none;color:black')
                self.exa_text2.setStyleSheet(
                    f'background-color:rgba(255,0,0,0);border:none;color:black')
            else: self.end = False
        self.timer.start(1000)
        def change_button():
            if self.IQ == -1:
                self.timer.timeout.connect(auto_click)
                self.IQ = 0
            self.IQ += 1 + self.tap_power
            self.IQkoef = 0
            self.IQkoef = int(0.05*sqrt(self.IQ))
            if self.IQkoef <= len(self.list_rangs_keys)-1:
                self.rank = self.list_rangs_keys[self.IQkoef]
            elif self.rank == self.list_rangs_keys[-1]:
                    self.limit = self.IQ
            else: self.rank = self.list_rangs_keys[-1]
            self.text.setText(f'{round(self.IQ,6)} IQ\nRank: {self.rank}')
            self.setStyleSheet(f'background-color:{self.rangs[self.rank]};border:none')
            self.text.setStyleSheet(f'background-color:rgba(0,0,0,0);border:none;color:{self.rangs[self.rank]}')
            self.exa_text.setStyleSheet(f'background-color:rgba(255,0,0,0);border:none;color:{self.rangs[self.rank]}')
            self.exa_text2.setStyleSheet(f'background-color:rgba(255,0,0,0);border:none;color:{self.rangs[self.rank]}')
            if self.IQ >= 4*self.limit > 0:
                self.text.setText(
                    f'{round(self.IQ, 6)} IQ\nRank: {self.rank}\nThis is the and game\nCongratulations!\nPress F to pay respect...')
                self.end = True
                self.setStyleSheet(f'background-color:white;border:none')
                self.text.setStyleSheet(f'background-color:rgba(0,0,0,0);border:none;color:black')
                self.exa_text.setStyleSheet(
                    f'background-color:rgba(255,0,0,0);border:none;color:black')
                self.exa_text2.setStyleSheet(
                    f'background-color:rgba(255,0,0,0);border:none;color:black')
            else:
                self.end = False
        self.button.clicked.connect(change_button)



    def keyPressEvent(self, a0):
        if a0.key() == Qt.Key.Key_G:
            # self.auto_click_koef += int(self.IQ)/1000
            self.auto_click_koef += 0.055*sqrt(int(self.IQ))
            self.IQ = 0

        if a0.key() == Qt.Key.Key_I:
            # self.tap_power += int(self.IQ)/100
            self.tap_power += 0.045*sqrt(int(self.IQ))
            self.IQ = 0

        if self.end is True and a0.key() == Qt.Key.Key_F:
            self.button.setDisabled(True)
            self.text.setText('You are worthy to be called\nTruly German\n Your obsession is the\neight miracle of world!\n Have a nice day, dude')
            self.exa_text.setText('')
            self.exa_text2.setText('')
            self.timer.stop()



app = QApplication(sys.argv)

game = Game()
game.show()

sys.exit(app.exec())