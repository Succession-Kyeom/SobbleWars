import pygame
import sys
import os

def image_load():
    global image_background
    global image_buble
    global image_sound
    global image_buble_missile1
    global image_buble_missile2
    global image_sound_missile1
    global image_sound_missile2

    # 현재 스크립트 파일의 디렉토리 경로 얻기
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 상대 경로를 절대 경로로 변환하기
    image_buble_path = os.path.join(script_dir, 'image', 'buble.png')
    image_sound_path = os.path.join(script_dir, 'image', 'sound.png')
    image_background_path = os.path.join(script_dir, 'image', 'background.png')
    image_buble_missile1_path = os.path.join(script_dir, 'image', 'buble_missile1.png')
    image_buble_missile2_path = os.path.join(script_dir, 'image', 'buble_missile2.png')
    image_sound_missile1_path = os.path.join(script_dir, 'image', 'sound_missile1.png')
    image_sound_missile2_path = os.path.join(script_dir, 'image', 'sound_missile2.png')

    # 이미지 로드하기
    try:
        image_background = pygame.image.load(image_background_path)
        image_buble = pygame.image.load(image_buble_path)
        image_sound = pygame.image.load(image_sound_path)
        image_buble_missile1 = pygame.image.load(image_buble_missile1_path)
        image_buble_missile2 = pygame.image.load(image_buble_missile2_path)
        image_sound_missile1 = pygame.image.load(image_sound_missile1_path)
        image_sound_missile2 = pygame.image.load(image_sound_missile2_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit()

def sound_load():
    global sound_buble_explosion
    global sound_background
    #global sound_sound_explosion

    # 현재 스크립트 파일의 디렉토리 경로 얻기
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 상대 경로를 절대 경로로 변환하기
    sound_buble_explosion_path = os.path.join(script_dir,'sound', 'buble_explosion.wav')
    #sound_sound_explosion_path = os.path.join(script_dir,'sound','sound_explosion.mp3')

    # 사운드 로드하기
    try:
        sound_buble_explosion = pygame.mixer.Sound(sound_buble_explosion_path)
        #sound_sound_explosion = pygame.mixer.Sound(sound_sound_explosion_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit()

class Missile:
    def __init__(self, x, y, speed, image, missile_type):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.type = missile_type
    
    def move(self):
        self.x += self.speed
        self.rect.x = self.x
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# 파이게임 초기화하기
pygame.init()
screen = pygame.display.set_mode((480, 270))
pygame.display.set_caption("pygame test")
clock = pygame.time.Clock()

# 이미지 로드하기
image_load()
sound_load()

# 초기 위치 설정
x1, y1 = 0, 120
x2, y2 = 390, 120

# 미사일 리스트 초기화
buble_missile_list = []
sound_missile_list = []

# 충돌 감지 함수
def check_collision(buble_missile_list, sound_missile_list):
    for b_missile in buble_missile_list[:]:
        for s_missile in sound_missile_list[:]:
            if b_missile.rect.colliderect(s_missile.rect):
                if b_missile.type == 'buble_missile1' and s_missile.type == 'sound_missile1':
                    buble_missile_list.remove(b_missile)
                    sound_buble_explosion.play()
                    sound_missile_list.remove(s_missile)
                    break
                elif b_missile.type == 'buble_missile2' and s_missile.type == 'sound_missile1':
                    sound_missile_list.remove(s_missile)
                    break
                elif b_missile.type == 'buble_missile2' and s_missile.type == 'sound_missile2':
                    buble_missile_list.remove(b_missile)
                    sound_buble_explosion.play()
                    sound_missile_list.remove(s_missile)
                    break
                elif b_missile.type == 'buble_missile1' and s_missile.type == 'sound_missile2':
                    buble_missile_list.remove(b_missile) 
                    sound_buble_explosion.play()
                    break

# 메인 루프 시작하기
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and y1 > 40:
                y1 -= 80  # w를 누르면 위로 이동
            elif event.key == pygame.K_s and y1 < 180:
                y1 += 80  # s를 누르면 아래로 이동
            if event.key == pygame.K_UP and y2 > 40:
                y2 -= 80  # UP 키를 누르면 위로 이동
            elif event.key == pygame.K_DOWN and y2 < 180:
                y2 += 80  # DOWN 키를 누르면 아래로 이동
            if event.key == pygame.K_a:
                Missile_x = x1 + image_buble.get_width()
                Missile_y = y1 + 17
                buble_missile_list.append(Missile(Missile_x, Missile_y, 5, image_buble_missile1, 'buble_missile1'))
            if event.key == pygame.K_d:
                Missile_x = x1 + image_buble.get_width()
                Missile_y = y1 + 7
                buble_missile_list.append(Missile(Missile_x, Missile_y, 5, image_buble_missile2, 'buble_missile2'))
            if event.key == pygame.K_LEFT:
                Missile_x = x2
                Missile_y = y2 + 17
                sound_missile_list.append(Missile(Missile_x, Missile_y, -5, image_sound_missile1, 'sound_missile1'))
            if event.key == pygame.K_RIGHT:
                Missile_x = x2
                Missile_y = y2 + 7
                sound_missile_list.append(Missile(Missile_x, Missile_y, -5, image_sound_missile2, 'sound_missile2'))

    screen.fill((255, 255, 255))  # 배경색상 설정하기
    screen.blit(image_background, (0, 0))  # 배경 그리기
    screen.blit(image_buble, (x1, y1))  # 이미지를 새로운 위치에 그리기
    screen.blit(image_sound, (x2, y2))  # 다른 이미지를 새로운 위치에 그리기

    # 미사일 그리기 및 이동
    for missile in buble_missile_list:
        missile.move()
        missile.draw(screen)
    
    for missile in sound_missile_list:
        missile.move()
        missile.draw(screen)
    
    # 충돌 감지 및 제거
    check_collision(buble_missile_list, sound_missile_list)

    # 화면 밖으로 나간 미사일 제거
    buble_missile_list = [missile for missile in buble_missile_list if missile.x < 480]
    sound_missile_list = [missile for missile in sound_missile_list if missile.x > 0]

    pygame.display.update()  # 화면 업데이트하기
    clock.tick(60)  # 프레임 레이트 설정하기

pygame.quit()
sys.exit()
