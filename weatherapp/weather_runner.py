import time
import utime

""" OLED SETUP """
from . import esp_01_oled as myoled
time.sleep(1)
  
def fill_show():
    myoled.oled.fill(0)
    myoled.oled.show()

""" NETWORK SETUP """

from . import network_setup
time.sleep(2)

""" NTP SETUP """
from . import ntp_setup
from .ntp_setup import now_date
time.sleep(2)


""" WEATHER APP """
_MIN_FREQUENCY = const(5)
import ujson
import utime
import urequests

lat=LAT
lon=LON
key='YOUR_API_KEY'
url="https://api.openweathermap.org/data/2.5/weather?lat=lat&lon=lon&appid=key&units=imperial"

while True:

    myoled.oled.text("Connecting...",0,0)
    weather=urequests.get(url)
    weather=ujson.loads(weather.text)
    city=weather['name']
    temp=weather['main']['temp']
    hum=weather['main']['humidity']
    info=weather['weather'][0]['description']

    myoled.oled.fill(0)
    myoled.oled.show()

    try:
        yr, mt, dy, hr, mn, s1, s2, s3 =  time.localtime()
        if hr < 10:
            hr = f'0{str(hr)}'
        if mn < 10:
            mn = f'0{str(mn)}'
        short_yr = str(yr)[2:]
        myoled.oled.text(
            f'{str(mt)}-{str(dy)}-{str(short_yr)} {str(hr)}:{str(mn)}', 0, 0
        )
        myoled.oled.text(city, 0, 17)
        myoled.oled.text(f"{str(temp)}F", 0, 34)
        myoled.oled.text(info,0, 51)
        myoled.oled.show()
    except Exception as e:
        myoled.oled.text(str(e), 0, 0 )
        myoled.oled.show()
    time.sleep(60 * _MIN_FREQUENCY)
