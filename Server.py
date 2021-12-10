import socket
import pickle
import pymemcache
from datetime import date

TCP_PORT = 5005
BUFFER_SIZE = 5096
MESSAGE = b"I rebooted!"
# LocalHost = '192.168.50.32'
client2 = '192.168.50.173'  # rocky linux 2
client3 = '192.168.50.44'   # Rocky Linux 3
Server1 = '192.168.50.207'  # Sony
Server2 = '192.168.50.146'  # Toshiba
Server3 = '192.168.50.155'  # HP
Server4 = '192.168.50.62'  # Rocky Linux 1
memcacheClient = pymemcache.Client([Server1, 11211])

log_list = []
client_list = [client2, client3]

class LogEntry:
    def __init__(self, key, value):
        self.time = date.today()
        self.Key = key
        self.Value = value


def print_hi(name):
    for client in client_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((client, TCP_PORT))
        s.sendall(MESSAGE)
        data_encoded = s.recv(BUFFER_SIZE)
        s.close()
        singleClientLog = pickle.loads(data_encoded)
        for entry in singleClientLog:
            log_list.append(entry)
    log_list.sort(key=lambda r: r.time)
    for entry in log_list:
        print(f"Recovered and setting {entry.Key} with value {entry.Value}")
        memcacheClient.set(entry.Key, entry.Value)
    memcacheClient.close()
    # Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
