import pygame
import sys


def init():
    pygame.init()
    window = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False

    for event in pygame.event.get():
        # 画面の閉じるボタンを押したとき
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # キーを押したとき
        if event.type == pygame.KEYDOWN:
            # ESCキーなら終了
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # すべてのキー入力の状態を確認
    keyInput = pygame.key.get_pressed()
    # キーに割り当てられた番号の取得
    keyNumber = getattr(pygame, 'K_{}'.format(keyName))

    # 押されているか
    if keyInput[keyNumber]:
        ans = True
    pygame.display.update()

    return ans






