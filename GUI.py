import sys
import pymorphy2
from datetime import datetime
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFont, QPalette, QBrush, QPixmap, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout,  QLineEdit, QMessageBox
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize

from pyqt5_plugins.examplebuttonplugin import QtGui

from Advanced_DB_RU import DbAdvanced
from OOP_DB import TeleGOD
from BD_parser import Parser


class CustomWebEnginePage(QWebEnginePage):
    """ Custom WebEnginePage to customize how we handle link navigation """
    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            mainWin.telegram.setUrl(url)
            return False
        return super().acceptNavigationRequest(url, _type, isMainFrame)


class Example(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.morph = pymorphy2.MorphAnalyzer()
        self.TeleGOD = TeleGOD(DbAdvanced())

        self.setMinimumSize(QSize(1900, 1000))
        self.setWindowTitle("InfoMiner")
        self.setGeometry(0, 0, 1900, 1000)

        self.layout = QGridLayout()

        self.path_to_picture = 'fon.jpg'
        # self.palette = QPalette()
        # self.palette.setBrush(QPalette.Background, QBrush(QPixmap(self.path_to_picture)))
        # self.setPalette(self.palette)
        self.setWindowIcon(QtGui.QIcon(self.path_to_picture))
        self.setStyleSheet("background-color: rgb(142, 222, 145);")

        self.browser = QWebEngineView()
        self.browser.setPage(CustomWebEnginePage(self))
        self.browser.setGeometry(0, 0, 1300, 780)
        self.browser.setUrl(QUrl("https://www.ibm.com/topics/artificial-intelligence"))
        # self.browser.setStyleSheet('border: 4px solid rgb(7, 107, 36)')
        self.setCentralWidget(self.browser)

        self.layout.addWidget(self.browser)

        self.telegram = QWebEngineView()
        self.telegram.setGeometry(1310, 0, 610, 1000)
        self.telegram.setUrl(QUrl("https://www.ibm.com/topics/natural-language-processing"))
        self.setCentralWidget(self.telegram)

        self.layout.addWidget(self.telegram)

        self.setLayout(self.layout)

        stylesheet = ("""QPushButton#pushButton {
                                    color: rgb(7, 107, 36);
                                    border-style: outset; 
                                    border-radius: 10px;
                                    font: bold 16px; 
                                    padding: 6px;
                                    color: rgb(255, 255, 255);
                                    border-bottom-width: 4px;
                                    border-right-width: 4px;
                                    border-color: rgb(7, 107, 36) ;     
                                    background-color: green;
                                    }
                                    QPushButton#pushButton:pressed {
                                    border-top-width: 2px;
                                    border-left-width: 2px; 
                                    border-bottom-width: 0px;
                                    border-right-width: 0px;
                                    background-color: green;
                                    border-style: inset;
                                    }""")

        text_box_style = """QLineEdit {color: rgb(255, 255, 255);
                                    background-color: rgb(7, 181, 56);
                                    border-radius: 10px;
                                    border: 4px solid rgb(7, 107, 36);} """

        self.bt1 = QPushButton("Выполнить", self)
        self.bt1.move(450, 935)
        self.bt1.setFont(QFont('San Francisco', 16))
        self.bt1.setFixedSize(140, 50)
        self.bt1.setObjectName("pushButton")
        self.bt1.setStyleSheet(stylesheet)
        self.bt1.clicked.connect(self.Button1)

        self.bt2 = QPushButton("Выполнить", self)
        self.bt2.move(1150, 840)
        self.bt2.setFont(QFont('San Francisco', 16))
        self.bt2.setFixedSize(140, 50)
        self.bt2.setObjectName("pushButton")
        self.bt2.setStyleSheet(stylesheet)
        self.bt2.clicked.connect(self.Button2)

        self.bt3 = QPushButton('Выполнить', self)
        self.bt3.move(1150, 790)
        self.bt3.setFont(QFont('San Francisco', 16))
        self.bt3.setFixedSize(140, 50)
        self.bt3.setObjectName("pushButton")
        self.bt3.setStyleSheet(stylesheet)
        self.bt3.clicked.connect(self.Button3)

        self.bt4 = QPushButton('Выполнить', self)
        self.bt4.move(1150, 890)
        self.bt4.setFont(QFont('San Francisco', 16))
        self.bt4.setFixedSize(140, 50)
        self.bt4.setObjectName("pushButton")
        self.bt4.setStyleSheet(stylesheet)
        self.bt4.clicked.connect(self.Button4)

        self.label1 = QLabel('<b>Сбор данных</b>', self)
        self.label2 = QLabel('<b>Создание интеративной карты</b>', self)
        self.label3 = QLabel('<b>Создание отчета</b>', self)

        self.label4 = QLabel('<b>Начало    (2023-01-15)</b>', self)
        self.label5 = QLabel('<b>Конец     (2023-01-16)</b>', self)
        self.label6 = QLabel('<b>Уникальность информации (1-99)</b>', self)
        self.label7 = QLabel('<b>Создание карты по тегам</b>', self)

        self.label1.setGeometry(50, 940, 300, 50)
        self.label2.setGeometry(650, 840, 350, 50)
        self.label3.setGeometry(650, 790, 300, 50)
        self.label4.setGeometry(50, 790, 300, 50)
        self.label5.setGeometry(50, 840, 300, 50)
        self.label6.setGeometry(50, 890, 360, 50)
        self.label7.setGeometry(650, 890, 350, 50)

        self.label1.setFont(QFont('San Francisco', 12))
        self.label2.setFont(QFont('San Francisco', 12))
        self.label3.setFont(QFont('San Francisco', 12))
        self.label4.setFont(QFont('San Francisco', 12))
        self.label5.setFont(QFont('San Francisco', 12))
        self.label6.setFont(QFont('San Francisco', 12))
        self.label7.setFont(QFont('San Francisco', 12))

        self.label1.setStyleSheet("color: rgb(11, 77, 14);")
        self.label2.setStyleSheet("color: rgb(11, 77, 14);")
        self.label3.setStyleSheet("color: rgb(11, 77, 14);")
        self.label4.setStyleSheet("color: rgb(11, 77, 14);")
        self.label5.setStyleSheet("color: rgb(11, 77, 14);")
        self.label6.setStyleSheet("color: rgb(11, 77, 14);")
        self.label7.setStyleSheet("color: rgb(11, 77, 14);")


        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox4 = QLineEdit(self)

        self.textbox1.move(450, 790)
        self.textbox1.resize(140, 40)
        self.textbox1.setFont(QFont('San Francisco', 12))

        self.textbox2.move(450,840)
        self.textbox2.resize(140, 40)
        self.textbox2.setFont(QFont('San Francisco', 12))

        self.textbox3.move(450, 890)
        self.textbox3.resize(140, 40)
        self.textbox3.setFont(QFont('San Francisco', 12))

        self.intValidator = QIntValidator(self)
        self.intValidator.setRange(1, 99)
        self.textbox3.setValidator(self.intValidator)

        self.textbox4.move(950, 895)
        self.textbox4.resize(190, 40)
        self.textbox4.setFont(QFont('San Francisco', 12))

        self.textbox1.setStyleSheet(text_box_style)
        self.textbox1.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox2.setStyleSheet(text_box_style)
        self.textbox2.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox3.setStyleSheet(text_box_style)
        self.textbox3.setAlignment(QtCore.Qt.AlignCenter)

        self.textbox4.setStyleSheet(text_box_style)
        self.textbox4.setAlignment(QtCore.Qt.AlignCenter)

        self.showMaximized()

    def warning(self, mistake):
        self.warning_window = QMessageBox()
        self.warning_window.setWindowTitle("Предупреждение")
        self.warning_window.setText(mistake)
        self.warning_window.setIcon(QMessageBox.Warning)
        self.warning_window.exec_()

    def GetDate(self):
        try:
            begin = datetime.strptime(self.textbox1.text(), '%Y-%m-%d')
            end = datetime.strptime(self.textbox2.text(), '%Y-%m-%d')
            return begin.timestamp(), end.timestamp()
        except Exception:
            return None, None

    def GetUniq(self):
        try:
            uniq = self.textbox3.text()
            uniq = int(uniq)
            return uniq
        except Exception:
            return None

    def Button1(self):
        parser = Parser()
        parser.parse()

    def Button2(self):
        begin, end = self.GetDate()
        uniq = self.GetUniq()
        if begin and end and uniq:
            self.TeleGOD.build_map(True, begin, end, uniq)
            self.browser.setHtml(self.TeleGOD.html)
        else:
            self.warning('Ошибка ввода данных')

    def Button3(self):
        begin, end = self.GetDate()
        uniq = self.GetUniq()
        if begin and end and uniq:
            self.TeleGOD.build_report(True, begin, end, uniq)
        else:
            self.warning('Ошибка ввода данных')

    def Button4(self):
        begin, end = self.GetDate()
        tag_word = self.textbox4.text()
        tag_word = self.morph.parse(tag_word)[0].normal_form

        if begin and end and tag_word:
            self.TeleGOD.tag_map_creation(tag_word, begin, end)
            self.browser.setHtml(self.TeleGOD.tag_html)
        else:
            self.warning('Ошибка ввода данных')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = Example()
    mainWin.show()
    sys.exit(app.exec_())
