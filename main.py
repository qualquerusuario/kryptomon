import pyautogui
import time

kryptomon_x = 1089
kryptomon_y = 660
contador = 0
pyautogui.sleep(1)


def comida(x, y):
    time.sleep(5)
    pyautogui.click(x=810, y=881)
    time.sleep(1)
    pyautogui.click(x=737, y=965)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.mouseUp()


def vida(x, y):
    time.sleep(6)
    pyautogui.click(x=899, y=879)
    time.sleep(2)
    pyautogui.click(x=737, y=965)
    time.sleep(2)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.mouseUp()


def toys(x, y):
    time.sleep(6)
    pyautogui.click(x=984, y=883)
    time.sleep(2)
    pyautogui.click(x=737, y=965)
    time.sleep(2)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.mouseUp()


def treinar(x, y, treino):
    time.sleep(7)
    pyautogui.click(x=1065, y=880)
    time.sleep(2)
    pyautogui.click(treino, y=960)
    time.sleep(2)
    pyautogui.mouseDown()
    pyautogui.mouseDown()
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.mouseUp()



while True:
    contador += 1
    comida(x = kryptomon_x ,y =kryptomon_y)
    vida(x = kryptomon_x ,y =kryptomon_y)
    toys(x = kryptomon_x ,y =kryptomon_y)
    if contador == 1:
        treinar(x=kryptomon_x, y=kryptomon_y, treino=739)
    elif contador == 2:
        treinar(x=kryptomon_x, y=kryptomon_y, treino=878)
    elif contador == 3:
        treinar(x=kryptomon_x, y=kryptomon_y, treino=1011)
    else:
        treinar(x=kryptomon_x, y=kryptomon_y, treino=1151)
        time.sleep(2)
        contador = 0

    time.sleep(1800)
