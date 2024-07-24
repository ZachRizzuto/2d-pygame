import pygame

pygame.init()

def create_font(text, font_color=(255, 255, 255), font_size=40, scale=1):
        font = pygame.font.SysFont("comicsans", font_size*scale)
        img = font.render(text, True, font_color)
        return img

img = create_font("Start Game")

class Button():

    

    def __init__(self, text, cb, cb_args, font_size=20, font_color=(255, 255, 255), img=img, scale=1):
        width = img.get_width()
        height = img.get_height()

        self.text = text
        self.font_size = int(font_size*scale)
        self.font_color = font_color
        self.img = pygame.transform.scale(img, (int(width*scale), int(height*scale)))
        self.rect = self.img.get_rect()
        self.cb = cb
        self.cb_args = cb_args


    text = ""

    

    def draw_button(self, surface: pygame.SurfaceType, x, y):
        #get mouse position
        mouse_pos = pygame.mouse.get_pos()
        #check mouseover and clicked
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                 self.cb(self.cb_args)
                 
                 
        self.rect.topleft = (x, y)
        surface.blit(img, (self.rect.x, self.rect.y))

pygame.quit()