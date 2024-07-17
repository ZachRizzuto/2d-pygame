import pygame
def handlePlayerMovement(key, movement_vector, player_speed, dt, player_pos):
    # Diagnol movement
    if key[pygame.K_a] and key[pygame.K_w]:
        movement_vector = pygame.math.Vector2(-player_speed * dt, -player_speed * dt)
    elif key[pygame.K_a] and key[pygame.K_s]:
        movement_vector = pygame.math.Vector2(-player_speed * dt, player_speed * dt)
    elif key[pygame.K_d] and key[pygame.K_w]:
        movement_vector = pygame.math.Vector2(player_speed * dt, -player_speed * dt)
    elif key[pygame.K_d] and key[pygame.K_s]:
        movement_vector = pygame.math.Vector2(player_speed * dt, player_speed * dt)
        
    # Left and Right
    elif key[pygame.K_a] == True:
        movement_vector = pygame.math.Vector2(-player_speed * dt, 0)
    elif key[pygame.K_d] == True:
        movement_vector = pygame.math.Vector2(player_speed * dt, 0)

    # Up and Down
    elif key[pygame.K_s] == True:
        movement_vector = pygame.math.Vector2(0, player_speed * dt)
    elif key[pygame.K_w] == True:
        movement_vector = pygame.math.Vector2(0, -player_speed * dt)

    
    player_pos += movement_vector.normalize() * player_speed if movement_vector.length() > 0 else movement_vector

    return player_pos