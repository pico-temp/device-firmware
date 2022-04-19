# Imports
import board
import digitalio
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20

# ProgIndicator Setup
progIndicator = digitalio.DigitalInOut(board.LED)
progIndicator.direction = digitalio.Direction.OUTPUT

# Temperature Setup
ow_bus = OneWireBus(board.D2)
temperature = DS18X20(ow_bus, ow_bus.scan()[0])

while True:
	progIndicator.value = True