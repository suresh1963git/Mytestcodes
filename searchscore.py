import pyautogui
import time
import webbrowser

# small pause before script starts
time.sleep(2)

# open browser
webbrowser.open("https://www.google.com")

# wait for browser to open
time.sleep(4)

# type search text
pyautogui.write("south africa vs australia score", interval=0.05)
pyautogui.press("enter")

# wait for results to load
time.sleep(4)

pyautogui.press("enter")