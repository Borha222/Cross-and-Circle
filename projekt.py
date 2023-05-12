import pygame
import sys

pygame.init()
pkt_1 = 0
pkt_2 = 0
ktora_gra = 1
szerokosc = 300
wysokosc = 400
szer_lini = 2
wielk_tab = 3
wiel_komorki = szerokosc // wielk_tab

tlo_kol = (255, 255, 255)
linie_kol = (0, 0, 0)
kolko_kol = (255, 0, 0)
krzyzyk_kol = (0, 0, 255)
def wstawianie():
    for y in range(wielk_tab):
        for x in range(wielk_tab):
            if plasza[x][y] == "O":
                pygame.draw.circle(screen, kolko_kol, (x * wiel_komorki + wiel_komorki // 2, y * wiel_komorki + wiel_komorki // 2), wiel_komorki // 2 - 20, szer_lini)
            elif plasza[x][y] == "X":
                pygame.draw.line(screen, krzyzyk_kol, (x * wiel_komorki + 20, y * wiel_komorki + 20), (x * wiel_komorki + wiel_komorki - 20, y * wiel_komorki + wiel_komorki - 20), szer_lini)
                pygame.draw.line(screen, krzyzyk_kol, (x * wiel_komorki + wiel_komorki - 20, y * wiel_komorki + 20), (x * wiel_komorki + 20, y * wiel_komorki + wiel_komorki - 20), szer_lini)

def sprawdzanie():
    global zwyciesca,gra_skonczona
    for y in range(wielk_tab):
        if plasza[y][0] == plasza[y][1] == plasza[y][2] is not None:
            zwyciesca = plasza[y][0]
            gra_skonczona = True
        elif plasza[0][y] == plasza[1][y] == plasza[2][y] is not None:
            zwyciesca = plasza[0][y]
            gra_skonczona = True
    if plasza[0][0] == plasza[1][1] == plasza[2][2] is not None:
        zwyciesca = plasza[0][0]
        gra_skonczona = True
    elif plasza[0][2] == plasza[1][1] == plasza[2][0] is not None:
        zwyciesca = plasza[0][2]
        gra_skonczona = True
def Gra():
    game_essa=False
    game_over = False
    gracz = "X"
    p = 0
    global plasza,screen,gra_skonczona,zwyciesca,pkt_1,pkt_2,ktora_gra
    plasza = [[None] * wielk_tab for i in range(wielk_tab)]
    screen = pygame.display.set_mode((szerokosc, wysokosc))
    pygame.display.set_caption("Kółko i krzyżyk")
    screen.fill(tlo_kol)
    for x in range(1, wielk_tab):
        pygame.draw.line(screen, linie_kol, (x * wiel_komorki, 0), (x * wiel_komorki, wysokosc - 100), szer_lini)
        pygame.draw.line(screen, linie_kol, (0, x * wiel_komorki), (szerokosc, x * wiel_komorki), szer_lini)
    font = pygame.font.Font(None, 24)
    text = font.render("Punkty 1 gracza: " + str(pkt_1), True, linie_kol)
    screen.blit(text, (0, 325))
    font = pygame.font.Font(None, 24)
    text = font.render("Punkty 2 gracza: " + str(pkt_2), True, linie_kol)
    screen.blit(text, (0, 375))
    gra_skonczona = False
    zwyciesca = None
    pygame.display.update()
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not gra_skonczona:
                myszka_x, myszka_y = pygame.mouse.get_pos()
                if myszka_y>300:
                    myszka_y = 299
                komorka_x = myszka_x // wiel_komorki
                komorka_y = myszka_y // wiel_komorki
                if plasza[komorka_x][komorka_y] is None:
                    plasza[komorka_x][komorka_y] = gracz
                    p+=1
                    sprawdzanie()
                    if gracz == "X":
                        gracz = "O"
                    else:
                        gracz = "X"
                wstawianie()
                pygame.display.update()
                if gra_skonczona:
                    font = pygame.font.Font(None, 36)
                    text = font.render("Wygrał: " + zwyciesca, True, linie_kol)
                    screen.blit(text, (szerokosc // 2 - text.get_width() // 2, wysokosc // 2 - text.get_height() // 2))
                    font = pygame.font.Font(None, 24)
                    text1 = font.render("Nacisnij R- by zagrać ponownie", True, linie_kol)
                    screen.blit(text1, (szerokosc // 2 - text1.get_width() // 2, wysokosc // 1.8 - text1.get_height()//2))
                    font = pygame.font.Font(None, 24)
                    text2 = font.render("Nacisnij Q- by zakończyć", True, linie_kol)
                    screen.blit(text2, (szerokosc // 2 - text2.get_width() // 2, wysokosc // 1.6 - text2.get_height()//2))
                    pygame.display.update()
                    if ((zwyciesca=="X")&(ktora_gra%2==1))|((zwyciesca=="O")&(ktora_gra%2==0)):
                        pkt_1+=1
                        ktora_gra+=1
                        game_essa= True
                    else:
                        pkt_2+=1
                        ktora_gra+=1
                        game_essa = True
                elif p==9:
                    font = pygame.font.Font(None, 48)
                    text = font.render("Remis!", True, linie_kol)
                    screen.blit(text, (szerokosc // 2 - text.get_width() // 2, wysokosc // 2 - text.get_height() // 2))
                    text1 = font.render("Nacisnij R- by zagrać ponownie", True, linie_kol)
                    screen.blit(text1, (szerokosc // 2 - text1.get_width() // 2, wysokosc // 1.8 - text1.get_height() // 2))
                    font = pygame.font.Font(None, 24)
                    text2 = font.render("Nacisnij Q- by zakończyć", True, linie_kol)
                    screen.blit(text2, (szerokosc // 2 - text2.get_width() // 2, wysokosc // 1.6 - text2.get_height() // 2))
                    game_essa = True
                    pygame.display.update()
        if game_essa:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key== pygame.K_r:
                            Gra()
                        elif event.key==pygame.K_q:
                            game_over=True
Gra()
