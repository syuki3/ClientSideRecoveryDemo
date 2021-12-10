import pickle
import socket
import time

from datetime import datetime

TCP_IP = '0.0.0.0'  # Listening IP (self)
Port = 5005  # Port to listen
BUFFER_SIZE = 5096
# host1 = '192.168.50.207' #Sony
# host2 = '192.168.50.146' #Toshiba
# host3 = '192.168.50.155' #HP
# host4 = '192.168.50.62' #Rocky Linux 1


class LogEntry:
    def __init__(self, key, value):
        self.time = datetime.utcnow()
        self.Key = key
        self.Value = value


def print_hi(name):
    print('Attempting to start server on port 5005..')
    entry1 = LogEntry("key2-1", 123)
    time.sleep(1)
    entry2 = LogEntry("key2-2", 456)
    time.sleep(1)
    entry3 = LogEntry("key2-3", 789)
    log_list = [entry2, entry3, entry1]
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((TCP_IP, Port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                # Create an instance of ProcessData() to send to server.
                variable = log_list
                # Pickle the object and send it to the server
                log_data = pickle.dumps(variable)
                conn.sendall(log_data)


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
