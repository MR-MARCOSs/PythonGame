import pgzrun
import random

WIDTH = 1200
HEIGHT = 750
TITLE = "Meu Primeiro Jogo PGZero"

player = Actor("player", (4, 3))
player.speed = 5
alien = Actor("alien", (40, 30))
alien.speed = 2
coins = [Actor("coin", (random.randint(50, 750), random.randint(50, 550))) for _ in range(5)]
score = 0

def on_mouse_down(pos):
    print("Clique em:", pos)
    if alien.collidepoint(pos):
        print("Acertou o alien!")
        alien.pos = (random.randint(50, 750), random.randint(50, 550))

def on_mouse_move(pos):
    player.pos = pos

def update():
    global score
    if keyboard.left:
        player.x -= player.speed
    if keyboard.right:
        player.x += player.speed
    if keyboard.up:
        player.y -= player.speed
    if keyboard.down:
        player.y += player.speed

    player.x = max(0, min(WIDTH, player.x))
    player.y = max(0, min(HEIGHT, player.y))
    alien.x += alien.speed
    if alien.x > WIDTH or alien.x < 0:
        alien.speed *= -1 

    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 1
            coins.append(Actor("coin", (random.randint(50, 1200), random.randint(50, 750))))


def draw():
    screen.clear()
    player.draw()
    alien.draw()
    for coin in coins:
        coin.draw()
    screen.draw.text(f"Pontuação: {score}", (10, 10), color="white")

pgzrun.go()