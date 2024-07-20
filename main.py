import pygame
import player_movement
# Initializing the Pygame library
pygame.init()
# Screen Settings in PX
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.display.set_caption("2D Game Alpha")
# Player Dimensions
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

player_speed = 5

# Game tick rate pretty much
clock = pygame.time.Clock()
# Delta time, it allows game to run outside of 60 fps and so it doesn't break when you get more than 60. Its a whole thing if you wanna research it. Pygame does it easy
dt = 0

# Screen Object used for drawing onto the screen and what have you
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# player position (there are other ways of doing this but this is how documentation references it to start (I am also learning pygame as we go (I know parenthesis in parenthesis (In parenthesis))))
PLAYER_POS = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

PLAYER_SPRITE_IMAGE = pygame.image.load("./assets/boy_down_1.png")
player_sprite = pygame.transform.scale(PLAYER_SPRITE_IMAGE, (100, 100))

player = player_movement.Player(player_speed, player_sprite, PLAYER_POS)
run = True

while run:

    # Checking if player closes game or not and closing if true
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Refreshes screen by filling it with a random color (not sure how this works for most games but this is how pygame does it for the most part)
    screen.fill((0,0,0))


    movement_vector = pygame.math.Vector2(0, 0)

    # Getting the controls
    # You'll notice we multiplay the changing value by delta time, this is how you keep movements with the same ratio.
    key = pygame.key.get_pressed()
    
    player.handlePlayerMovement(key, movement_vector, dt)

    # Drawing the player to the screen
    # pygame.draw.circle(screen, "red", player_pos, 40)
    player.draw_player(screen)


    # Really am not sure what this does... I'll have to read on it
    pygame.display.flip()

    player.pos.x = max(0, min(player.pos.x, SCREEN_WIDTH - PLAYER_WIDTH))
    player.pos.y = max(0, min(player.pos.y, SCREEN_HEIGHT - PLAYER_HEIGHT))

    # Updating the screen every frame multiplied by delta time to keep ratio
    # The alternative to this is calling pygame.display.update() but this will shoot speeds through the roof due to fps

    # 60 ticks for 60 frames divided by 1000 (so we yield 60 frames per second)
    dt = clock.tick(60) / 1000 

# Quitting the pygame
pygame.quit()