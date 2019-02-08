# 各種ライブラリ導入
from m5stack import lcd
import time
import network
import urequests

# Wi-Fi系各種定義
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
# SSID & PassWord入力
wifi.connect("nstudents", "nnnedjpwireless")

# While文で接続待ちをする
while not wifi.isconnected():
    lcd.print(".")
    time.sleep(0.1)

# Getしたデータを画面に表示する
response = urequests.get('http://jsonplaceholder.typicode.com/albums/1')
lcd.print("\n")
lcd.println(response.text)
