from machine import Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C
import framebuf

id = 0 
sda = Pin(0)
scl = Pin(1)

i2c = I2C(id =id, scl=scl, sda=sda)

print(i2c.scan())

oled = SSD1306_I2C(width=128, height=64, i2c=i2c)
oled.init_display()
oled.text("Hello World", 0, 0)
oled.show()
oled.invert(1)

with open('frame04.pbm', 'rb') as f:
    f.readline() # magic number
    f.readline() # creator comment
    f.readline() # dimensions
    data = bytearray(f.read())

fb = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

oled.blit(fb, 0,0)
oled.show()