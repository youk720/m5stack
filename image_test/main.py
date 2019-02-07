# ライブラリ導入
from m5stack import lcd

# 初期化
lcd.clear()

# 画像挿入
lcd.image(lcd.CENTER, lcd.BOTTOM, file="/flash/icon.jpg")

# 見出し
lcd.setCursor(0, 0)
lcd.setColor(lcd.WHITE, lcd.BLUE)

fw, fh = lcd.fontSize()
ww, wh = lcd.winsize()

lcd.rect(0, 0, ww, fh + 1, lcd.BLUE, lcd.BLUE)
lcd.println("N High School students Card")

# 文字
lcd.font(lcd.FONT_Comic)
lcd.setColor(lcd.WHITE, lcd.BLACK)
lcd.print('Waricoma', 10, 30)
