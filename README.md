# ClientSideRecoveryDemo
Demo code of Client side MemCache recovery using Pymemcache.
This is a basic test project that works as a proof of concept that creating a client sided Memcache recovery system is possible.

The scenario is that a client was setting Key value pairs to a server crashes.
Once the server crashes, it sends out a signal indicating it restarted on the Server.py startup.
The signal gets received by Client.py and Clieny2.py and sends logged data back to the server.
The server receives the log data, sorts it; and replays it back to rebuild it's cache.

# Running the app

Prereqs:  
Setup a Server and Client system.
Install MemCache on Server

1. Restart or clear all key data on MemCached server.
2. Start Client.py and Client2.py
3. Start Server.py 

# Future work and improvements
If you want to enhance and further update this sample project feel free to do so.
I  would suggest wrapping the client.py in a library that has simple Get, and Set commands from PyMemCache.
Upon doing a Set command, add the data to the log objects.

On the Serverside I would recommend adding a method of calling a Key dump that writes the key value pairs to disk.
The server should then send a different signal to the Clients indicating they may clear their logs.
