import pygame
import sys
from datetime import datetime, timedelta

pygame.init()

BLANC = (255, 255, 255)
CIEL = (0, 255, 255)

largeur, hauteur = 400, 200
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Affichage de l'heure")

police = pygame.font.Font(None, 36)

def afficher_heure(heure):
    texte = police.render(f"{heure[0]:02d}:{heure[1]:02d}:{heure[2]:02d}", True, BLANC)
    fenetre.blit(texte, (largeur // 2 - texte.get_width() // 2, hauteur // 2 - texte.get_height() // 2))

def regler_heure(heure, minutes, secondes):
    return (heure % 24, minutes % 60, secondes % 60)

def regler_alarme(heure, minutes, secondes):
    return (heure % 24, minutes % 60, secondes % 60)

heure_actuelle = datetime.now().time()
heure_affichee = (heure_actuelle.hour, heure_actuelle.minute, heure_actuelle.second)

alarme = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_h:
                heure_affichee = regler_heure(heure_affichee[0] + 1, heure_affichee[1], heure_affichee[2])
            elif event.key == pygame.K_m:
                heure_affichee = regler_heure(heure_affichee[0], heure_affichee[1] + 1, heure_affichee[2])
            elif event.key == pygame.K_s:
                heure_affichee = regler_heure(heure_affichee[0], heure_affichee[1], heure_affichee[2] + 1)
            # Régler l'alarme avec les touches 'A'
            elif event.key == pygame.K_a:
                alarme = regler_alarme(heure_affichee[0], heure_affichee[1], heure_affichee[2])

    if alarme and heure_affichee == alarme:
        print("Réveil ! L'alarme a sonné.")
        alarme = None

    heure_actuelle = datetime.now().time()
    heure_affichee = (heure_actuelle.hour, heure_actuelle.minute, heure_actuelle.second)

    fenetre.fill(CIEL)
 
    afficher_heure(heure_affichee)

    pygame.display.flip()

    pygame.time.delay(1000)

pygame.quit()
sys.exit()
