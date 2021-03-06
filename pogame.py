# -*- coding: utf-8 -*-
import pygame
import random

from constants import *
from screen import create_screen, update_screen,bougerLeMechant
from world import create_world


def main():

    inventory = []

    # Création du "monde" tel que nous le définissons
    world = create_world()
    # Création des surfaces de dessin
    screen, background = create_screen(world)
    # Création d'une horloge
    clock = pygame.time.Clock()
    # Coordonnées [x, y] du joueur
    player = [0, 0]
    # initialisation de coordonnées aléatoires pour le mechant
    mechant_x = random.randint(0,WORLD_WIDTH-1)
    mechant_y = random.randint(0,WORLD_HEIGHT-1)
    mechant = [mechant_x,mechant_y]
    # Les variables qui nous permettent de savoir si notre programme est en cours d'exécution ou s'il doit se terminer.
    alive = True
    win = False
    running = True
    status = "start"
    # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
    update_screen(screen, background, world, player,mechant,status)
    clock.tick()

    # Boucle "quasi" infinie, qui s'arrêtera si le joueur est mort, ou si l'arrêt du programme est demandé.


    while running:
        # À chaque itération, on demande à pygame quels "évènements" se sont passés. Ces évènements sont l'interface
        # qui permet d'interragir avec l'extérieur du programme, et en particulier l'utilisateur (qui utilisera son
        # clavier, par exemple).


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # L'utilisateur souhaite fermer la fenêtre ou quitter par un autre moyen (menus ...).
                # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va se
                # terminer.
                running = False
            elif event.type == pygame.KEYDOWN:
                # Une touche du clavier a été pressée.
                if event.key == pygame.K_q:
                    # L'utilisateur a appuyé sur "Q", pour Quitter.
                    # À la prochaine itération de notre boucle principale, la condition sera fausse et le programme va
                    # se terminer.
                    running = False
                if event.key == pygame.K_SPACE:
                    status = "play"
                    continue # passer à la prochaine iteration
                if status=="play":
                    if event.key == pygame.K_UP:
                        if player[1] > 0:
                            player = (player[0], player[1] - 1)
                            mechant = bougerLeMechant(mechant)
                    elif event.key == pygame.K_DOWN:
                        if player[1] < WORLD_HEIGHT - 1 :
                            player = (player[0], player[1] + 1)
                            mechant = bougerLeMechant(mechant)                
                    elif event.key == pygame.K_LEFT:
                        if player[0] > 0:
                            player = (player[0] - 1, player[1])
                            mechant = bougerLeMechant(mechant)
                    elif event.key == pygame.K_RIGHT:
                        if player[0] < WORLD_WIDTH - 1:
                            player = (player[0] + 1, player[1])
                            mechant = bougerLeMechant(mechant)
                    elif event.key == pygame.K_i:
                        if  world[player[1]][player[0]]:
                                print(world[player[1]][player[0]][0],"trouvé")
                        else:
                            print("this is empty")
                    elif event.key == pygame.K_d:
                        if  inventory:
                            world[player[1]][player[0]]=inventory[0]
                            inventory.pop(0)
                        else:
                            print("inventory is empty")
                    elif event.key == pygame.K_p:
                        if  world[player[1]][player[0]]:
                            inventory.append(world[player[1]][player[0]])
                            world[player[1]][player[0]]=[]
                        else:
                            print("this is empty")
                    elif event.key == pygame.K_v:
                        if  inventory:
                                print(inventory)
                        else:
                            print("inventory is empty")

        
        # On vérifie si le joueur a gagné
        if inventory:
            s = 0
            for elt in inventory:
                s+=elt[0]
            if s>=100:
                win = True
                status = "gagné"
        # On vérifie si le joueur a perdu
        if mechant[0]==player[0] and mechant[1]==player[1]:
            alive=False
            status = "perdu"
        # On met à jour ce qu'on affiche sur l'écran, et on "pousse" l'aiguille de l'horloge d'un pas.
        update_screen(screen, background, world, player,mechant,status)
        clock.tick()
if __name__ == "__main__":
    try:
        main()
    finally:
        pygame.quit()