#!/usr/bin/python3
import vk
import random
import time
# auth
#token = 'tokenHere'
session = vk.Session(access_token=token)
api = vk.API(session)

def send_message():
    irand = random.randint(1, 10)
    if irand == 1:
        message = 'Сообщение 1'
    elif irand == 2:
        message = 'Сообщение 2'
    elif irand == 3:
        message = 'Сообщение 3'
    elif irand == 4:
        message = 'Сообщение 4'
    elif irand == 5:
        message = 'Сообщение 5'
    elif irand == 6:
        message = 'Сообщение 6'
    elif irand == 7:
        message = 'Сообщение 7'
    elif irand == 8:
        message = 'Сообщение 8'
    elif irand == 9:
        message = 'Сообщение 9'
    elif irand == 10:
        message = 'Сообщение 10'

    domain = 'id'  #id send here
    api.messages.send(domain=domain, message=message)

    print("Message sent", time.strftime("%H:%M:%S"))

def main():
    itimerand = random.randint(60, 1800)
    time.sleep(itimerand)
    send_message()
# Send message
main()
