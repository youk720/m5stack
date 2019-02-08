from m5stack import lcd
import network
import socket
import time

def connect():
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect("nstudents", "nnnedjpwireless")
    while station.isconnected() == False:
        lcd.print(".")
        time.sleep(0.5)
        pass
    lcd.print("\n")
    lcd.println("connected")
    lcd.println(str(station.ifconfig()))
connect()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    conn.send("<h1>test!!</h1>")
    conn.close()
