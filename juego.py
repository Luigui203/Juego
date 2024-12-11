import pygame
import sys
import random
import threading
from Controller.Usuario import Usuario

# Inicialización de Pygame
pygame.init()

# Configuración de pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Galaga con Jefes")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 122, 255)
ROJO = (255, 0, 0)
VIOLETA = (138, 43, 226)
NEON = (216, 191, 216)  # Color para el bordeado de neón

# Cargar imagen de fondo
fondo_menu = pygame.image.load("imagenes/menu.png")
fondo_menu = pygame.transform.scale(fondo_menu, (ANCHO, ALTO))

# Cargar imagen de controles
imagen_controles = pygame.image.load("imagenes/menu.png")
imagen_controles = pygame.transform.scale(imagen_controles, (ANCHO, ALTO))

# Fuente para el texto con estilo retro
fuente = pygame.font.Font(pygame.font.match_font('pressstart2p', False), 24)

# Fuente más grande para el título
titulo_fuente = pygame.font.Font(pygame.font.match_font('pressstart2p', False), 48)

# Función para dibujar texto en pantalla
def dibujar_texto(superficie, texto, x, y, color=BLANCO, fuente=fuente):
    texto_surface = fuente.render(texto, True, color)
    rect = texto_surface.get_rect(center=(x, y))
    superficie.blit(texto_surface, rect)

# Función para dibujar un botón con efecto de neón
def dibujar_boton_con_neon(superficie, rect, texto, color_boton, color_texto):
    # Dibujar el efecto de neón (bordes alrededor del botón)
    for grosor in range(8, 0, -2):  # Bordes decrecientes
        pygame.draw.rect(superficie, NEON, rect.inflate(grosor, grosor), width=1)
    # Dibujar el botón
    pygame.draw.rect(superficie, color_boton, rect)
    # Dibujar el texto
    dibujar_texto(superficie, texto, rect.centerx, rect.centery, color_texto)

