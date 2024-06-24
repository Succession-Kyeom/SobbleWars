import pygame
import time
import sys

from hellow import GameStart
from Button import Button

##pygame 초기화
pygame.init()

##변수 초기화 및 설정
#색상 설정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#화면 사이즈 설정
size = (1280, 720)
screen = pygame.display.set_mode(size)

#스크린 이름 설정
pygame.display.set_caption("소음을 부르는 광기의 비눗방울 대전쟁")

#이미지 로드 및 크기 설정

startImage = pygame.image.load("C:image\\start_btn.png")
startImageOn = pygame.image.load("C:image\\start_onmouse.png")
startImageClick = pygame.image.load("C:image\\start_clicked.png")
start = (startImage, startImageOn, startImageClick)
startSize = start[0].get_size()

aboutImage = pygame.image.load("C:image\\about_btn.png")
aboutImageOn = pygame.image.load("C:image\\about_onmouse.png")
aboutImageClick = pygame.image.load("C:image\\about_clicked.png")
about = (aboutImage, aboutImageOn, aboutImageClick)
aboutSize = about[0].get_size()

story1 = pygame.image.load("C:image\\story1.png")
story1 = pygame.transform.scale(story1, (1280, 720))

story2 = pygame.image.load("C:image\\story2.png")
story2 = pygame.transform.scale(story2, (1280, 720))

story3 = pygame.image.load("C:image\\story3.png")
story3 = pygame.transform.scale(story3, (1280, 720))

story4 = pygame.image.load("C:image\\story4.png")
story4 = pygame.transform.scale(story4, (1280, 720))

story = [story1, story2, story3, story4]

#초 당 설정
roop = True
clock = pygame.time.Clock()

state = 0
index = 0
#####

#게임 종료
def Quit():
    pygame.quit()
    sys.exit()

def HowToPlay():
    while(True):
        pygame.display.update()
############

##메인 루프
while(roop):
    alpha = 0
    clock.tick(60)
    #이벤트 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #이벤트 == 종료 일 경우
            roop = False #루프 탈출
        if event.type == pygame.KEYDOWN and state == 0:
            for alpha in range(255, -1, -10):
                story[index].set_alpha(alpha)
                time.sleep(0.01)

            index += 1
            if index == 4:
                state = 1

    screen.fill(BLACK)
    if state == 0:
        screen.blit(story[index], (0, 0))
    elif state == 1:
        startButton = Button(start[0], start[1], start[2], 1070, 570, startSize[0], startSize[1], GameStart)
        aboutButton = Button(about[0], about[1], about[2], 1070, 630, aboutSize[0], aboutSize[1], HowToPlay)

    #*중요* 화면 업데이트
    pygame.display.update()
    pygame.display.flip()

#종료
Quit()