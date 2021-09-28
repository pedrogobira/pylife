from sys import exit

import pygame

WIDTH = 800
HEIGHT = 600

COLOR_BLACK = pygame.Color(0, 0, 0)
COLOR_WHITE = pygame.Color(255, 255, 255)
COLOR_GREEN = pygame.Color("green")

# inicializando jogo
pygame.init()

FPS = 60

# propriedades da janela
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pylife")

# definindo fonte base
FONT = pygame.font.Font(None, 32)


def init_players_view():
    user_text = ""

    # caixa do input de texto e cor do mesmo
    input_rect = pygame.Rect(200, 200, 140, 32)
    input_rect_active_color = pygame.Color(0, 0, 200)
    input_rect_inactive_color = pygame.Color(240, 240, 240)
    input_rect_current_color = input_rect_inactive_color

    button_rect = pygame.Rect(200, 240, 100, 30)

    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                # lendo o que é digitado
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        if len(user_text) < 25:
                            user_text += event.unicode

        # preenchendo background com cor
        WIN.fill(COLOR_BLACK)

        # atualizando cor do input
        if active:
            input_rect_current_color = input_rect_active_color
        else:
            input_rect_current_color = input_rect_inactive_color

        # desenhando retangulo do input na tela
        pygame.draw.rect(WIN, input_rect_current_color, input_rect, 2)

        # desenhando botao
        pygame.draw.rect(WIN, COLOR_GREEN, button_rect)

        # criando camada para o texto
        text_surface = FONT.render(user_text, True, (255, 255, 255))

        # desenhando camanda de texto na tela na posicao da caixa de input
        WIN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # caixa de input acompanha o tamanho da camada de texto
        input_rect.w = max(140, text_surface.get_width() + 10)

        # atualizando tela parcialmente
        draw_window()


def draw_window():
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    draw_window()


if __name__ == "__main__":
    init_players_view()