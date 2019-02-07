from m5stack import lcd

import time
import ujson
import urequests

class Weather:
    def __init__(self):
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather?q={},jp&appid={}'
        self.api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        self.prefectures = ['Tokyo', 'Saitama', 'Nagoya']

        lcd.setCursor(0, 0)
        lcd.setColor(lcd.WHITE)
        lcd.font(lcd.FONT_DejaVu24)
        self.fw, self.fh = lcd.fontSize()

    def get_weather(self, prefecture):
        response = urequests.get(self.base_url.format(prefecture, self.api_key))
        json = response.json()
        main = json['main']
        self.temp = main['temp']
        self.pressure = main['pressure']
        self.humidity = main['humidity']
        self.temp_min = main['temp_min']
        self.temp_max = main['temp_max']

    def display(self, prefecture):
        lcd.clear()
        lcd.print(prefecture, 0, self.fw * 0)
        lcd.print("temp: {}".format(self.temp), 10, self.fw * 1)
        lcd.print("pressure: {}".format(self.pressure), 10, self.fw * 2)
        lcd.print("humidity: {}".format(self.humidity), 10, self.fw * 3)
        lcd.print("temp_min: {}".format(self.temp_min), 10, self.fw * 4)
        lcd.print("temp_max: {}".format(self.temp_max), 10, self.fw * 5)

weather = Weather()
while True:
    for prefecture in weather.prefectures:
        weather.get_weather(prefecture)
        weather.display(prefecture)
        time.sleep(10)
