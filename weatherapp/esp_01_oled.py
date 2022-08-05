"""

# Esp-01 to OLED on bread board
# https://www.instructables.com/I2C-With-the-ESP8266-01-Exploring-ESP8266Part-1/

Connect USB / FTDI programmer to esp-01 and then to OLED:

esp01 OLED
IO2   sda
IO0   scl

esp-01 pin map
https://www.theengineeringprojects.com/wp-content/uploads/2019/03/introduction-to-esp-01.jpg

"""
from machine import Pin,I2C
from . import ssd1306
i2c = I2C(scl=Pin(0), sda=Pin(2), freq=100000)
oled=ssd1306.SSD1306_I2C(128,64,i2c)

