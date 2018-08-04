import sys
import pygame

def check_keydown_events(event, Ship):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        Ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        Ship.moving_left = True

def check_keyup_events(event, Ship):
    #响应松开
    if event.key == pygame.K_RIGHT:
        Ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        Ship.moving_left = False

def check_events(Ship):
    # 按键与鼠标
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 飞船向右移动
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, Ship)
        # 飞船向左移动
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, Ship)

def update_screen(ai_settings, screen, Ship):
    # 更新屏幕
    screen.fill(ai_settings.bg_color)
    Ship.blitme()

    # 刷新屏幕
    pygame.display.flip()
