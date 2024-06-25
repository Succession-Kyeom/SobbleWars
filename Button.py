import pygame
import time

#화면 사이즈 설정
size = (1280, 720)
screen = pygame.display.set_mode(size)

#버튼 클래스
class Button:
    def __init__(self, image, imageOn, imageClick, x, y, width, height, state, result=0, action=None):
        mouse = pygame.mouse.get_pos()  # 마우스 좌표 mouse = [mouse_x, mouse_y]
        click = pygame.mouse.get_pressed()  # 마우스 클릭 확인 click = [left, wheel, right]
        act = False

        screen.blit(image, (x, y))
        if x <= mouse[0] <= (x + width) and y <= mouse[1] <= (y + height): #마우스 좌표가 버튼 내부일 때
            screen.blit(imageOn, (x, y)) #활성화 이미지로 변경
            if click[0] and action != None:
                act = True
                screen.blit(imageClick, (x, y))
                result = action()
            if result != 0:
                state = 2
        else: #마우스 좌표가 버튼 외부일 때
            screen.blit(image, (x, y))