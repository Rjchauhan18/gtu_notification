import os
from bs4 import BeautifulSoup 
import requests
import time 
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
from dotenv import load_dotenv

load_dotenv(".env")

# NUMBER = os.environ["number"]

keyboard = Controller()




def send_whatsapp_message(number:int,msg: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no=f"+91{number}", 
            message=msg,
            tab_close=True
        )
        time.sleep(5)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        print("Message sent!\n\n" + msg)
    except Exception as e:
        print(str(e))

# <a href="#" id="ContentPlaceHolder1_lvCircular_lblContentHeading_0"></a>


r = requests.get("https://www.gtu.ac.in/Circular.aspx")

try:
    html = BeautifulSoup(r.text,'html.parser')
except Exception as e:
    print(e)

h3_tag=html.find("h3",{"class":"d-block"})
# print(element_by_class.prettify())

# try:
#     file = open("circular.html", "w",encoding="utf-8")
#     file.write(element_by_class.prettify())
# except Exception as e:
#     print(e)


# top_circular = h3_tag.find("a" , {"class":"most-popular-post"})
# print(top_circular.pret
# tify())

# title and link of the content

with open("save.txt", "r") as f:
    last_notification = f.readlines()
    # print(last_n/otification[0])



# with open("save.txt", "w") as f:
#             f.writelines("link"+" rahul chauhan")


def info():

    #date
    dt = (html.find("p",{"id":"ContentPlaceHolder1_lvCircular_lblUploadDate_0"})).text
    link_tag=h3_tag.find("a",{"target" :"_blank"},href=True)
    link= link_tag.get('href')

    # print(dt)
    # print(link_tag.text)

    if last_notification[0] != link:
        try:
            msg = (dt + "\n"+link_tag.text+ "\n"+link + "\n")
        except Exception as e:
            print(e)

        # print(os.getenv('number'))
        
        send_whatsapp_message(os.getenv('number'),msg)
        with open("save.txt", "w") as f:
            f.writelines(link)
            # last_link.append(link)



if __name__ == "__main__":
# while True:
    info()

