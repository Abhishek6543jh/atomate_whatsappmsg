import pywhatkit
import datetime
def whatsappmsg():
    number = input("the number of recepient")
    msg = input("enter the message here")
    hor= int(datetime.datetime.now().strftime("%H"))
    min= int(datetime.datetime.now().strftime("%M"))
    mmin = min + 2
    pywhatkit.sendwhatmsg(f'+91{number}' , msg ,hor,mmin)


whatsappmsg()