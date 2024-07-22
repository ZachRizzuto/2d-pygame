import pygame
class Player:
    direction = "down"
    spriteCounter = 0
    spriteNum = 1

    def __init__(self, speed, sprite, pos):
        self.speed = speed
        self.sprite = sprite
        self.pos = pos

    def draw_player(self, screen):
        self.get_player_sprite()
        screen.blit(self.sprite, self.pos)
        

    def get_player_sprite(self):
        match self.direction:
            case "up":
                player_sprite = pygame.transform.scale(pygame.image.load(f"./assets/boy_up_{self.spriteNum}.png"), (100, 100))
            case "down":
                player_sprite = pygame.transform.scale(pygame.image.load(f"./assets/boy_down_{self.spriteNum}.png"), (100, 100))
            case "left":
                player_sprite = pygame.transform.scale(pygame.image.load(f"./assets/boy_left_{self.spriteNum}.png"), (100, 100))
            case "right":
                player_sprite = pygame.transform.scale(pygame.image.load(f"./assets/boy_right_{self.spriteNum}.png"), (100, 100))
            case _:
                player_sprite = pygame.transform.scale(pygame.image.load(f"./assets/boy_down_{self.spriteNum}.png"), (100, 100))
        self.sprite = player_sprite

    def handlePlayerMovement(self, key, movement_vector, dt):
    
    # Diagnol movement
        if key[pygame.K_a] and key[pygame.K_w]:
            movement_vector = pygame.math.Vector2(-self.speed * dt, -self.speed * dt)
        elif key[pygame.K_a] and key[pygame.K_s]:
            movement_vector = pygame.math.Vector2(-self.speed * dt, self.speed * dt)
        elif key[pygame.K_d] and key[pygame.K_w]:
            movement_vector = pygame.math.Vector2(self.speed * dt, -self.speed * dt)
        elif key[pygame.K_d] and key[pygame.K_s]:
            movement_vector = pygame.math.Vector2(self.speed * dt, self.speed * dt)
            
        # Left and Right
        elif key[pygame.K_a] == True:
            self.direction = "left"
            movement_vector = pygame.math.Vector2(-self.speed * dt, 0)
        elif key[pygame.K_d] == True:
            self.direction = "right"
            movement_vector = pygame.math.Vector2(self.speed * dt, 0)

        # Up and Down
        elif key[pygame.K_s] == True:
            self.direction = "down"
            movement_vector = pygame.math.Vector2(0, self.speed * dt)
        elif key[pygame.K_w] == True:
            self.direction = "up"
            movement_vector = pygame.math.Vector2(0, -self.speed * dt)

        if key[pygame.K_w] or key[pygame.K_a] or key[pygame.K_s] or key[pygame.K_d]:
            self.spriteCounter += 1
            if self.spriteCounter > 20:
                self.spriteCounter = 0
                if self.spriteNum == 1:
                    self.spriteNum = 2
                elif self.spriteNum == 2:
                    self.spriteNum = 1

        
        self.pos += movement_vector.normalize() * self.speed if movement_vector.length() > 0 else movement_vector

        
        