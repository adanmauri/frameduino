> ⚠️ **Deprecated.** This project's successor is [liveduino](https://github.com/adanmauri/liveduino) — use that for new projects.

## FrameDuino ##

FrameDuino is a Python 2 framework that talks to a [Pinguino](https://github.com/PinguinoIDE/pinguino) board using the Arduino-style API you already know: `pinMode`, `digitalWrite`, `digitalRead`, `analogRead`, `analogWrite`, `eepromRead`/`eepromWrite`. The `usb_interpreter.pde` firmware runs on the board and listens for these commands over USB, Bluetooth, or serial, so your Python script drives the hardware directly, without compiling and flashing a sketch for every change.

This project is no longer under active development; see [Status](#status) below.

## Status ##

**FrameDuino is legacy.** It was an alpha, Python 2 only, and Pinguino only.

Its spiritual successor is **[liveduino](https://github.com/adanmauri/liveduino)**: the same idea, rebuilt from scratch for Python 3.13+, targeting Arduino boards (UNO, Nano, Mini, Pro Mini, Fio, and more) over the standard Firmata protocol, with USB, Wi-Fi/Ethernet, and Bluetooth drivers, servo and I2C support, a CLI that flashes firmware for you, and 100% test coverage.

If you're starting a new project, use [liveduino](https://github.com/adanmauri/liveduino) instead. FrameDuino stays here for historical reference and for anyone still working with a Pinguino board.

## Examples ##

Examples using raw code and manual configuration.

```python
from pinguino import *
from drivers.usb_driver import *

pinguino = Pinguino(USBDriver())
pinguino.pinMode(0,OUTPUT)
pinguino.pinMode(7,INPUT)
pinguino.digitalWrite(0, HIGH)
print pinguino.digitalRead(7)
pinguino.disconnect()
```

## Drivers ##

FrameDuino ships drivers for connecting to a Pinguino board over:

- USB (`usb_driver.py`)
- Serial (`serial_driver.py`)
- Bluetooth (`bt_driver.py`)
- CDC (`cdc_driver.py`)

## Firmware ##

`pinguino/usb_interpreter.pde` is the Pinguino sketch that must be flashed to the board; it parses the incoming commands and calls the matching Arduino/Wiring function.

## License ##

Distributed under the GPLv2 (or later) license. See [LICENSE](LICENSE) and [NOTICE](NOTICE) for details.
