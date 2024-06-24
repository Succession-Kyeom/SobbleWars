import pygame
import time
import sys

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

#이미지 로드
startImage = pygame.image.load("C:\\Users\\user\\PycharmProjects\\SobbleWars\\image\\게임시작.png")
endImage = pygame.image.load("C:\\Users\\user\\PycharmProjects\\SobbleWars\\image\\게임종료.png")

#초 당 설정
roop = True
clock = pygame.time.Clock()
#####

def Quit():
    pygame.quit()
    sys.exit()

#버튼 클래스
class Button:
    def __init__(self, image, x, y, width, height, action=None):
        mouse = pygame.mouse.get_pos()  # 마우스 좌표 mouse = [mouse_x, mouse_y]
        click = pygame.mouse.get_pressed()  # 마우스 클릭 확인 click = [left, wheel, right]

        if x <= mouse[0] <= x + width and y <= mouse[1] <= y + height: #마우스 좌표가 버튼 내부일 때
            screen.blit(image, (x, y)) #활성화 이미지로 변경
            if click[0] and action != None: #클릭 시
                time.sleep(1) #n초 지연
                action()
        else: #마우스 좌표가 버튼 외부일 때
            screen.blit(image, (x, y))

def MainMenu():
    while (True):
        startButton = Button(startImage, 500, 40, 100, 40, None)
        endButton = Button(endImage, 800, 40, 100, 40, None)

    return select

##메인 루프
while(roop):
    #프레임 설정
    clock.tick(60)

    #이벤트 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #이벤트 == 종료 일 경우
            roop = False #루프 탈출

    #스크린 채우기
    screen.fill(BLACK)

    startButton = Button(startImage, 500, 40, 100, 40, None)
    endButton = Button(endImage, 800, 40, 100, 40, Quit())

    #*중요* 화면 업데이트
    pygame.display.flip()

#종료
pygame.quit()