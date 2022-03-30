import pyautogui
import time

pyautogui.sleep(1)


def comida():
    time.sleep(12)
    pyautogui.click(x=813, y=780)
    time.sleep(1)
    pyautogui.click(x=732, y=863)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.moveTo(x=963, y=628)
    time.sleep(1)
    pyautogui.mouseUp()


def vida():
    time.sleep(6)
    pyautogui.click(x=897, y=782)
    time.sleep(2)
    pyautogui.click(x=729, y=866)
    time.sleep(2)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.moveTo(x=963, y=628)
    time.sleep(1)
    pyautogui.mouseUp()


def toys():
    time.sleep(6)
    pyautogui.click(x=985, y=783)
    time.sleep(2)
    pyautogui.click(x=734, y=858)
    time.sleep(2)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.moveTo(x=963, y=628)
    time.sleep(1)
    pyautogui.mouseUp()


def treinar():
    time.sleep(7)
    pyautogui.click(x=1069, y=784)
    time.sleep(2)
    pyautogui.click(x=1014, y=861)
    time.sleep(2)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.moveTo(x=963, y=628)
    time.sleep(1)
    pyautogui.mouseUp()



while True:
    comida()
    vida()
    toys()
    treinar()
    time.sleep(1800)
