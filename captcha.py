from twocaptcha import TwoCaptcha
import time

solver = TwoCaptcha('e6ee3559fc00b2d50e8c72bfb86b13f4')

id = solver.send(file='E:/Coding/hemis_bot/captcha_image.jpg')
time.sleep(20)

code = solver.get_result(id)
