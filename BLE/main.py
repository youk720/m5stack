from network import Bluetooth
from m5stack import lcd
lcd.println("start")

bluetooth = Bluetooth()
bluetooth.set_advertisement(name='ESP32', service_uuid=b'1234567890123456')

def conn_cb (bt_o):
    events = bt_o.events()   # this method returns the flags and clears the internal registry
    if events & Bluetooth.CLIENT_CONNECTED:
        lcd.println("Client connected")
    elif events & Bluetooth.CLIENT_DISCONNECTED:
        lcd.println("Client disconnected")

def main():
    bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
    bluetooth.advertise(True)
