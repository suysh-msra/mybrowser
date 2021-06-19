###base code for browser ,courtesy samcodes
'''import smtplib
import speech_recognition as sr
import pyttsx3

from email.message import EmailMessage

'''
###to do : store login and password
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class mainWindow(QMainWindow):

    def __init__(self):


        super(mainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)#!!!!!!!!!!!!!
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction("<-",self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        fwd_btn = QAction("->",self)
        fwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fwd_btn)

        refresh_btn = QAction("G",self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        home = QAction("H",self)
        home.triggered.connect(self.navigate_youtube)####misleading function,actually takes you to home page
        navbar.addAction(home)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)


        '''utube_btn = QAction("YOUTube",self)
        utube_btn.triggered.connect(self.navigate_youtube)
        navbar.addAction(utube_btn)

        refresh_btn = QAction("<-",self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)'''

        


    def navigate_youtube(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        url = "https://"+(self.url_bar.text())
        self.browser.setUrl(QUrl(url))

    def update_url(self, r):
        self.url_bar.setText(r.toString())

        
app = QApplication(sys.argv)
QApplication.setApplicationName("gharelu chchipkali")

window = mainWindow()
                              
app.exec_()                  


