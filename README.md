## FrameDuino 0.1 ##

This framework is under development. Alpha version released.

## Examples ##

Examples using raw code and manual configuration.

```
from pinguino import *
from drivers.usb_driver import *

pinguino = Pinguino(USBDriver())
pinguino.pinMode(0,OUTPUT)
pinguino.pinMode(7,INPUT)
pinguino.digitalWrite(0, HIGH)
print pinguino.digitalRead(7)
pinguino.disconnect()
```
