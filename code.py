# Imports
import board
import digitalio
from adafruit_onewire.bus import OneWireBus
from adafruit_ds18x20 import DS18X20
import busio
import adafruit_ssd1306

# ProgIndicator Setup
progIndicator = digitalio.DigitalInOut(board.LED)
progIndicator.direction = digitalio.Direction.OUTPUT

# Temperature Setup
ow_bus = OneWireBus(board.GP5)
temperature = DS18X20(ow_bus, ow_bus.scan()[0])

# Display Setup
i2c = busio.I2C(sda=board.GP0, scl=board.GP1)
display = adafruit_ssd1306.SSD1306_I2C(27, 27, i2c)
def displayTemperatureEdit(temp):
	display.fill(0)
	display.text("Temperature: " + str(float(temp)) + "°C")
	display.show()
while True:
	progIndicator.value = True