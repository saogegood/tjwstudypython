"""
Module/Script Name:<snake_game>
Author: <Devin>
Date: <2023/3/31 13:43>
Description: <Description of Module/Script>
"""
import pygame
import sys
import random
import time

# 游戏初始化
pygame.init()

# 屏幕设置
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("贪吃蛇")

# 定义颜色
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# 蛇和食物的尺寸
snake_size = 20
food_size = 20

# 蛇的初始位置
snake_pos = [[100, 100], [80, 100], [60, 100]]

# 食物的初始位置
food_pos = [random.randrange(1, (width//20)) * 20, random.randrange(1, (height//20)) * 20]
food_spawn = True

# 设置方向
direction = "RIGHT"
change_to = direction

# 游戏速度
speed = 15
clock = pygame.time.Clock()

# 定义字体
font = pygame.font.SysFont("monospace", 35)

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    direction = change_to

    # 更新蛇的位置
    if direction == "UP":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] - snake_size])
    if direction == "DOWN":
        snake_pos.insert(0, [snake_pos[0][0], snake_pos[0][1] + snake_size])
    if direction == "LEFT":
        snake_pos.insert(0, [snake_pos[0][0] - snake_size, snake_pos[0][1]])
    if direction == "RIGHT":
        snake_pos.insert(0, [snake_pos[0][0] + snake_size, snake_pos[0][1]])

    # 检测蛇是否吃到食物
    if snake_pos[0] == food_pos:
        food_spawn = False
    else:
        snake_pos.pop()

    # 重新生成食物
    if not food_spawn:
        food_pos = [random.randrange(1, (width//20)) * 20, random.randrange(1, (height//20)) * 20]
    food_spawn = True

    # 蛇死亡检测
    if (snake_pos[0][0] < 0 or snake_pos[0][0] >= width or
            snake_pos[0][1] < 0 or snake_pos[0][1] >= height or
            snake_pos[0] in snake_pos[1:]):
        pygame.quit()
        sys.exit()

    # 清空屏幕
    black = (0, 0, 0)
    screen.fill(black)

    # 画蛇和食物
    for pos in snake_pos:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], food_size, food_size))

    # 更新显示 1
    pygame.display.flip()

    # 控制游戏速度
    clock.tick(speed)

