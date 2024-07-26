import pygame

pygame.init()

def create_font(text="Sample Text", font_color=(255, 255, 255), font_size=40, scale=1):
        font = pygame.font.SysFont("comicsans", font_size*scale)
        img = font.render(text, True, font_color)
        return img

img = create_font("SAMPLE TEXT")

class Button():

    

    def __init__(self, text, cb, cb_args, font_size=20, font_color=(255, 255, 255), scale=1):
        img = create_font(text)
        self.padding = 20

        self.text = text
        self.font_size = int(font_size*scale)
        self.font_color = font_color

        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width*scale), int(height*scale)))
        self.rect = pygame.Rect(0, 0, (self.img.get_width() + (2 * self.padding)), (self.img.get_height() + (2 * self.padding)))

        

        self.cb = cb
        self.cb_args = cb_args

    

    def draw_button(self, surface: pygame.SurfaceType, x, y, centered=False):
        button_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        #get mouse position
        mouse_pos = pygame.mouse.get_pos()
        #check mouseover and clicked
        

        if self.rect.collidepoint(mouse_pos):
            outline_rect = pygame.draw.rect(button_surface, (255, 255, 255, 200), (0,0, self.rect.width, self.rect.height), 3, 10)
            outline_rect.center = (button_surface.get_width() // 2, button_surface.get_height() // 2)
            if pygame.mouse.get_pressed()[0] == 1:
                 self.cb(self.cb_args)

        button_surface.blit(self.img, (self.padding,self.padding))
        if centered:
            #matching collision to pos of text
            self.rect.center = (surface.get_width() // 2, surface.get_height() // 2)
            surface.blit(button_surface, (((surface.get_width() - self.img.get_width()) // 2) - self.padding, ((surface.get_height() - self.img.get_height() ) // 2 ) - self.padding))
        else:
             surface.blit(self.img, x ,y)
        

pygame.quit()