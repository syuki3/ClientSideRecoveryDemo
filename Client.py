import pickle
import socket
import threading
import pymemcache
from threading import Thread
import time

from datetime import datetime

TCP_IP = '0.0.0.0'  # Listening IP (self)
Port = 5005  # Port to listen
BUFFER_SIZE = 5096
#Server1 = '127.0.0.1' #local Server
Server1 = '192.168.50.207'  # Sony
# host2 = '192.168.50.146' #Toshiba
# host3 = '192.168.50.155' #HP
# host4 = '192.168.50.62' #Rocky Linux 1
memcacheClient = pymemcache.Client([Server1, 11211])
log_list = []

class LogEntry:
    def __init__(self, key, value):
        self.time = datetime.utcnow()
        self.Key = key
        self.Value = value
def thread_Listen(name):
    print('Attempting to start server on port 5005..')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_IP, Port))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                try:
                    print('Connected by', addr)
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    if (data == b"Clear"):
                        print("Received Clear Signal, local cache cleared.")
                        log_list.clear()
                    elif (data == b"I rebooted!"):
                        print("Received reboot Signal, sending logs")
                        # Create an instance of ProcessData() to send to server.
                        variable = log_list
                        # Pickle the object and send it to the server
                        log_data = pickle.dumps(variable)
                        conn.sendall(log_data)
                except:
                    print("Connection Closed.")
def main(name):
    t = Thread(target=thread_Listen, args=(1,))
    t.daemon = True
    t.start()
    time.sleep(1)
    while True:
        val = input("Enter Command [Get, Set, PrintCache, QUIT]: ")
        if (val == "Get"):
            key = input("Enter Key: ")
            start_time = time.perf_counter()
            ret = memcacheClient.get(key)
            end_time = time.perf_counter()
            print(f"{key} : {ret} found in {end_time - start_time} seconds");
        elif(val == "Set"):
            key = input("Enter Key: ")
            value = input("Enter value: ")
            start_time = time.perf_counter()
            memcacheClient.set(key, value)
            end_time = time.perf_counter()
            print(f"{key} : {value} Set in {end_time - start_time} seconds");
            log_list.append(LogEntry(key, value))
            #should technically only log if successfully added
        elif(val == "PrintCache"):
            for entry in log_list:
                print(f"{entry.Key} has value {entry.Value}")
        elif(val  == "QUIT"):
            return

if __name__ == '__main__':
    main('PyCharm')
