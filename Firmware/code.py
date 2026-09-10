import board
import busio
import neopixel
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.keys import KC

keyboard = KMKKeyboard()


encoder_handler = EncoderHandler()
keyboard.extensions.append(MediaKeys())

keyboard.row_pins = (board.GP1, board.GP2, board.GP4)
keyboard.column_pins = (board.GP28, board.GP29, board.GP0)
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

keyboard.modules = [Layers(), encoder_handler]



OLED_SCL = board.GP6
OLED_SDA = board.GP7

LED_PIN = board.GP3
LED_COUNT = 12

MOD_LAYER = KC.TG(1)


keyboard.keymap = [
    [#layer media
        KC.MPRV, KC.MNXT, MOD_LAYER,
        KC.MPLY, KC.MSTP, KC.MUTE,
        KC.N7, KC.N8, KC.N9
    ],
   [#layer function
       KC.F1, KC.F2, MOD_LAYER,
       KC.F3, KC.F4, KC.F5,
       KC.F6, KC.F7, KC.F8
   ]
   # next update is for blender layer
]


#next update is to make the oled interact current playing music or audio
i2c = busio.I2C(OLED_SCL, OLED_SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128,32,i2c,addr=0x3C)


oled.fill(0)
oled.text("MACROPAD", 0, 0, 1)
oled.text("Ready", 0, 24, 1)
oled.show()

encoder_handler.pins = (board.GP26, board.GP27)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
    ((KC.VOLU, KC.VOLD),),
]


pixels = neopixel.NeoPixel(LED_PIN,
    LED_COUNT,
    brightness=0.2,
    auto_write=False,
    pixel_order=neopixel.GRB)

pixels.fill((255, 255, 255))
pixels.show()

if __name__ == '__main__':
    keyboard.go()


    # while True:
    #     layer = keyboard.active_layers[0]

    #     oled.fill(0)
    #     oled.text("MACROPAD", 0, 0, 1)

    #     if layer == 0:
    #         oled.text("MEDIA", 0, 12, 1)
    #     elif layer == 1:
    #         oled.text("FUNCTION", 0, 12, 1)

    #     oled.show()
