import pyautogui as pygui
import time
import keyboard as key
 
x = 1007
num = 1007

while True:
    #Dota 2
    if key.is_pressed('capslock'):
        while x > 7:
            key.press_and_release("shift+enter")
            time.sleep(0.3)
            x = x - 7
            num = str(f"{x}-7")
            pygui.write(str(num))
            time.sleep(0.2)
            key.press_and_release('enter')
            time.sleep(0.2)
    #Discord
    if key.is_pressed('tab'):
        while x > 7:
            x = x - 7
            num = str(f"{x}-7")
            pygui.write(str(num))
            time.sleep(0.5)
            key.press_and_release('enter')
            time.sleep(0.5)