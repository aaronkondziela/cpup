cpup
====

Copy files to a MicroPython internal filesystem like on ESP8266 and ESP32

Because IDE plugins are tiresome, and CLI utilities are nice.

Usage
-----

To get usage:

	cpup -h

	Usage: ./cpup <-f in_filename> [-o out_filename] [-d /dev/ttyACM0] [-s 115200] [-v]
	       ./cpup -h

	Defaults are as shown. Will use -f as -o if -o is not specified.

Note, this does not hold your hand. There are no checks for sufficient space,
and existing files of the same name are simply overwritten. Sharp tool, use
with care, will ya?

Note, file get does not work yet.

Also also wik, `cat.py` can help with that at the REPL. Toss it into `lib/cat.py`, then
`from cat import *` and `cat('filename')`

Pro Tips
--------

Runs on GNU/Linux. Probably won't work on a Mac due to stty weirdness. I have
not tested.

If you happen to have ModemManager running on your GUI-tacular Linux desktop,
get rid of it, because it screws up things like this, dfu-util, etc., by
trying to throw AT commands at newly-attached USB serial devices.

License
-------

Released under MIT license
