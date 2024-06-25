import pygame
import sys
import os
import time

from hellow import GameStart

def image_scaling(self):
    size = 8/3
    self = pygame.transform.scale(self, (int(self.get_width() * size), int(self.get_height() * size)))
    return self
def image_load():
    global image_feverbackground1
    global image_feverbuble
    global image_feversound
    global image_buble_missile1
    global image_buble_missile2
    global image_sound_missile1
    global image_sound_missile2
    global image_lifescore
    global image_timenumber
    global image_rainbow


    # 현재 스크립트 파일의 디렉토리 경로 얻기
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 상대 경로를 절대 경로로 변환하기
    image_feverbuble_path = os.path.join(script_dir, 'image', 'feverbuble.png')
    image_feversound_path = os.path.join(script_dir, 'image', 'feversound.png')
    image_feverbackground1_path = os.path.join(script_dir, 'image', 'feverbackground1.png')
    image_buble_missile1_path = os.path.join(script_dir, 'image', 'buble_missile1.png')
    image_buble_missile2_path = os.path.join(script_dir, 'image', 'buble_missile2.png')
    image_sound_missile1_path = os.path.join(script_dir, 'image', 'sound_missile1.png')
    image_sound_missile2_path = os.path.join(script_dir, 'image', 'sound_missile2.png')
    image_lifescore_path = os.path.join(script_dir, 'image', 'lifescore.png')

    image_timenumber = []
    for i in range(1, 11):
        image_timenumber_path = os.path.join(script_dir,'number',   "{}.png".format(i))
        try:
            image_timenumber.append(pygame.image.load(image_timenumber_path))
        # 이미지를 필요한 대로 사용하거나 저장하세요.
        except FileNotFoundError as e:
            print(e)
            sys.exit()
    image_rainbow = []
    for i in range(1, 11):
        image_rainbow_path = os.path.join(script_dir,'rainbow',   "r{}.png".format(i))
        try:
            image_rainbow.append(pygame.image.load(image_rainbow_path))
            size = 64/25
            image_rainbow[i - 1] = pygame.transform.scale(image_rainbow[i - 1], (int(image_rainbow[i - 1].get_width() * size), int(image_rainbow[i - 1].get_height() * size)))
        # 이미지를 필요한 대로 사용하거나 저장하세요.
        except FileNotFoundError as e:
            print(e)
            sys.exit()

    # 이미지 로드하기
    try:
        image_feverbackground1 = pygame.image.load(image_feverbackground1_path)
        image_feverbuble = pygame.image.load(image_feverbuble_path)
        image_feversound = pygame.image.load(image_feversound_path)
        image_buble_missile1 = pygame.image.load(image_buble_missile1_path)
        image_buble_missile2 = pygame.image.load(image_buble_missile2_path)
        image_sound_missile1 = pygame.image.load(image_sound_missile1_path)
        image_sound_missile2 = pygame.image.load(image_sound_missile2_path)
        image_lifescore = pygame.image.load(image_lifescore_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit()
    image_feverbackground1 = image_scaling(image_feverbackground1)
    image_feverbuble = image_scaling(image_feverbuble)
    image_feversound = image_scaling(image_feversound)
    image_buble_missile1 = image_scaling(image_buble_missile1)
    image_buble_missile2 = image_scaling(image_buble_missile2)
    image_sound_missile1 = image_scaling(image_sound_missile1)
    image_sound_missile2 = image_scaling(image_sound_missile2)
    image_lifescore = image_scaling(image_lifescore)


def initialize_timer(seconds):
    global start_ticks
    global countdown_time
    countdown_time = seconds
    start_ticks = pygame.time.get_ticks()


def sound_load():
    global sound_buble_explosion
    global sound_sound_explosion
    global sound_buble_creation
    global sound_sound_creation


    # 현재 스크립트 파일의 디렉토리 경로 얻기
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 상대 경로를 절대 경로로 변환하기
    sound_buble_explosion_path = os.path.join(script_dir,'sound', 'buble_explosion.wav')
    sound_sound_explosion_path = os.path.join(script_dir,'sound','sound_explosion.wav')
    sound_buble_creation_path = os.path.join(script_dir,'sound', 'buble_creation.wav')
    sound_sound_creation_path = os.path.join(script_dir,'sound','sound_creation.wav')

    # 사운드 로드하기
    try:
        sound_buble_explosion = pygame.mixer.Sound(sound_buble_explosion_path)
        sound_sound_explosion = pygame.mixer.Sound(sound_sound_explosion_path)
        sound_sound_explosion = pygame.mixer.Sound(sound_sound_explosion_path)
        sound_buble_creation = pygame.mixer.Sound(sound_buble_creation_path)
        sound_sound_creation = pygame.mixer.Sound(sound_sound_creation_path)

    except FileNotFoundError as e:
        print(e)
        sys.exit()

class Missile:
    def __init__(self, x, y, speed, image, missile_type, life, invinsible):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.type = missile_type
        self.life = life
        self.invinsible = invinsible
    def move(self):
        self.x += self.speed
        self.rect.x = self.x
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# 파이게임 초기화하기
pygame.init()
pygame.mixer.init()  # 사운드 초기화
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("pygame test")
clock = pygame.time.Clock()

# 이미지 로드하기
image_load()
sound_load()






def check_collision(buble_missile_list, sound_missile_list):
    buble_missiles_to_remove = []
    sound_missiles_to_remove = []
    next_missile1 = None
    next_next_missile1 = None
    for b_missile in buble_missile_list[:]:
        for s_missile in sound_missile_list[:]:
            if (b_missile.rect.colliderect(s_missile.rect))and(s_missile.invinsible == 0):
                if b_missile.type == 'buble_missile1' and s_missile.type == 'sound_missile1':
                    if b_missile not in buble_missiles_to_remove:
                        buble_missiles_to_remove.append(b_missile)
                    sound_buble_explosion.play()
                    if s_missile not in sound_missiles_to_remove:
                        sound_missiles_to_remove.append(s_missile)
                    sound_sound_explosion.play()
                    break
                elif b_missile.type == 'buble_missile2' and s_missile.type == 'sound_missile1':
                    if s_missile not in sound_missiles_to_remove:
                        sound_missiles_to_remove.append(s_missile)
                    sound_sound_explosion.play()
                    break
                elif b_missile.type == 'buble_missile2' and s_missile.type == 'sound_missile2':
                    if b_missile not in buble_missiles_to_remove:
                        buble_missiles_to_remove.append(b_missile)
                    sound_buble_explosion.play()

                    b_index = buble_missile_list.index(b_missile)
                    if b_index + 1 < len(buble_missile_list):
                        next_missile1 = buble_missile_list[b_index + 1]
                        next_missile1.y += 240
                        next_missile1.invinsible == 0
                        next_missile1.speed -= 8

                    if b_index + 2 < len(buble_missile_list):
                            next_next_missile1 = buble_missile_list[b_index + 2]
                            next_next_missile1.y -= 240
                            next_missile1.invinsible == 0
                            next_next_missile1.speed -= 8


                    s_missile.life -= 1
                    if (s_missile not in sound_missiles_to_remove)and(s_missile.life == 0):
                        sound_missiles_to_remove.append(s_missile)
                    sound_sound_explosion.play()
                    break
                elif b_missile.type == 'buble_missile1' and s_missile.type == 'sound_missile2':
                    if (b_missile not in buble_missiles_to_remove)and(b_missile.life == 1):
                        buble_missiles_to_remove.append(b_missile)
                    sound_buble_explosion.play()
                    break
                


    # 루프가 끝난 후 나중에 제거할 미사일을 실제로 제거
    for b_missile in buble_missiles_to_remove:
        if b_missile in buble_missile_list:
            buble_missile_list.remove(b_missile)

    for s_missile in sound_missiles_to_remove:
        if s_missile in sound_missile_list:
            sound_missile_list.remove(s_missile)

#경기 타이머
timer = time.time()

def fevertime(life1, life2, y0, y): #y0 는 y1 y는 y2
    Tick = 1
    initialize_timer(10)

    # 초기 위치 설정
    x1, y1 = 0, y0
    x2, y2 = 1040, y

    # 라이프스코어 리스트 초기화
    lifescore_list1 = [image_lifescore, image_lifescore, image_lifescore, image_lifescore, image_lifescore]
    lifescore_count1 = life1
    lifescore_list2 = [image_lifescore, image_lifescore, image_lifescore, image_lifescore, image_lifescore]
    lifescore_count2 = life2

    # 미사일 리스트 초기화
    buble_missile_list = []
    sound_missile_list = []

    last_buble_missile1_time = 0
    last_buble_missile2_time = 0
    last_sound_missile1_time = 0
    last_sound_missile2_time = 0

    # 라이프 시간용 변수
    lifescore_time1 = 0
    lifescore_time2 = 0

    # 무적 상태 변수
    invinsible_state1 = 0
    invinsible_state2 = 0

    # 무적 상태 시간
    invinsible_time1 = 0
    invinsible_time2 = 0

    # 무적 상태 flip flop counter
    invinsible_count1 = 0
    invinsible_count2 = 0

    timer = time.time()



    # 메인 루프 시작하기
    running = True
    while running:

        current_time = time.time()

        i = (int)(10 - current_time + timer)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and y1 > 80:
                    y1 -= 240 # w를 누르면 위로 이동

                elif event.key == pygame.K_s and y1 < 560:
                    y1 += 240  # s를 누르면 아래로 이동
                if event.key == pygame.K_UP and y2 > 80:
                    y2 -= 240  # UP 키를 누르면 위로 이동
                elif event.key == pygame.K_DOWN and y2 < 560:
                    y2 += 240  # DOWN 키를 누르면 아래로 이동
                if event.key == (pygame.K_a) and (current_time - last_buble_missile1_time) >= 0.3:
                    sound_buble_creation.play()
                    Missile_x = x1 + image_feverbuble.get_width()
                    Missile_y = y1 + 45
                    buble_missile_list.append(Missile(Missile_x, Missile_y, 18, image_buble_missile1, 'buble_missile1', 1, 0))
                    last_buble_missile1_time = current_time

                if event.key == pygame.K_d and (current_time - last_buble_missile2_time) >= 0.5:
                    sound_buble_creation.play()
                    Missile_x = x1 + image_feverbuble.get_width()
                    Missile_y = y1 + 14
                    buble_missile_list.append(Missile(Missile_x, Missile_y, 18, image_buble_missile2, 'buble_missile2', 1, 0))
                    Missile_x = x1 + image_feverbuble.get_width() - 10
                    Missile_y = y1 + 45
                    buble_missile_list.append(Missile(Missile_x, Missile_y, 18, image_buble_missile1, 'buble_missile1',2, 1))
                    Missile_x = x1 + image_feverbuble.get_width() - 8
                    Missile_y = y1 + 45
                    buble_missile_list.append(Missile(Missile_x, Missile_y, 18, image_buble_missile1, 'buble_missile1', 2, 1))
                    last_buble_missile2_time = current_time

                if event.key == pygame.K_LEFT and (current_time - last_sound_missile1_time) >= 0.5:
                    sound_sound_creation.play()
                    Missile_x = x2
                    Missile_y = y2 + 45
                    sound_missile_list.append(Missile(Missile_x, Missile_y, -18, image_sound_missile1, 'sound_missile1', 1, 0))
                    sound_sound_creation.play()
                    last_sound_missile1_time = current_time

                if event.key == pygame.K_RIGHT and (current_time - last_sound_missile2_time) >= 0.8:
                    sound_sound_creation.play()
                    Missile_x = x2
                    Missile_y = y2 + 14
                    sound_missile_list.append(Missile(Missile_x, Missile_y, -10, image_sound_missile2, 'sound_missile2', 2, 0))
                    last_sound_missile2_time = current_time

        screen.fill((255, 255, 255))  # 배경색상 설정하기
        screen.blit(image_rainbow[((int)(Tick/5))%10], (0, 0))
        if Tick == 45:
            Tick = 0
        screen.blit(image_feverbackground1, (0, 0))  # 배경 그리기
        screen.blit(image_timenumber[i - 1], ((image_feverbackground1.get_width() - image_timenumber[i - 1].get_width())/2, 26))

        screen.blit(image_feverbuble, (x1, y1))  # 이미지를 새로운 위치에 그리기
        screen.blit(image_feversound, (x2, y2))  # 다른 이미지를 새로운 위치에 그리기

        # 미사일 그리기 및 이동
        for missile in buble_missile_list:
            missile.move()
            missile.draw(screen)

        for missile in sound_missile_list:
            missile.move()
            missile.draw(screen)

        # 충돌 감지 및 제거
        check_collision(buble_missile_list, sound_missile_list)

        # 화면 밖으로 나간 미사일 제거 및 라이프 감소
        new_buble_missile_list = []
        for missile in buble_missile_list:
            if missile.x < 1280:
                new_buble_missile_list.append(missile)
            else:
                lifescore_count2 -= 1
                if (len(lifescore_list2) != 0)and(current_time - lifescore_time2 > 1.5):
                    lifescore_list2.pop()
                    lifescore_time2 = current_time
                    invinsible_state2 = 1
                    invinsible_time2 = current_time
                    image_feversound.set_alpha(168)


        new_sound_missile_list = []
        for missile in sound_missile_list:
            if missile.x > 0:
                new_sound_missile_list.append(missile)
            else:
                lifescore_count1 -= 1
                if (len(lifescore_list1) != 0)and(current_time - lifescore_time1 >= 1.6):
                    lifescore_list1.pop()
                    lifescore_time1 = current_time
                    invinsible_state1 = 1
                    invinsible_time1 = current_time
                    image_feverbuble.set_alpha(168)

        if invinsible_state1 == 1:

            if (invinsible_count1%2 == 0)and(current_time - invinsible_time1 >= 0.4):
                image_feverbuble.set_alpha(255)
                invinsible_count1 += 1
                invinsible_time1 = current_time

                if (invinsible_count1%3 == 0):
                    invinsible_state1 = 0
                    invinsible_count1 = 0

            elif (invinsible_count1%2 == 1)and(current_time - invinsible_time1 >= 0.4):
                image_feverbuble.set_alpha(168)
                invinsible_count1 += 1
                invinsible_time1 = current_time


        if invinsible_state2 == 1:

            if (invinsible_count2%2 == 0)and(current_time - invinsible_time2 >= 0.4):
                image_feversound.set_alpha(255)
                invinsible_count2 += 1
                invinsible_time2 = current_time

                if (invinsible_count2%3 == 0):
                    invinsible_state2 = 0
                    invinsible_count2 = 0

            elif (invinsible_count2%2 == 1)and(current_time - invinsible_time2 >= 0.4):
                image_feversound.set_alpha(168)
                invinsible_count2 += 1
                invinsible_time2 = current_time

        buble_missile_list = new_buble_missile_list
        sound_missile_list = new_sound_missile_list

        # 생명 이미지 그리기
        for i, _ in enumerate(lifescore_list1):
            screen.blit(image_lifescore, (26 + i * 80, 26))

        for i, _ in enumerate(lifescore_list2):
            screen.blit(image_lifescore, (1200 - i * 80, 26))  # y 좌표를 다르게 해서 겹치지 않게 설정



        pygame.display.update()  # 화면 업데이트하기
        clock.tick(60)  # 프레임 레이트 설정하기    
        Tick += 1

        if i < 0:
            running = False

