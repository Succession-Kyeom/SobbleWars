import pygame
import sys
import os
import time
from fever import fevertime

def image_scaling(self):
    size = 8/3
    self = pygame.transform.scale(self, (int(self.get_width() * size), int(self.get_height() * size)))
    return self
def image_load():
    global image_background
    global image_buble
    global image_sound
    global image_buble_missile1
    global image_buble_missile2
    global image_sound_missile1
    global image_sound_missile2
    global image_lifescore
    global image_winLose
    global image_loseWin

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
    image_lifescore_path = os.path.join(script_dir, 'image', 'lifescore.png')
    image_winLose_path = os.path.join(script_dir, 'image', 'winlose.png')
    image_loseWin_path = os.path.join(script_dir, 'image', 'losewin.png')

    # 이미지 로드하기
    try:
        image_background = pygame.image.load(image_background_path)
        image_buble = pygame.image.load(image_buble_path)
        image_sound = pygame.image.load(image_sound_path)
        image_buble_missile1 = pygame.image.load(image_buble_missile1_path)
        image_buble_missile2 = pygame.image.load(image_buble_missile2_path)
        image_sound_missile1 = pygame.image.load(image_sound_missile1_path)
        image_sound_missile2 = pygame.image.load(image_sound_missile2_path)
        image_lifescore = pygame.image.load(image_lifescore_path)
        image_winLose = pygame.image.load(image_winLose_path)
        image_loseWin = pygame.image.load(image_loseWin_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit()
    image_background = image_scaling(image_background)
    image_buble = image_scaling(image_buble)
    image_sound = image_scaling(image_sound)
    image_buble_missile1 = image_scaling(image_buble_missile1)
    image_buble_missile2 = image_scaling(image_buble_missile2)
    image_sound_missile1 = image_scaling(image_sound_missile1)
    image_sound_missile2 = image_scaling(image_sound_missile2)
    image_lifescore = image_scaling(image_lifescore)
    image_winLose = image_scaling(image_winLose)
    image_loseWin = image_scaling(image_loseWin)

def sound_load():
    global sound_buble_explosion
    global sound_sound_explosion
    global sound_buble_creation
    global sound_sound_creation
    global win

    # 현재 스크립트 파일의 디렉토리 경로 얻기
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 상대 경로를 절대 경로로 변환하기
    sound_buble_explosion_path = os.path.join(script_dir,'sound', 'buble_explosion.wav')
    sound_sound_explosion_path = os.path.join(script_dir,'sound','sound_explosion.wav')
    sound_buble_creation_path = os.path.join(script_dir,'sound', 'buble_creation.wav')
    sound_sound_creation_path = os.path.join(script_dir,'sound','sound_creation.wav')
    winPath = os.path.join(script_dir, 'sound', '승리.wav')

    # 사운드 로드하기
    try:
        sound_buble_explosion = pygame.mixer.Sound(sound_buble_explosion_path)
        sound_sound_explosion = pygame.mixer.Sound(sound_sound_explosion_path)
        sound_sound_explosion = pygame.mixer.Sound(sound_sound_explosion_path)
        sound_buble_creation = pygame.mixer.Sound(sound_buble_creation_path)
        sound_sound_creation = pygame.mixer.Sound(sound_sound_creation_path)
        win = pygame.mixer.Sound(winPath)

    except FileNotFoundError as e:
        print(e)
        sys.exit()
def font_load():
    global font
    
    # 현재 스크립트 파일의 디렉토리 경로 얻기
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 상대 경로를 절대 경로로 변환하기
    font_path = os.path.join(script_dir, 'fonts', 'myfont.ttf')
    
    # 폰트 로드하기
    try:
        font = pygame.font.Font(font_path, 60)  # 폰트 크기를 30으로 설정
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
pygame.mixer.init()  # 사운드 초기화
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("pygame test")
clock = pygame.time.Clock()

# 이미지 로드하기
image_load()
sound_load()
font_load()

# 충돌 감지 함수
def check_collision(buble_missile_list, sound_missile_list):
    for b_missile in buble_missile_list[:]:
        for s_missile in sound_missile_list[:]:
            if b_missile.rect.colliderect(s_missile.rect):
                if b_missile.type == 'buble_missile1' and s_missile.type == 'sound_missile1':
                    buble_missile_list.remove(b_missile)
                    sound_buble_explosion.play()
                    sound_missile_list.remove(s_missile)
                    sound_sound_explosion.play()
                    break
                elif b_missile.type == 'buble_missile2' and s_missile.type == 'sound_missile1':
                    sound_missile_list.remove(s_missile)
                    sound_sound_explosion.play()
                    break
                elif b_missile.type == 'buble_missile2' and s_missile.type == 'sound_missile2':
                    buble_missile_list.remove(b_missile)
                    sound_buble_explosion.play()
                    sound_missile_list.remove(s_missile)
                    sound_sound_explosion.play()

                    break
                elif b_missile.type == 'buble_missile1' and s_missile.type == 'sound_missile2':
                    buble_missile_list.remove(b_missile) 
                    sound_buble_explosion.play()
                    break



def GameStart():
    global win

    # 초기 위치 설정
    x1, y1 = 0, 320
    x2, y2 = 1040, 320

    # 경기 타이머
    timer = time.time()
    time_script = ''

    # 라이프스코어 리스트 초기화
    lifescore_list1 = [image_lifescore, image_lifescore, image_lifescore, image_lifescore, image_lifescore]
    lifescore_count1 = 5
    lifescore_list2 = [image_lifescore, image_lifescore, image_lifescore, image_lifescore, image_lifescore]
    lifescore_count2 = 5

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
    # 메인 루프 시작하기
    running = True
    while lifescore_count1 and lifescore_count2 > 0:
        pygame.mixer.unpause()
        current_time = time.time()
        last = 30 - current_time + timer

        time_script = "{}".format((int)(last))
        text_surface = font.render(time_script, True, (0, 0, 0))  # 검은색 텍스트 렌더링

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
                if event.key == (pygame.K_a) and (current_time - last_buble_missile1_time) >= 0.7:
                    sound_buble_creation.play()
                    Missile_x = x1 + image_buble.get_width()
                    Missile_y = y1 + 45
                    buble_missile_list.append(Missile(Missile_x, Missile_y, 13, image_buble_missile1, 'buble_missile1'))
                    last_buble_missile1_time = current_time

                if event.key == pygame.K_d and (current_time - last_buble_missile2_time) >= 1.0:
                    sound_buble_creation.play()
                    Missile_x = x1 + image_buble.get_width()
                    Missile_y = y1 + 14
                    buble_missile_list.append(Missile(Missile_x, Missile_y, 13, image_buble_missile2, 'buble_missile2'))
                    last_buble_missile2_time = current_time

                if event.key == pygame.K_LEFT and (current_time - last_sound_missile1_time) >= 0.7:
                    sound_sound_creation.play()
                    Missile_x = x2
                    Missile_y = y2 + 45
                    sound_missile_list.append(Missile(Missile_x, Missile_y, -13, image_sound_missile1, 'sound_missile1'))
                    last_sound_missile1_time = current_time

                if event.key == pygame.K_RIGHT and (current_time - last_sound_missile2_time) >= 1.0:
                    sound_sound_creation.play()
                    Missile_x = x2
                    Missile_y = y2 + 14
                    sound_missile_list.append(Missile(Missile_x, Missile_y, -13, image_sound_missile2, 'sound_missile2'))
                    last_sound_missile2_time = current_time

        screen.fill((255, 255, 255))  # 배경색상 설정하기
        screen.blit(image_background, (0, 0))  # 배경 그리기
        screen.blit(text_surface, ((image_background.get_width() - text_surface.get_width())/2, 26))

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

        # 화면 밖으로 나간 미사일 제거 및 라이프 감소
        new_buble_missile_list = []
        for missile in buble_missile_list:
            if missile.x < 1280:
                new_buble_missile_list.append(missile)
            else:


                if (lifescore_count2 != 0)and(current_time - lifescore_time2 > 1.5):
                    lifescore_count2 -= 1
                    lifescore_list2.pop()
                    lifescore_time2 = current_time
                    invinsible_state2 = 1
                    invinsible_time2 = current_time
                    image_sound.set_alpha(168)


        new_sound_missile_list = []
        for missile in sound_missile_list:
            if missile.x > 0:
                new_sound_missile_list.append(missile)
            else:
                if (len(lifescore_list1) != 0)and(current_time - lifescore_time1 >= 1.6):
                    lifescore_count1 -= 1
                    lifescore_list1.pop()
                    lifescore_time1 = current_time
                    invinsible_state1 = 1
                    invinsible_time1 = current_time
                    image_buble.set_alpha(168)

        if invinsible_state1 == 1:
            if (invinsible_count1%2 == 0)and(current_time - invinsible_time1 >= 0.4):
                image_buble.set_alpha(255)
                invinsible_count1 += 1
                invinsible_time1 = current_time

                if (invinsible_count1%3 == 0):
                    invinsible_state1 = 0
                    invinsible_count1 = 0

            elif (invinsible_count1%2 == 1)and(current_time - invinsible_time1 >= 0.4):
                image_buble.set_alpha(168)
                invinsible_count1 += 1
                invinsible_time1 = current_time


        if invinsible_state2 == 1:

            if (invinsible_count2%2 == 0)and(current_time - invinsible_time2 >= 0.4):
                image_sound.set_alpha(255)
                invinsible_count2 += 1
                invinsible_time2 = current_time

                if (invinsible_count2%3 == 0):
                    invinsible_state2 = 0
                    invinsible_count2 = 0

            elif (invinsible_count2%2 == 1)and(current_time - invinsible_time2 >= 0.4):
                image_sound.set_alpha(168)
                invinsible_count2 += 1
                invinsible_time2 = current_time

        buble_missile_list = new_buble_missile_list
        sound_missile_list = new_sound_missile_list

        # 생명 이미지 그리기
        for i, _ in enumerate(lifescore_list1):
            screen.blit(image_lifescore, (26 + i * 80, 26))

        for i, _ in enumerate(lifescore_list2):
            screen.blit(image_lifescore, (1200 - i * 80, 26))  # y 좌표를 다르게 해서 겹치지 않게 설정

        if last <= 0:
            temp1, temp2 = lifescore_count1, lifescore_count2
            lifescore_count1, lifescore_count2, y1, y2 = fevertime(lifescore_count1, lifescore_count2, y1, y2)
            timer = time.time()
            for x in range(temp1 - lifescore_count1):
                lifescore_list1.pop()
            for x in range(temp2 - lifescore_count2):
                lifescore_count2

        pygame.display.update()  # 화면 업데이트하기
        clock.tick(60)  # 프레임 레이트 설정하기

    if lifescore_count1 == 0:
        pygame.mixer.pause()
        screen.blit(image_loseWin, (0, 0))
        win.play()
        pygame.display.update()
        time.sleep(6)
    elif lifescore_count2 == 0:
        pygame.mixer.pause()
        screen.blit(image_winLose, (0, 0))
        win.play()
        pygame.display.update()
        time.sleep(6)