import pygame
import random

from constants import *



def create_screen(world):
    # Initialise screen
    pygame.init()
    board_width = WORLD_WIDTH * ROOM_SIZE
    board_height = WORLD_HEIGHT * ROOM_SIZE
    screen = pygame.display.set_mode((board_width, board_height))
    pygame.display.set_caption("SciencesPo Game")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    for x in range(WORLD_WIDTH):
        for y in range(WORLD_HEIGHT):
            if bool(x % 2) == bool(y % 2):

                color = (200, 200, 200)
            else:
                color = (250, 250, 250)

            pygame.draw.rect(
                background,
                color,
                [
                    x * ROOM_SIZE,
                    y * ROOM_SIZE,
                    ROOM_SIZE,
                    ROOM_SIZE,
                ],
            )

    return screen, background    
    


def update_screen(screen, background, world, player,mechant,status):
    board_width = WORLD_WIDTH * ROOM_SIZE
    board_height = WORLD_HEIGHT * ROOM_SIZE

    if status=="start":
        # Affichage du message d'acceuil
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('GET RICH OR DIE TRYING', True, (0,0,0),(255,255,255))
        textRect = text.get_rect()
        textRect.center = (board_width // 2, board_height // 2)
        screen.fill((255,255,255)) # obtenir un écran blanc
        screen.blit(text,textRect)
        # Affichage du boutton
        font = pygame.font.Font('freesansbold.ttf', 16)
        text_boutton = font.render('Tapez Espace pour commencer', True, (255,255,255),(0, 0, 128))
        bouttonRect = text_boutton.get_rect()
        bouttonRect.center = (board_width // 2, board_height // 2+20)
        screen.blit(text_boutton,bouttonRect)

    elif status=="play":
        player_x, player_y = player
        mechant_x,mechant_y = mechant
        screen.blit(background, (0, 0))

        # couleur (red, green, blue)
        bonhomme=pygame.image.load('bonhomme.png')
        screen.blit(
            bonhomme,
            (player_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2-5,
            player_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2-5)
        )
        """
        pygame.draw.rect(
            screen,
            (224, 64, 64),
            [
                player_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
                player_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2,
                PLAYER_SIZE,
                PLAYER_SIZE,
            ],
        )
        """
        img_mechant = pygame.image.load('mechant.png')
        screen.blit(
            img_mechant,
            (mechant_x * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2-5,
            mechant_y * ROOM_SIZE + (ROOM_SIZE - PLAYER_SIZE) / 2-5)
        )

        # TODO en théorie, il faudrait utiliser les éléments du monde pour afficher d'autres choses sur notre écran ...
        for y in range(len(world)):
            for x in range(len(world[y])):
                if world[y][x]:
                    pygame.draw.circle(
                        screen,
                        (204, 204, 0),
                        [
                            x * ROOM_SIZE + (ROOM_SIZE - OBJECT_SIZE) / 2+OBJECT_SIZE/2,
                            y * ROOM_SIZE + (ROOM_SIZE - OBJECT_SIZE) / 2+OBJECT_SIZE/2,
                        ],
                        radius=OBJECT_SIZE/2
                    )
    elif status=="gagné":
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Félicitations ! Tu es riche !', True, (0,0,0),(255,255,255))
        textRect = text.get_rect()
        textRect.center = (board_width // 2, board_height // 2)
        screen.fill((255,255,255))
        screen.blit(text,textRect)
    elif status=="perdu":
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Ton avidité a causé ta perte !', True, (0,0,0),(255,255,255))
        textRect = text.get_rect()
        textRect.center = (board_width // 2, board_height // 2)
        screen.fill((255,255,255))
        screen.blit(text,textRect)

    pygame.display.flip()

def bougerLeMechant(mechant):
    mechant_x,mechant_y = mechant
    # Mouvement aléatoire du mechant
    r = random.randint(-2,2)
    while mechant_x+r<0 or mechant_x+r>=WORLD_WIDTH:
        r = random.randint(-2,2)
    mechant_x = mechant_x+r
    r = random.randint(-2,2)
    while  mechant_y+r<0 or mechant_y+r>=WORLD_HEIGHT:
        r = random.randint(-2,2)
    mechant_y = mechant_y+r
    return [mechant_x,mechant_y]