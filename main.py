import pygame
import Player
import menu



def main():
    # Initializing the Pygame library
    pygame.init()

    # Screen Settings in PX
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    pygame.display.set_caption("2D Game Alpha")
    # Player Dimensions
    PLAYER_WIDTH = 100
    PLAYER_HEIGHT = 100

    player_speed = 5

    # Game tick rate pretty much
    clock = pygame.time.Clock()
    # Delta time, it allows game to run outside of 60 fps and so it doesn't break when you get more than 60. Its a whole thing if you wanna research it. Pygame does it easy
    dt = 0

    # Screen Object used for drawing onto the screen and what have you
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    # player position (there are other ways of doing this but this is how documentation references it to start (I am also learning pygame as we go (I know parenthesis in parenthesis (In parenthesis))))
    PLAYER_POS = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    PLAYER_SPRITE_IMAGE = pygame.image.load("./assets/boy_down_1.png")
    player_sprite = pygame.transform.scale(PLAYER_SPRITE_IMAGE, (100, 100))

    player = Player.Player(player_speed, player_sprite, PLAYER_POS)
    run = True

    # Game states
    game_is_paused = False

    while run:
        
    

    # Checking if player closes game or not and closing if true
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_is_paused = True
            if event.type == pygame.QUIT:
                run = False

    # Refreshes screen by filling it with a random color (not sure how this works for most games but this is how pygame does it for the most part)
        screen.fill((0,0,0))

        while game_is_paused == True:
            screen.fill((0, 0, 0))
            menu.draw_text(screen, "Game Is Paused", (screen.get_width() // 2), (screen.get_height() // 2))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_is_paused = False
            pygame.display.flip()
            

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

        player.pos.x = max(0, min(player.pos.x, screen.get_width() - PLAYER_WIDTH))
        player.pos.y = max(0, min(player.pos.y, screen.get_height() - PLAYER_HEIGHT))

        # Updating the screen every frame multiplied by delta time to keep ratio
        # The alternative to this is calling pygame.display.update() but this will shoot speeds through the roof due to game running faster on better machines

        # delta time runs tick every second
        dt = clock.tick(60) / 1000 

# Quitting the pygame
pygame.quit()

if __name__ == "__main__":
    main()