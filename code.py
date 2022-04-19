# Imports
import board
import digitalio

# ProgIndicator Setup
progIndicator = digitalio.DigitalInOut(board.LED)
progIndicator.direction = digitalio.Direction.OUTPUT

while True:
	progIndicator.value = True