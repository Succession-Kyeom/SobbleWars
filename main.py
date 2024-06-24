import pygame
import sys

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
pygame.display.set_caption("소음을 부르는 달밤의 비눗방울 대전쟁")

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

#초 당 설정
roop = True
clock = pygame.time.Clock()
#####

#게임 시작
def GameStart():
    print("call game start")
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
        screen.fill(WHITE)

        pygame.display.update()

#게임 종료
def Quit():
    pygame.quit()
    sys.exit()

##메인 루프
while(roop):
    #프레임 설정
    clock.tick(60)

    #이벤트 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #이벤트 == 종료 일 경우
            roop = False #루프 탈출

    screen.fill(BLACK)
    startButton = Button(start[0], start[1], start[2], 540, 370, startSize[0], startSize[1], GameStart)
    aboutButton = Button(about[0], about[1], about[2], 540, 500, aboutSize[0], aboutSize[1], Quit)

    #*중요* 화면 업데이트
    pygame.display.update()
    pygame.display.flip()

#종료
Quit()