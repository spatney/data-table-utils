'''Rabbit helper'''
import socket
import time
import os
import pika


class SingletonMeta(type):
    '''META Class'''

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonConnection(metaclass=SingletonMeta):
    '''SingletonConnection'''

    def __init__(self):
        '''init'''
        self._connection = None

    def get_connection(self):
        '''get connection'''
        if self._connection is None or self._connection.is_closed:
            self._connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=os.getenv('RABBIT_HOST_NAME'),
                    port=5672,
                    credentials=pika.PlainCredentials(
                        username=os.getenv('RABBIT_USERNAME'),
                        password=os.getenv('RABBIT_PASSWORD')
                    )
                )
            )
        return self._connection


def wait_for_rabbit_to_be_online():
    '''wait_for_rabbit_to_be_online'''
    print("checking if rabbit is online ...")
    pingcounter = 0
    is_reachable = False
    retry_timeout = 3
    while is_reachable is False and pingcounter < 5:
        rabbit_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            rabbit_socket.connect((os.getenv('RABBIT_HOST_NAME'), 5672))
            is_reachable = True
            time.sleep(retry_timeout)
        except socket.error:
            print("rabbit still waking up ... will retry")
            time.sleep(retry_timeout)
            pingcounter += 1
        rabbit_socket.close()

    if is_reachable:
        print("rabbit is alive!")
    else:
        print("giving up, rabbit still down")
