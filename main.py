import pygame
import Player
import menu
import Button
import math

class main():
    # Game states
    run = True
    game_is_paused = False
    def set_game_is_paused(self, bool):
            self.game_is_paused = bool

    def main(self):

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

        # menu button

        start_button = Button.Button("Click To Resume", self.set_game_is_paused, False, font_size=30, scale=1, font_color=(0, 0, 255))
        start_button.img = start_button.img.convert_alpha()
        # temp background so black isn't as boring

        background_image = pygame.transform.scale(pygame.image.load("./assets/Grass.png"), (32*3.13, 32*3.13))
        # Draws background image calculated with screen dimensions
        def draw_background(screen: pygame.SurfaceType, image: pygame.SurfaceType):
            screen_width = screen.get_width()
            screen_height = screen.get_height()
            
            image_width, image_height = image.get_size()

            tilesX = math.ceil(screen_width / image_width)
            tilesY = math.ceil(screen_height / image_height)

            for x in range(tilesX):
                for y in range(tilesY):
                    screen.blit(image, (x*image_width, y*image_height))
        # draws pause background when game is paused
        def draw_pause_background(screen: pygame.SurfaceType):
            pause_background = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
            pygame.draw.rect(pause_background, (125, 125, 125, 100), [0,0, screen.get_width(), screen.get_width()])
            
            
            start_button.draw_button(pause_background, 0, 0, True)
            
            screen.blit(pause_background, (0,0))




        while self.run:


        # Checking if player closes game or not and closing if true
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if(self.game_is_paused):
                            self.set_game_is_paused(False)
                        else:
                            self.set_game_is_paused(True)
                    if event.key == pygame.K_LSHIFT:
                        player.speed += 2
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT:
                        player.speed -= 2
                if event.type == pygame.QUIT:
                    self.run = False

        # Refreshes screen by filling it with a random color (not sure how this works for most games but this is how pygame does it for the most part)
            screen.fill((0,0,0))

            movement_vector = pygame.math.Vector2(0, 0)

            # Getting the controls
            # You'll notice we multiplay the changing value by delta time, this is how you keep movements with the same ratio.
            key = pygame.key.get_pressed()
            
            if not self.game_is_paused:
                player.handlePlayerMovement(key, movement_vector, dt)
                
            
            # Drawing background player will be on
            draw_background(screen, background_image)

            # Drawing the player to the screen
            player.draw_player(screen)

            # this is here because cascading, it allows it to be drawn on top
            if self.game_is_paused:
                draw_pause_background(screen)

            # Really am not sure what this does... I'll have to read on it
            pygame.display.flip()

            player.pos.x = max(0, min(player.pos.x, screen.get_width() - PLAYER_WIDTH))
            player.pos.y = max(0, min(player.pos.y, screen.get_height() - PLAYER_HEIGHT))

            # Updating the screen every frame multiplied by delta time to keep ratio
            # The alternative to this is calling pygame.display.update() but this will shoot speeds through the roof due to game running faster on better machines

            # delta time runs tick every second
            dt = clock.tick(60) / 1000 

main = main()
# Quitting the pygame
pygame.quit()

if __name__ == "__main__":
    main.main()