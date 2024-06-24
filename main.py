import pygame

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
size = (1920, 1080)
screen = pygame.display.set_mode(size)

#스크린 이름 설정
pygame.display.set_caption("소음을 부르는 달밤의 비눗방울 대전쟁")

#초 당 설정
roop = True
clock = pygame.time.Clock()
#####

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

    #*중요* 화면 업데이트
    pygame.display.flip()

#종료
pygame.quit()