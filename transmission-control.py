#! /usr/bin/env python3

from transmission_rpc import Client
import os
import time

# The idea is following: remove alternative speed mode if more than 1 hour passed. 
# For this use "/tmp/transmission_control"

FILE_NAME = "/tmp/transmission_control"

def speedup_transmission():
    client = Client(username='transmission', password='transmission')
    client.set_session(alt_speed_enabled=False)

if __name__ == "__main__":
    if os.path.exists(FILE_NAME):
        file_time = os.path.getmtime(FILE_NAME)
        current_time = time.time()
        if current_time - file_time >= 3600:
            speedup_transmission()
            os.remove(FILE_NAME)
    else:
        open(FILE_NAME, "w")