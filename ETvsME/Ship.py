import pygame


class Ships:
    def __init__(self, ai_settings, screen):
        # 初始位置
        self.screen = screen
        # 加载飞船
        self.image = pygame.image.load('images/hero.gif')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 每艘新飞船刷新在底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 连续移动状态
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 连续移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
