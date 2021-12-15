# ClientSideRecoveryDemo
Demo code of Client side MemCache recovery using Pymemcache.
This is a basic test project that works as a proof of concept that creating a client sided Memcache recovery system is possible.

This allows for users to get and set keys from the client side, and additionally print the current log data.
The server data may clear its local cache, the client cache, and also request log data from the clients via the restart command.

# Running the app

Prereqs:  
Setup a Server and Client system.
Install MemCache on Server
Install PyMemCache modules for python

1. Restart or clear all key data on MemCached server.
2. Start Client.py
3. Start Server.py 

# Future work and improvements
If you want to enhance and further update this sample project feel free to do so.
On the Serverside I would recommend adding a method of calling a Key dump that writes the key value pairs to disk.
