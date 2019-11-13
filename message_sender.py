from selenium import webdriver
from time import sleep
driver= webdriver.Chrome("D:\Whatsapp_Automation_from_github\chromedriver.exe")
print("Scan QR code")
driver.get("https://web.whatsapp.com/")


def message():
    name=input("Enter name of user :")
    message=input("Enter the message :")
    count=int(input("Enter count of messages: "))
    user= driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msgbox = driver.find_element_by_class_name("_3u328")

    for i in range(count):
        msgbox.send_keys(message)
        button=driver.find_element_by_class_name("_3M-N-")
        button.click()
        sleep(0.3)

def vidimg():
    name= input("Enter name of user :")
    path= input("Enter path of file :")
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    attach_box=driver.find_element_by_xpath('//div[@title = "Attach"]')
    attach_box.click()
    imgvid_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    imgvid_box.send_keys(path)

    sleep(3)

    send_button = driver.find_element_by_xpath('//span[@data-icon="send-light"]')
    send_button.click()

def logout():
    search_for_dot= driver.find_element_by_xpath('//span[@data-icon="menu"]')
    search_for_dot.click()
    sleep(1.8)
    out = driver.find_element_by_xpath('//div[@title = "Log out"]')
    out.click()

message()
logout()

#new features to be added

#1. Menu driven system
#2. automatic connection request to be handled