# Función para el menú principal
def menu_principal():
    while True:
        # Dibujar imagen de fondo
        pantalla.blit(fondo_menu, (0, 0))

        # Dibujar el título
        dibujar_texto(pantalla, "Space Mania", ANCHO // 2, 100, BLANCO, titulo_fuente)

        # Definir los botones
        boton_play = pygame.Rect(ANCHO // 2 - 100, 200, 200, 50)
        boton_controles = pygame.Rect(ANCHO // 2 - 100, 300, 200, 50)
        boton_exit = pygame.Rect(ANCHO // 2 - 100, 400, 200, 50)

        # Dibujar botones con efecto de neón
        dibujar_boton_con_neon(pantalla, boton_play, "Play", VIOLETA, BLANCO)
        dibujar_boton_con_neon(pantalla, boton_controles, "Controles", VIOLETA, BLANCO)
        dibujar_boton_con_neon(pantalla, boton_exit, "Exit", VIOLETA, BLANCO)

        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_play.collidepoint(evento.pos):
                    return  # Salir del menú y comenzar el juego principal
                elif boton_controles.collidepoint(evento.pos):
                    mostrar_controles()
                elif boton_exit.collidepoint(evento.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()


# Fuente más pequeña y en negrita para los controles
texto_fuente = pygame.font.SysFont("Arial", 24, bold=True)

# Función para dibujar el texto con negrita
def dibujar_texto_negrita(surface, texto, x, y, color, fuente):
    texto_renderizado = fuente.render(texto, True, color)
    surface.blit(texto_renderizado, (x, y))

# Función para mostrar la pantalla de controles
def mostrar_controles():
    mostrando = True
    while mostrando:
        pantalla.fill(NEGRO)

        # Dibujar el título de la sección de controles alineado a la izquierda
        dibujar_texto_negrita(pantalla, "CONTROLES", 20, 50, AZUL, titulo_fuente)

        # Dibujar imagen de controles con el mismo tamaño de la ventana
        pantalla.blit(imagen_controles, (0, 0))  # Aquí no se escala, se coloca tal cual

        # Instrucciones de controles
        instrucciones = [
            ("Mover: Flecha derecha / Flecha izquierda", (20, 150)),
            ("Disparar: Barra espaciadora", (20, 175))
        ]
        
        # Organizar el texto de forma más clara, con mayor separación
        espacio = 50  # Espacio entre líneas
        for i, (texto, pos) in enumerate(instrucciones):
            # Colocar el texto con el índice (i) para separar mejor las instrucciones
            dibujar_texto_negrita(pantalla, texto, pos[0], pos[1] + i * espacio, BLANCO, texto_fuente)

        # Dibujar el botón para regresar más abajo
        boton_regresar = pygame.Rect(pantalla.get_width() // 2 - 100, 420, 200, 50)  # Ajuste en la posición vertical
        dibujar_boton_con_neon(pantalla, boton_regresar, "Regresar (Esc)", VIOLETA, BLANCO)

        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_regresar.collidepoint(evento.pos):
                    mostrando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    mostrando = False

        pygame.display.flip()



# Llamar al menú principal antes de iniciar el juego
menu_principal()


# Aquí comienza el juego principal, reemplaza con el código existente del juego
# Por ejemplo:
def juego_principal():
    print("Ejecutando juego principal...")

# Aseguramos que el nombre de usuario sea pasado correctamente
if len(sys.argv) > 1:
    nombreUsuario = sys.argv[1]  # Recibir el nombre de usuario desde los argumentos
else:
    nombreUsuario = None  # Si no se pasa el nombre de usuario, lo dejamos en None

# Imprime el nombre de usuario recibido (solo para comprobar que funciona)
print(f"Nombre de usuario recibido: {nombreUsuario}")

# Inicializamos Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Galaga con Jefes")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Cargar imágenes
jugador_img = pygame.image.load("imagenes\spaceship.png")
corazon_img = pygame.image.load("imagenes/corazon.png")  # Asegúrate de tener esta imagen
corazon_img = pygame.transform.scale(corazon_img, (30, 30))  # Ajustar tamaño
enemigo_img = pygame.image.load("imagenes\enemy.png")
bala_img = pygame.image.load("imagenes/bullet.png")
boss_img = pygame.image.load("imagenes/boss.png")
boss1_img = pygame.image.load("imagenes/boss1.png")
boss2_img= pygame.image.load("imagenes/dada.png")
bala_boss_img = pygame.image.load("imagenes/boss_bullet.png")



# Cargar sonidos
sonido_disparo = pygame.mixer.Sound("sonidos\disparo.wav")
sonido_impacto = pygame.mixer.Sound("sonidos\impacto.wav")
sonido_boss_disparo = pygame.mixer.Sound("sonidos/boss_disparo.wav")
sonido_game_over = pygame.mixer.Sound("sonidos\game_over.wav")
sonido_ambiente = pygame.mixer.Sound("sonidos\sonido_fondo.wav")

# Ajustar volumen de los sonidos
sonido_disparo.set_volume(0.2)  # Disparo a la mitad del volumen
sonido_impacto.set_volume(0.5)  # Impacto un poco más alto
sonido_boss_disparo.set_volume(0.2)  # Disparo del jefe más bajo
sonido_game_over.set_volume(0.8)  # Game over a volumen medio
sonido_ambiente.set_volume(0.6)  # Sonido ambiente mucho más bajo


# Clases del juego
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(jugador_img, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.bottom = ALTO - 10
        self.velocidad = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.rect.right < ANCHO:
            self.rect.x += self.velocidad

    def disparar(self):
        bala = Bala(self.rect.centerx, self.rect.top)
        todas_las_sprites.add(bala)
        balas.add(bala)
        sonido_disparo.play()  # Reproducir sonido de disparo

class Enemigo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(enemigo_img, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, ANCHO - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.velocidad_y = random.randint(1, 5)
        self.velocidad_x = random.choice([-1, 1]) * random.uniform(0.5, 2)

    def update(self):
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        # Rebotar en los bordes
        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.velocidad_x *= -1

        # Reiniciar si salen de la pantalla
        if self.rect.top > ALTO:
            self.rect.x = random.randint(0, ANCHO - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.velocidad_y = random.randint(1, 5)
            self.velocidad_x = random.choice([-1, 1]) * random.uniform(0.5, 2)

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bala_img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad_y = -10

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.bottom < 0:
            self.kill()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(boss_img, (200, 200))
        self.rect = self.image.get_rect()
        self.rect.centerx = ANCHO // 2
        self.rect.top = 10
        self.velocidad_x = 3
        self.vida = 30  # Ajustado a 30 impactos
        self.tiempo_disparo = random.randint(300, 700)  # Tiempo aleatorio entre 300 y 700 ms
        self.tiempo_ultimo_disparo = pygame.time.get_ticks()

    def update(self):
        self.rect.x += self.velocidad_x
        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.velocidad_x *= -1

        # Disparar de forma aleatoria
        if pygame.time.get_ticks() - self.tiempo_ultimo_disparo >= self.tiempo_disparo:
            self.disparar()
            self.tiempo_ultimo_disparo = pygame.time.get_ticks()
            self.tiempo_disparo = random.randint(300, 700)  # Cambiar el tiempo de disparo para el siguiente

    def disparar(self):
        for _ in range(4):
            x = random.randint(self.rect.left, self.rect.right)
            bala = BalaBoss(x, self.rect.bottom)
            todas_las_sprites.add(bala)
            balas_boss.add(bala)
            sonido_boss_disparo.play()

    def recibir_impacto(self):
        self.vida -= 1
        if self.vida <= 0:
            self.kill()  # Eliminar al jefe del juego

class BalaBoss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bala_boss_img, (15, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.velocidad_y = 5

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.top > ALTO:
            self.kill()

# Función para manejar enemigos
def actualizar_enemigos():
    while ejecutando:
        enemigos.update()
        pygame.time.delay(30)  # Controla la velocidad del hilo


# Función para mostrar mensaje de fin de juego
def mostrar_mensaje_fin(pantalla, texto, puntuacion):
    pantalla.fill(NEGRO)  # Limpiar la pantalla
    fuente = pygame.font.SysFont("Arial", 36)
    texto_surface = fuente.render(texto, True, BLANCO)
    rect = texto_surface.get_rect(center=(ANCHO // 2, ALTO // 2 - 40))  # Ajustar para que esté centrado
    pantalla.blit(texto_surface, rect)

    # Mostrar la puntuación final
    fuente_puntuacion = pygame.font.SysFont("Arial", 24)
    texto_puntuacion = fuente_puntuacion.render(f"Puntuación Final: {puntuacion}", True, BLANCO)
    rect_puntuacion = texto_puntuacion.get_rect(center=(ANCHO // 2, ALTO // 2 + 20))
    pantalla.blit(texto_puntuacion, rect_puntuacion)

    # Mostrar opciones para salir, reiniciar o regresar al menú
    fuente_opciones = pygame.font.SysFont("Arial", 24)
    texto_salir = fuente_opciones.render("Presiona 'Q' para salir o 'R' para reiniciar", True, BLANCO)
    pantalla.blit(texto_salir, (ANCHO // 2 - 200, ALTO // 2 + 60))

    # Mensaje adicional para regresar al menú
    texto_menu = fuente_opciones.render("Presiona 'ESC' para volver al Menú Principal", True, BLANCO)
    pantalla.blit(texto_menu, (ANCHO // 2 - 200, ALTO // 2 + 100))

    pygame.display.flip()  # Actualizar la pantalla



# Función para mostrar las vidas como corazones
def mostrar_vidas(pantalla, vidas):
    for i in range(vidas):
        x = 10 + i * 35  # Espaciado entre corazones
        pantalla.blit(corazon_img, (x, 40))


# Función para reiniciar el juego
def reiniciar_juego():
    global puntuacion, vidas, jefe_aparecido, puntos_para_jefe
    
    # Guardar el puntaje antes de reiniciar
    if nombreUsuario is not None:
        usuario = Usuario()
        usuario.guardarPuntaje(nombreUsuario, puntuacion)  # Guardar el puntaje solo si es mayor
    else:
        print("No se ha iniciado sesión correctamente.")
    
    # Reiniciar los estados del juego
    puntuacion = 0
    vidas = 3
    jefe_aparecido = False
    puntos_para_jefe = 20  # Resetear los puntos necesarios para el jefe a 20

    # Reiniciar al jugador
    jugador.rect.centerx = ANCHO // 2
    jugador.rect.bottom = ALTO - 10

    # Eliminar todos los sprites existentes
    todas_las_sprites.empty()
    enemigos.empty()
    balas.empty()
    balas_boss.empty()

    # Agregar el jugador de nuevo
    todas_las_sprites.add(jugador)

    # Regenerar enemigos iniciales
    for _ in range(8):  # Cambia este número según los enemigos iniciales deseados
        enemigo = Enemigo()
        todas_las_sprites.add(enemigo)
        enemigos.add(enemigo)


# Variables del juego
puntuacion = 0
vidas = 3
jefe_aparecido = False  # Variable para saber si el jefe ya apareció
puntos_para_jefe = 20  # Puntos necesarios para que aparezca el jefe
reloj = pygame.time.Clock()

# Inicializar la variable para controlar el sonido
sonido_game_over_reproducido = False

# Inicialización de grupos de sprites
todas_las_sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()
balas_boss = pygame.sprite.Group()

# Crear jugador
jugador = Jugador()
todas_las_sprites.add(jugador)

# Crear enemigos
for i in range(8):
    enemigo = Enemigo()
    todas_las_sprites.add(enemigo)
    enemigos.add(enemigo)

# Crear un hilo para manejar a los enemigos
ejecutando = True
hilo_enemigos = threading.Thread(target=actualizar_enemigos)
hilo_enemigos.start()

def cerrar_juego(puntaje,nombreUsuario):
    if nombreUsuario is not None:
        # Suponiendo que tienes una clase Usuario que puede guardar el puntaje
        usuario = Usuario()
        usuario.guardarPuntaje(nombreUsuario, puntaje)  # Guardar el puntaje con el nombre de usuario
    else:
        print("No se ha iniciado sesión correctamente.")
    
    # Finaliza el juego
    pygame.quit()
    sys.exit()

# Reproducir el sonido en bucle
sonido_ambiente.play(loops=-1, maxtime=0)  # loops=-1 hace que se repita indefinidamente

# Bucle principal
jugando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            cerrar_juego(puntuacion, nombreUsuario)

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and jugando:
                jugador.disparar()

    if jugando:
        # Comprobar si el jugador ha alcanzado los puntos necesarios para el jefe
        if puntuacion >= puntos_para_jefe and not jefe_aparecido:
            jefe = Boss()
            todas_las_sprites.add(jefe)
            jefe_aparecido = True

        # Actualización
        todas_las_sprites.update()

        # Colisiones entre enemigos y balas
        colisiones = pygame.sprite.groupcollide(enemigos, balas, True, True)
        for colision in colisiones:
            puntuacion += 1
            sonido_impacto.play()  # Reproducir sonido de impacto
            if not jefe_aparecido:  # Solo crear nuevos enemigos si el jefe no está presente
                enemigo = Enemigo()
                todas_las_sprites.add(enemigo)
                enemigos.add(enemigo)

        # Colisiones entre enemigos y jugador
        colisiones_jugador = pygame.sprite.spritecollide(jugador, enemigos, True)
        if colisiones_jugador:
            vidas -= 1
            if vidas <= 0:
                jugando = False
                mostrar_mensaje_fin(pantalla, "¡GAME OVER!", puntuacion)  # Llamar con la puntuación final

        # Colisiones entre balas del jefe y jugador
        colisiones_boss = pygame.sprite.spritecollide(jugador, balas_boss, True)
        if colisiones_boss:
            vidas -= 1
            if vidas <= 0:
                jugando = False
                mostrar_mensaje_fin(pantalla, "¡GAME OVER!", puntuacion)  # Llamar con la puntuación final

        # Colisiones entre balas y el jefe
        if jefe_aparecido:
            colisiones_jefe = pygame.sprite.spritecollide(jefe, balas, True)  # Eliminar las balas que impactan
            for colision in colisiones_jefe:
                jefe.recibir_impacto()  # Reducir vida del jefe

            # Verificar si el jefe fue destruido
            if not jefe.alive():
                jefe_aparecido = False  # El jefe ya no está
                puntuacion += 10  # Bonus por derrotar al jefe
                puntos_para_jefe *= 2  # Duplicar los puntos necesarios para el siguiente jefe
                # Regenerar enemigos tras derrotar al jefe
                for _ in range(8):  # Cambia este número según los enemigos iniciales deseados
                    enemigo = Enemigo()
                    todas_las_sprites.add(enemigo)
                    enemigos.add(enemigo)

        # Dibujar en pantalla
        pantalla.fill(NEGRO)
        todas_las_sprites.draw(pantalla)

        # Mostrar puntuación
        fuente = pygame.font.SysFont("Arial", 24)
        texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
        pantalla.blit(texto_puntuacion, (10, 10))

        # Mostrar vidas como corazones
        mostrar_vidas(pantalla, vidas)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de fotogramas
        reloj.tick(60)

    else:
        # Mostrar mensaje de game over con la puntuación final
        mostrar_mensaje_fin(pantalla, "¡GAME OVER!", puntuacion)
        # Reproducir sonido solo si no se ha reproducido antes
        if not sonido_game_over_reproducido:
            sonido_game_over.play()
            sonido_game_over_reproducido = True  # Marcar que el sonido ya se ha reproducido

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_q:  # Salir del juego
                    ejecutando = False
                    cerrar_juego(puntuacion, nombreUsuario)
                elif evento.key == pygame.K_r:  # Reiniciar el juego
                    reiniciar_juego()
                    jugando = True
                    puntuacion = 0  # Reiniciar puntuación
                    vidas = 3  # Reiniciar vidas
                    jefe_aparecido = False  # Reiniciar estado del jefe
                    sonido_game_over_reproducido = False  # Restablecer el estado para permitir que el sonido se reproduzca la próxima vez
                    todas_las_sprites.empty()  # Limpiar todos los sprites
                    enemigos.empty()  # Limpiar todos los enemigos
                    balas.empty()  # Limpiar todas las balas
                    jugador = Jugador()  # Crear un nuevo jugador
                    todas_las_sprites.add(jugador)
                    # Reagregar enemigos iniciales
                    for _ in range(8):
                        enemigo = Enemigo()
                        todas_las_sprites.add(enemigo)
                        enemigos.add(enemigo)
                elif evento.key == pygame.K_ESCAPE:  # Volver al menú principal
                     
                    menu_principal()
                    reiniciar_juego()  # Reinicia las variables del juego
                    jugando = True
                    sonido_game_over_reproducido = False
# Ejecutar el juego principal
juego_principal()





