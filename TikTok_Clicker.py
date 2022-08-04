import time
import pyautogui
import random
import PySimpleGUI as sg      
import webbrowser
import sys
import keyboard


def exit_func():
    if keyboard.is_pressed('F2'):
        sys.exit()
    
def sleep_func():
    time.sleep((random.uniform(0.8, 2.2)))
    
def a(b):
    for i in range(b):
        exit_func()
        pyautogui.moveTo(683, 572)
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.doubleClick()
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.moveTo(1333, 559)
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.click()
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.moveTo(683, 572)
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.doubleClick()
        exit_func()
        sleep_func()
        exit_func()
def a_2(b):
    for i in range(b):
        exit_func()
        pyautogui.moveTo(683, 572)
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.doubleClick()
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.moveTo(1833, 151)
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.click()
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.moveTo(1333, 559)
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.click()
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.moveTo(683, 572)
        exit_func()
        sleep_func()
        exit_func()
        pyautogui.doubleClick()
        exit_func()
        sleep_func()
        exit_func()
sg.theme('DarkGrey13')  

author = sg.Button('Created by Maik ßⒸ', enable_events=True, key='-LINK-', button_color=('white', 'grey'))

layout = [[sg.Text("""

▀█▀ █ █▄▀ ▀█▀ █▀█ █▄▀  
░█░ █ █░█ ░█░ █▄█ █░█  

█▄▄ █▀█ ▀█▀   ▄▄   ▀█ █▀█ ▀█ ▀█
█▄█ █▄█ ░█░   ░░   █▄ █▄█ █▄ █▄
                   """)], [sg.T("")],
          [sg.Text(':')], 
          [sg.Text('- The space bar function')], 
          [sg.Text('- Turn on TikTok in full screen')],
          [sg.Text('- Press ENTER or click Ok')],
          [sg.Text(" ")],
          [sg.Text('How many likes would you like to give?')], 
          [sg.InputText()], [sg.T("")], 
          [sg.Text('Leave a follow?')], 
          [sg.Radio('Yes', "RADIO1", default=True, key="-IN2-")],
          [sg.Radio('No', "RADIO1", default=False)],
          [author, sg.T("                  "), sg.Ok(button_color=('white', 'grey')), sg.Cancel(button_color=('white', 'grey'), key='-CANCEL-')],
          [sg.Text(" ")],
          [sg.Text('WARNING! TO STOP PROGRAM START PRESSING F2...')],
          ]      

window = sg.Window('TikTok Bot - 2022 v0.01', layout, margins=(100, 50))
  

event, values = window.read() 

text_input = values[0]


if event == '-CANCEL-':
    window.close()
    sys.exit()

if event == '-LINK-':
    webbrowser.open(r'https://eune.op.gg/summoners/eune/Maik%20%C3%9F')
    window.close()
    sys.exit()
    
while isinstance(text_input, str):
    try:
        text_input = int(text_input)
    except:
        sg.popup('Error, please try again.')
        window.close()
        sys.exit()
        break
    
if text_input <= 0:
    sg.popup('Error, please try again.')
    window.close()
    sys.exit()
else:
    sg.popup(f"""You entered: {text_input}
    Have fun 🙂""")
    window.close()
   
if values["-IN2-"] == True:
    a_2(text_input)
else:
    a(text_input)

window.close()
sys.exit()  