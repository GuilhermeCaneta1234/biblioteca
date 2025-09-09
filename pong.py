import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da janela
largura = 800
altura = 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("PONG Colorido")

# Cores
AZUL_ESCURO = (10, 10, 40)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
BRANCO = (255, 255, 255)

# Raquetes
raquete_largura = 10
raquete_altura = 100
raquete_vel = 6

jogador = pygame.Rect(10, altura // 2 - 50, raquete_largura, raquete_altura)
computador = pygame.Rect(largura - 20, altura // 2 - 50, raquete_largura, raquete_altura)

# Bola
bola = pygame.Rect(largura // 2, altura // 2, 15, 15)
bola_vel_x = 5
bola_vel_y = 5

# Pontuação
font = pygame.font.Font(None, 40)
pontos_jogador = 0
pontos_computador = 0

# Loop do jogo
clock = pygame.time.Clock()
rodando = True

while rodando:
    clock.tick(60)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and jogador.top > 0:
        jogador.y -= raquete_vel
    if teclas[pygame.K_s] and jogador.bottom < altura:
        jogador.y += raquete_vel

    # Movimento do computador (IA simples)
    if computador.centery < bola.centery:
        computador.y += raquete_vel
    if computador.centery > bola.centery:
        computador.y -= raquete_vel

    # Movimento da bola
    bola.x += bola_vel_x
    bola.y += bola_vel_y

    # Colisões com topo e base
    if bola.top <= 0 or bola.bottom >= altura:
        bola_vel_y *= -1

    # Colisão com raquetes
    if bola.colliderect(jogador) or bola.colliderect(computador):
        bola_vel_x *= -1

    # Pontuação
    if bola.left <= 0:
        pontos_computador += 1
        bola.center = (largura // 2, altura // 2)
        bola_vel_x *= -1

    if bola.right >= largura:
        pontos_jogador += 1
        bola.center = (largura // 2, altura // 2)
        bola_vel_x *= -1

    # Desenhar elementos
    tela.fill(AZUL_ESCURO)
    pygame.draw.rect(tela, VERDE, jogador)
    pygame.draw.rect(tela, VERDE, computador)
    pygame.draw.ellipse(tela, VERMELHO, bola)
    pygame.draw.aaline(tela, AMARELO, (largura // 2, 0), (largura // 2, altura))

    texto = font.render(f"{pontos_jogador}  :  {pontos_computador}", True, BRANCO)
    tela.blit(texto, (largura // 2 - texto.get_width() // 2, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()
