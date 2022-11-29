from fileinput import close
import webbrowser
import pyautogui
import time

#abre o navegador
def abreNav():
    #url = 'https://localhost:80'
    #webbrowser.get('chrome').open(url)
    webbrowser.open('https://localhost:80')
    time.sleep(2)
    
#nova aba
def abreAba():
    pyautogui.hotkey('ctrl', 't')
    time.sleep(2)

#fecha aba
def fechaAba():
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)

#abre aba anonima
def abreAnon():
    pyautogui.hotkey('ctrl', 'shift', 'n')
    time.sleep(2)

#cola link e roda
def colaRoda():
    pyautogui.write('https://www.youtube.com/watch?v=f0FjItTl3M4')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

#captura de mouse na tela
def clickMouse():
    global position, moveto, clickLeft, clickRight
    position = x, y = pyautogui.position(804, 704)
    moveto = pyautogui.moveTo(position)
    time.sleep(3)
    clickLeft = pyautogui.leftClick(position)
    # clickRight = pyautogui.rightClick(position)
    print(f"O mouse está na posicao {position}, e foi movido para , {moveto} e clicou em {clickLeft}")
    time.sleep(3)


#encerra chrome
def fim():
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)

#roda script
def main():
    abreNav()
    abreAnon()
    colaRoda()
    clickMouse()
    fechaAba()
    fim()

if __name__ == '__main__':
    main()

# #laco para repetir script
# while(True):
#     main()