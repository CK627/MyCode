import pyautogui
from pynput.keyboard import Key, Controller
import time

content = input("您要轰炸的内容：")
times = eval(input("您要轰炸的次数："))

pyautogui.hotkey('ctrl', 'alt', 'w')

keyboard = Controller()
for i in range(times):
    keyboard.type(content)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)     # 间隔0.1s
