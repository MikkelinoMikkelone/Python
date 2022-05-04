SystemModules 
import pyautogui
import keyboard
print(pyautogui.size())

run = True

while run==True:
    
        if keyboard.read_key() == "s":
            print("Megall a program")
            break 
        pyautogui.click(5279,1511,duration=3)
    

