#!/usr/bin/env python
'''
publisher
KentStateRobotics Jared Butcher 7/21/2019
'''

import networking
import message
import time

class Publisher:
    __init__(self, networkCore, messageType, source, topic, message):
        if len(source) > message.NAME_LENGTH or len(topic) > message.NAME_LENGTH:
            raise Exception("Topic or source of publisher exceaded maximum length of {} characters".format(message.NAME_LENGTH))
        self.networkCore = networkCore
        self.messageType = messageType
        self.source = padString(source, message.NAME_LENGTH)
        self.topic = padString(topic, message.NAME_LENGTH)
        self.message = message
        self.sequence = 0

    def publish(self, message):
        message['header']['source'] = self.networkCore.name
        message['header']['topic'] = self.topic
        message['header']['timestamp'] = time.time()
        message['header']['sequence'] = self.sequence
        message['header']['messageType'] = self.messageType
        self.networkCore.routeExternal(messsage['header'], self.message.pack(message))

    