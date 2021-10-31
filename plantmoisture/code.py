import board
import analogio
import neopixel
import time
import const # separate file const.py on the device

a1 = analogio.AnalogIn(board.A1)
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

dry_max = 20.0
good_max = 60.0
reading_max = 5

DRY_COLOR = (255, 0, 0)
GOOD_COLOR = (0, 255, 0)
WET_COLOR = (0, 0, 255)

def set_color(moisture):
    color = ""
    print(f'avg {moisture}')

    if moisture <= dry_max:
        color = DRY_COLOR
    elif moisture >= good_max:
        color = WET_COLOR
    else:
        color = GOOD_COLOR

    for i in range(10):
        pixels[i] = color
    pixels.show()

while True:
    sum = 0
    for i in range(reading_max):
        sum += a1.value
        time.sleep(0.2)

    moisture = sum / reading_max
    moisture = moisture / 1000

    set_color(moisture)
    print(const.BAM)
