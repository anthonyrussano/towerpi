import board
import neopixel

# Setup for NeoPixel
pixels = neopixel.NeoPixel(board.D18, 4)  # Assuming 4 LEDs connected to GPIO18

# Define an orange color. You might need to adjust the values to get the shade you want.
orange_color = (255, 80, 0)  # This is a common RGB representation for orange.

# Set all LEDs to orange
for i in range(4):  # Assuming there are 4 LEDs
    pixels[i] = orange_color
