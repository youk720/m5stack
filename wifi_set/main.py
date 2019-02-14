from m5stack import *
import network
import socket
import time

ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid="m5stack", authmode=network.AUTH_WPA_WPA2_PSK, password=b"micropythoN")
ap_if.active(True)
lcd.println(str(ap_if.ifconfig()))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    conn.send("<h1>test!!</h1>")
    conn.close()
