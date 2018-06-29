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
        message = 'Сообщение1'
    elif irand == 2:
        message = 'Сообщение2'
    elif irand == 3:
        message = 'Сообщение3'
    elif irand == 4:
        message = 'Сообщение4'
    elif irand == 5:
        message = 'Сообщение5'

    domain = 'id'  #id send here
    api.messages.send(domain=domain, message=message)

    print("Message sent", time.strftime("%H:%M:%S"))

def main():
    itimerand = random.randint(60, 1800)
    time.sleep(itimerand)
    send_message()
# Send message
main()
