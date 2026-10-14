#importar librerias/modulos
import pygame
from pathlib import Path
import random

# definicion de variables
ancho = 750
alto = 700

pygame.init()
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Recoge las monedas")
reloj = pygame.time.Clock()

# cargar imagenes
carpeta_actual = Path(__file__).parent

imagen_personaje = pygame.image.load(carpeta_actual / "personaje.png").convert_alpha()
imagen_personaje = pygame.transform.smoothscale(imagen_personaje, (100, 100))
personaje = pygame.Rect(380, 230, 100, 100)

imagen_moneda = pygame.image.load(carpeta_actual / "moneda.png").convert_alpha()
imagen_moneda = pygame.transform.smoothscale(imagen_moneda, (30, 30))
moneda = pygame.Rect(200, 250, 30, 30)

velocidad = 15

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        personaje.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        personaje.x += velocidad
    if teclas[pygame.K_UP]:
        personaje.y -= velocidad
    if teclas[pygame.K_DOWN]:
        personaje.y += velocidad

    # evitar que salga de la pantalla
    personaje.x = max(0, min(ancho - personaje.width, personaje.x))
    personaje.y = max(0, min(alto - personaje.height, personaje.y))

    # detectar colision con la moneda
    if personaje.colliderect(moneda):
        moneda.x = random.randint(0, ancho - moneda.width)
        moneda.y = random.randint(0, alto - moneda.height)

    ventana.fill((30, 180, 50))
    ventana.blit(imagen_personaje, personaje)
    ventana.blit(imagen_moneda, moneda)
    pygame.display.flip()
    reloj.tick(30)

