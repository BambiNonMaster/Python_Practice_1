import pygame
import sys
from Setting import Settings
from Ship import Ships
import Game_funcitons as gf


def run_game():
    ai_settings = Settings()
    pygame.init()
    # 屏幕大小
    screen = pygame.display.set_mode((ai_settings.screen_widt, ai_settings.screen_height))
    # 字体
    pygame.display.set_caption("Alien Invasion")
    # 创建飞船
    Ship = Ships(ai_settings,screen)

    while True:
        gf.check_events(Ship)
        Ship.update()
        gf.update_screen(ai_settings, screen, Ship)
        screen.fill(ai_settings.bg_color)
        Ship.blitme()
        pygame.display.flip()


run_game()
