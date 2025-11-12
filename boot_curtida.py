import pyautogui
from time import sleep
import pyperclip
import webbrowser


# LAÇO: Após 24hrs rodar tudo denovo.
while True:
    # 1- navegar até o instagram "https://www.instagram.com"
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(5)
    pyautogui.press('f11')
    sleep(2)

    # 2 - entrar com meu usuário
    def escrever (frase):
        pyperclip.copy(frase)
        pyautogui.hotkey('ctrl','v')

    button_user = pyautogui.locateCenterOnScreen('button_user.png',confidence=0.8)
    pyautogui.moveTo(button_user[0],button_user[1],duration=1)
    pyautogui.leftClick()
    escrever('Inserir um usuário')

    # 3- entrar com minha senha
    button_password = pyautogui.locateCenterOnScreen('button_password.png',confidence=0.8)
    pyautogui.moveTo(button_password[0],button_password[1],duration=1)
    pyautogui.leftClick()
    escrever('Inserir uma senha')

    # 4- clicar em login
    button_login = pyautogui.locateCenterOnScreen('button_login.png',confidence=0.8)
    pyautogui.moveTo(button_login[0],button_login[1],duration=(1))
    pyautogui.leftClick()
    sleep(5)

    # 5- cliccar em agora não
    button_notnow_instagram = pyautogui.locateCenterOnScreen('button_notnow_instagram.png',confidence=0.8)
    pyautogui.moveTo(button_notnow_instagram[0],button_notnow_instagram[1],duration=1)
    pyautogui.leftClick()
    sleep(1)

    # 6 pesquisar pagina
    button_search = pyautogui.locateCenterOnScreen('button_search.png',confidence=0.8)
    pyautogui.leftClick(button_search[0],button_search[1],duration=1)
    escrever('nike')
    sleep(3)

    # 7 entrar na pagina
    nike_profile = pyautogui.locateCenterOnScreen('nike_profile.png',confidence=0.8)
    pyautogui.leftClick(nike_profile[0],nike_profile[1],duration=1)
    sleep(5)

    # 8 clicar na postagem mais recente
    feed_posts = pyautogui.locateCenterOnScreen('feed_posts.png',confidence=0.8)
    pyautogui.moveTo(feed_posts[0],feed_posts[1],duration=1)
    pyautogui.move(0,80,duration=1)
    pyautogui.leftClick()

    # 9 se já estiver curtido, fazer nada, e pausar oo bot por 24 hrs
    try:
        red_like = pyautogui.locateCenterOnScreen('red_like.png', confidence=0.9)
    except pyautogui.ImageNotFoundException:
        red_like = None

    if red_like is not None:
        sleep(3)

        #sair da conta
        pyautogui.press('esc')
        config_menu = pyautogui.locateCenterOnScreen('config.png',confidence=0.8)  
        pyautogui.leftClick(config_menu[0],config_menu[1],duration=1)
        log_off = pyautogui.locateCenterOnScreen('log_off.png')
        pyautogui.leftClick(log_off[0],log_off[1],duration=1)

        sleep(1)
        pyautogui.press('f11')
        sleep(1)
        pyautogui.hotkey('ctrl','w')
        sleep(1)
        print("Post já está curtido! Aguardando 24 horas...")
        # pausar por 24hrs
        sleep(86.400)

    else:

        # 10 verificar se já está curtida se não estiver curtido, curtir foto e comentar
        gray_like = pyautogui.locateCenterOnScreen('grey_like.png',confidence=0.7, region=(900,800, 200, 150))

        if gray_like is not None:
            
            pyautogui.leftClick(gray_like[0],gray_like[1],duration=1) 
            comment = pyautogui.locateCenterOnScreen('comment.png',confidence=0.8)
            pyautogui.leftClick(comment[0],comment[1],duration=1)
            escrever('Top demais 🔥')
            pyautogui.press('enter')
            sleep(1)

            #sair da conta
            pyautogui.press('esc')
            config_menu = pyautogui.locateCenterOnScreen('config.png',confidence=0.8)  
            pyautogui.leftClick(config_menu[0],config_menu[1],duration=1)
            log_off = pyautogui.locateCenterOnScreen('log_off.png')
            pyautogui.leftClick(log_off[0],log_off[1],duration=1)

            sleep(1)
            pyautogui.press('f11')
            sleep(1)
            pyautogui.hotkey('ctrl','w')


            # pausar por 24hrs
            sleep(86.400)








