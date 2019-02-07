from m5stack import lcd
import time
import network
lcd.print("action\n")

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("ssid", "pass")
# start_date = time.time()
while not wifi.isconnected():
    # now = time.time()
    lcd.print(".")
    # if now- start_date > timeout_sec:
    #     break
    time.sleep(100)

if wifi.isconnected():
    lcd.print("connected!\n")
else:
    lcd.print("disconnected...\n")
# lcd.print(wifi.ifcongig())
