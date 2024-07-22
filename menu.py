import pygame

def draw_text(screen: pygame.Surface, text: str, x: int, y: int):
    # font
    font = pygame.font.SysFont("comicsans", 40)
    
    # text color 
    TEXT_COL = (255, 255 ,255)

    img = font.render(text, True, TEXT_COL)
    img_rect = img.get_rect()
    img_rect.center = (screen.get_width() / 2, screen.get_height() / 2)
    screen.blit(img, img_rect)