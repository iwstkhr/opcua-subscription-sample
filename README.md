# OPC UA Subscription Sample
Python sample of subscribing data change using asyncua


## Requirements
Only [asyncua library](https://github.com/FreeOpcUa/opcua-asyncio) is needed. Install it by the following command.

```sh
$ pip install asyncua
```


## Usage
First, start an OPC UA testing server which writes a random int value to a variable node every second.
The following sample Python script starts the testing server with `opc.tcp://localhost:4840`, having a variable node `MyObject/MyVariable`.

```sh
$ python server.py
Server started: OPC UA Server(opc.tcp://localhost:4840)
```

Then, run an OPC UA client script which reacts to data change notifications from the above OPC UA server.
You can define an event handler `datachange_notification` in a class and pass it to `create_subscription` function.

```sh
$ python client.py
Data change notification was received and queued.
New value 4 of "['0:Root', '0:Objects', '2:MyObject', '2:MyVariable']" was processed.
Data change notification was received and queued.
New value 79 of "['0:Root', '0:Objects', '2:MyObject', '2:MyVariable']" was processed.
Data change notification was received and queued.
New value 75 of "['0:Root', '0:Objects', '2:MyObject', '2:MyVariable']" was processed.
...
```
