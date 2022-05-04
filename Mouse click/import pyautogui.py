import pyautogui
import keyboard

while (1):
    print("Elindul a program")
    pyautogui.click(5279,1511,duration=1)
    print("Fut a program")
    try:
        if keyboard.is_pressed('q'): 
            break
        else:
            pass
    finally:
            pass
