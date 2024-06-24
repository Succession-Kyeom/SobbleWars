import pygame
import sys  # sys 모듈 임포트하기

# 이미지 로드하기
image_buble = pygame.image.load('C:image//buble.png')
image_sound = pygame.image.load('C:image//sound.png')

image = pygame.transform.scale(image, (int(ext[0] * size), int(ext[1] * size)))


# 파이게임 초기화하기
pygame.init()
screen = pygame.display.set_mode((480, 270))
# 제목 표시줄 설정하기
pygame.display.set_caption("pygame test")
# 프레임 매니저 초기화하기
clock = pygame.time.Clock()

# 초기 위치 설정
x1 = 0
x2 = 420
y1 = 90
y2 = 90

# 배경색상 설정하기
screen.fill((255, 255, 255))

# 화면 업데이트하기
pygame.display.update()

# 메인 루프 시작하기
running = True
while running:
    # 이벤트 확인하기
    for event in pygame.event.get():
        # 닫기 버튼을 눌렀는지 확인하기
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_w)and (y1 != 0):
                y1 -= 90  # w를 누르면 위로 이동
            elif (event.key == pygame.K_s)and(y1 != 180):
                y1 += 90  # s를 누르면 아래로 이동
            if event.key == (pygame.K_UP)and(y2 != 0):
                y2 -= 90  # w를 누르면 위로 이동
            elif (event.key == pygame.K_DOWN)and(y2 != 180):
                y2 += 90  # s를 누르면 아래로 이동

    # 배경색상 설정하기
    screen.fill((255, 255, 255))
    # 이미지를 새로운 위치에 그리기
    screen.blit(image_buble, (x1, y1))
    screen.blit(image_sound, (x2, y2))

    # 화면 업데이트하기
    pygame.display.update()

    # 프레임 레이트 설정하기
    clock.tick(60)

# 게임 종료하기
pygame.quit()
sys.exit()
