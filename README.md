CPUTemp
========== 
Python GATT server example for the Raspberry Pi
 
Copyright (c) 2019, Douglas Otwell

Distributed under the MIT license http://opensource.org/licenses/MIT 

Prerequisites
-------------
As of BlueZ version 5.50 (currently shipped with Raspbian Buser) there 
is no need to enable experimental flag for bluetoothd. 

Installation 
------------
    git clone https://github.com/douglas6/cputemp.git
    cd cputemp

Usage 
----- 
    python3 cputemp.py

The server should by accessable by any BLE client; I like to use
the 'nRF Connect' app on my Android phone.

The service (UUID 00000001-710e-4a5b-8d75-3e5b444b3c3f) provides 
two characteristics:

UUID 00000002-710e-4a5b-8d75-3e5b444b3c3f: a read/notify
characteristic representing the Pi's CPU temperature as a string.

UUID 00000003-710e-4a5b-8d75-3e5b444b3c3f: a read/write
characteristic indicating the units to use to display the
temperature; 'F' or 'C'.
