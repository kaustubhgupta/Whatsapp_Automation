import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp_Automation")
        self.setGeometry(300,300,400,500)
        self.UI()

    def UI(self):
        self.text = QLabel("Enter your name:",self)
        self.text.move(20,50)
        self.msg_val = QLabel("Enter your message:",self)
        self.msg_val.move(20,75)
        self.msg_cout = QLabel("Enter count of your message:", self)
        self.msg_cout.move(20, 100)
        self.blank = QLabel("", self)
        self.blank.move(20, 125)
        self.send = QPushButton("Send",self)
        self.send.move(20,150)
        self.send.clicked.connect(self.send)
        self.show()

    def send(self):

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())

if __name__=='__main__':
    main()

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("D:\Whatsapp_Automation_from_github\chromedriver.exe")
driver.get("https://web.whatsapp.com/")




def message():
    name = input("Enter name of user :")
    messagev = input("Enter the message :")
    count = int(input("Enter count of messages: "))
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msgbox = driver.find_element_by_class_name("_3u328")
    for i in range(count):
        msgbox.send_keys(messagev)
        button = driver.find_element_by_class_name("_3M-N-")
        button.click()
        sleep(0.3)







