import pygame
import os


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.StartPositionX = 40
        self.StartPositionY = 40
        self.width_hex = 40
        self.height_hex = 40
        self.show_rules = False
        self.coor_hexes_x = []
        self.coor_hexes_y = []
        self.chosen_on = False
        self.chosen_x = 0
        self.chosen_y = 0
        self.now_move = 'blue'
        self.can_go1 = False
        self.can_go2 = False

        self.hp_sword_blue = [0, 50, 50, 50, 50, 50, 50, 50, 50, 50]
        self.hp_sword_red = [0, 50, 50, 50, 50, 50, 50, 50, 50, 50]
        self.hp_bow_blue = [0, 30, 30, 30, 30]
        self.hp_bow_red = [0, 30, 30, 30, 30]
        self.hp_cavalry_blue = [0, 70, 70, 70, 70, 70, 70]
        self.hp_cavalry_red = [0, 70, 70, 70, 70, 70, 70]

        self.stam_sword_blue = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.stam_sword_red = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.stam_bow_blue = [0, 2, 2, 2, 2]
        self.stam_bow_red = [0, 2, 2, 2, 2]
        self.stam_cavalry_blue = [0, 4, 4, 4, 4, 4, 4]
        self.stam_cavalry_red = [0, 4, 4, 4, 4, 4, 4]

        self.coor_blue_sword = [0, 33, 46, 20, 59, 58, 45, 32, 7, 19]
        self.coor_red_sword = [0, 191, 204, 192, 178, 179, 166, 165, 153, 152]
        self.coor_blue_bow = [0, 8, 21, 34, 47]
        self.coor_red_bow = [0, 203, 190, 177, 164]
        self.coor_blue_cavalry = [0, 86, 73, 99, 98, 85, 97]
        self.coor_red_cavalry = [0, 138, 125, 126, 112, 113, 114]

        for j in range(17):
            for i in range(12):
                self.coor_hexes_x.append(48 + j * 60)
                self.coor_hexes_y.append(68 + i * 40)
            for i in range(13):
                self.coor_hexes_x.append(78 + j * 60)
                self.coor_hexes_y.append(48 + i * 40)
        self.hex_fill = []
        for i in range(250):
            self.hex_fill.append('')

    def render(self):
        if self.show_rules is False:

            colors = [pygame.Color('black'), pygame.Color('white'), pygame.Color('red'), pygame.Color('green')]
            for y in range(self.height):
                dp = 0
                for x in range(self.width + 1):
                    pygame.draw.line(screen, colors[0],
                                     (self.width_hex * x + dp * 20 + self.StartPositionX, self.height_hex * y +
                                     self.StartPositionY + 40),
                                     (self.width_hex * x + 10 + dp * 20 + self.StartPositionX, self.height_hex * y - 20
                                      + self.StartPositionY + 40), 3)
                    pygame.draw.line(screen, colors[0],
                                     (self.width_hex * x + 10 + dp * 20 + self.StartPositionX, self.height_hex * y - 20
                                      + self.StartPositionY + 40),
                                     (self.width_hex * x + 30 + dp * 20 + self.StartPositionX, self.height_hex * y - 20
                                      + self.StartPositionY + 40), 3)
                    pygame.draw.line(screen, colors[0],
                                     (self.width_hex * x + 30 + dp * 20 + self.StartPositionX, self.height_hex * y - 20
                                      + self.StartPositionY + 40),
                                     (self.width_hex * x + 40 + dp * 20 + self.StartPositionX, self.height_hex * y
                                      + self.StartPositionY + 40), 3)
                    pygame.draw.line(screen, colors[0],
                                     (self.width_hex * x + 40 + dp * 20 + self.StartPositionX, self.height_hex * y
                                      + self.StartPositionY + 40),
                                     (self.width_hex * x + 30 + dp * 20 + self.StartPositionX, self.height_hex * y + 20
                                      + self.StartPositionY + 40), 3)
                    pygame.draw.line(screen, colors[0],
                                     (self.width_hex * x + 30 + dp * 20 + self.StartPositionX, self.height_hex * y + 20
                                      + self.StartPositionY + 40),
                                     (self.width_hex * x + 10 + dp * 20 + self.StartPositionX, self.height_hex * y + 20
                                      + self.StartPositionY + 40), 3)
                    pygame.draw.line(screen, colors[0],
                                     (self.width_hex * x + 10 + dp * 20 + self.StartPositionX, self.height_hex * y + 20
                                      + self.StartPositionY + 40),
                                     (self.width_hex * x + dp * 20 + self.StartPositionX, self.height_hex * y
                                      + self.StartPositionY + 40), 3)
                    dp += 1
                dp = 0
                for x in range(self.width):
                    pygame.draw.line(screen, colors[0], (self.width_hex * x + 30 + dp * 20 + self.StartPositionX,
                                                         self.height_hex * y + 20 + self.StartPositionY),
                                     (self.width_hex * x + 40 + dp * 20 + self.StartPositionX,
                                      self.height_hex * y + self.StartPositionY), 3)
                    pygame.draw.line(screen, colors[0], (self.width_hex * x + 40 + dp * 20 + self.StartPositionX,
                                                         self.height_hex * y + self.StartPositionY),
                                     (self.width_hex * x + 60 + dp * 20 + self.StartPositionX,
                                      self.height_hex * y + self.StartPositionY), 3)
                    pygame.draw.line(screen, colors[0], (self.width_hex * x + 60 + dp * 20 + self.StartPositionX,
                                                         self.height_hex * y + self.StartPositionY),
                                     (self.width_hex * x + 70 + dp * 20 + self.StartPositionX,
                                      self.height_hex * y + 20 + self.StartPositionY), 3)
                    pygame.draw.line(screen, colors[0], (self.width_hex * x + 70 + dp * 20 + self.StartPositionX,
                                                         self.height_hex * y + 20 + self.StartPositionY),
                                     (self.width_hex * x + 60 + dp * 20 + self.StartPositionX,
                                      self.height_hex * y + 40 + self.StartPositionY), 3)
                    pygame.draw.line(screen, colors[0], (self.width_hex * x + 60 + dp * 20 + self.StartPositionX,
                                                         self.height_hex * y + 40 + self.StartPositionY),
                                     (self.width_hex * x + 40 + dp * 20 + self.StartPositionX,
                                      self.height_hex * y + 40 + self.StartPositionY), 3)
                    pygame.draw.line(screen, colors[0], (self.width_hex * x + 40 + dp * 20 + self.StartPositionX,
                                                         self.height_hex * y + 40 + self.StartPositionY),
                                     (self.width_hex * x + 30 + dp * 20 + self.StartPositionX,
                                      self.height_hex * y + 20 + self.StartPositionY), 3)
                    dp += 1
            dop_pos_y = self.StartPositionY + self.height * self.height_hex
            y = 0
            dp = 0
            for x in range(self.width):
                pygame.draw.line(screen, colors[0],
                             (self.width_hex * x + 30 + dp * 20 + self.StartPositionX,
                              self.height_hex * y + 20 + dop_pos_y),
                             (self.width_hex * x + 40 + dp * 20 + self.StartPositionX, self.height_hex * y + dop_pos_y), 3)
                pygame.draw.line(screen, colors[0],
                             (self.width_hex * x + 40 + dp * 20 + self.StartPositionX, self.height_hex * y + dop_pos_y),
                             (self.width_hex * x + 60 + dp * 20 + self.StartPositionX, self.height_hex * y + dop_pos_y), 3)
                pygame.draw.line(screen, colors[0],
                             (self.width_hex * x + 60 + dp * 20 + self.StartPositionX, self.height_hex * y + dop_pos_y),
                             (self.width_hex * x + 70 + dp * 20 + self.StartPositionX,
                              self.height_hex * y + 20 + dop_pos_y), 3)
                pygame.draw.line(screen, colors[0],
                             (self.width_hex * x + 70 + dp * 20 + self.StartPositionX,
                              self.height_hex * y + 20 + dop_pos_y),
                             (self.width_hex * x + 60 + dp * 20 + self.StartPositionX,
                              self.height_hex * y + 40 + dop_pos_y), 3)
                pygame.draw.line(screen, colors[0],
                             (self.width_hex * x + 60 + dp * 20 + self.StartPositionX,
                              self.height_hex * y + 40 + dop_pos_y),
                             (self.width_hex * x + 40 + dp * 20 + self.StartPositionX,
                              self.height_hex * y + 40 + dop_pos_y), 3)
                pygame.draw.line(screen, colors[0],
                             (self.width_hex * x + 40 + dp * 20 + self.StartPositionX,
                              self.height_hex * y + 40 + dop_pos_y),
                             (self.width_hex * x + 30 + dp * 20 + self.StartPositionX,
                              self.height_hex * y + 20 + dop_pos_y), 3)
                dp += 1
            help_spr = pygame.sprite.Sprite()
            help_spr.image = load_image("help.png")
            help_spr.rect = help_spr.image.get_rect()
            help_spr.rect.x = 0
            help_spr.rect.y = 0
            all_sprites.add(help_spr)

            button_up_spr = pygame.sprite.Sprite()
            button_up_spr.image = load_image("arrow_move_up.jpg")
            button_up_spr.rect = button_up_spr.image.get_rect()
            button_up_spr.rect.x = 675
            button_up_spr.rect.y = 100
            all_sprites.add(button_up_spr)

            button_down_spr = pygame.sprite.Sprite()
            button_down_spr.image = load_image("arrow_move_down.jpg")
            button_down_spr.rect = button_down_spr.image.get_rect()
            button_down_spr.rect.x = 675
            button_down_spr.rect.y = 250
            all_sprites.add(button_down_spr)

            button_up_left_spr = pygame.sprite.Sprite()
            button_up_left_spr.image = load_image("arrow_move_up_left.jpg")
            button_up_left_spr.rect = button_up_left_spr.image.get_rect()
            button_up_left_spr.rect.x = 625
            button_up_left_spr.rect.y = 125
            all_sprites.add(button_up_left_spr)

            button_down_left_spr = pygame.sprite.Sprite()
            button_down_left_spr.image = load_image("arrow_move_down_left.jpg")
            button_down_left_spr.rect = button_down_left_spr.image.get_rect()
            button_down_left_spr.rect.x = 625
            button_down_left_spr.rect.y = 225
            all_sprites.add(button_down_left_spr)

            button_up_right_spr = pygame.sprite.Sprite()
            button_up_right_spr.image = load_image("arrow_move_up_right.jpg")
            button_up_right_spr.rect = button_up_right_spr.image.get_rect()
            button_up_right_spr.rect.x = 725
            button_up_right_spr.rect.y = 125
            all_sprites.add(button_up_right_spr)

            button_down_right_spr = pygame.sprite.Sprite()
            button_down_right_spr.image = load_image("arrow_move_down_right.jpg")
            button_down_right_spr.rect = button_down_right_spr.image.get_rect()
            button_down_right_spr.rect.x = 725
            button_down_right_spr.rect.y = 225
            all_sprites.add(button_down_right_spr)

            def_spr = pygame.sprite.Sprite()
            def_spr.image = load_image("def.png")
            def_spr.rect = def_spr.image.get_rect()
            def_spr.rect.x = 670
            def_spr.rect.y = 170
            all_sprites.add(def_spr)

            blue_main = pygame.sprite.Sprite()
            blue_main.image = load_image("main_blue.png")
            blue_main.rect = blue_main.image.get_rect()
            blue_main.rect.x = self.coor_hexes_x[23]
            blue_main.rect.y = self.coor_hexes_y[23]
            self.hex_fill[23] = 'blue_main'
            all_sprites.add(blue_main)
            self.hp_blue_main = 1
            if self.hp_blue_main <= 0:
                print('red win')

            red_main = pygame.sprite.Sprite()
            red_main.image = load_image("main_red.png")
            red_main.rect = red_main.image.get_rect()
            red_main.rect.x = self.coor_hexes_x[188]
            red_main.rect.y = self.coor_hexes_y[188]
            self.hex_fill[188] = 'red_main'
            all_sprites.add(red_main)
            self.hp_red_main = 1
            if self.hp_blue_main <= 0:
                print('blue win')

            end = pygame.sprite.Sprite()
            end.image = load_image("end.png")
            end.rect = end.image.get_rect()
            end.rect.x = 725
            end.rect.y = 325
            all_sprites.add(end)

            start_move = pygame.sprite.Sprite()
            start_move.image = load_image("start_move.png")
            start_move.rect = start_move.image.get_rect()
            start_move.rect.x = 625
            start_move.rect.y = 325
            all_sprites.add(start_move)

            font1 = pygame.font.Font(None, 15)

            sword_blue_1 = pygame.sprite.Sprite()
            sword_blue_1.image = load_image("sword_blue.png")
            sword_blue_1.rect = sword_blue_1.image.get_rect()
            sword_blue_1.rect.x = self.coor_hexes_x[self.coor_blue_sword[1]]
            sword_blue_1.rect.y = self.coor_hexes_y[self.coor_blue_sword[1]]
            hp_sword_blue_1 = font1.render(str(self.hp_sword_blue[1]), 1, (0, 0, 255))
            place = hp_sword_blue_1.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[1]] + 9, self.coor_hexes_y[self.coor_blue_sword[1]] + 2))
            screen.blit(hp_sword_blue_1, place)
            stam_sword_blue_1 = font1.render(str(self.stam_sword_blue[1]), 1, (0, 0, 255))
            place1 = stam_sword_blue_1.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[1]] + 21, self.coor_hexes_y[self.coor_blue_sword[1]] + 23))
            screen.blit(stam_sword_blue_1, place1)
            self.hex_fill[self.coor_blue_sword[1]] = 'blue_sword_1'
            all_sprites.add(sword_blue_1)

            sword_blue_2 = pygame.sprite.Sprite()
            sword_blue_2.image = load_image("sword_blue.png")
            sword_blue_2.rect = sword_blue_2.image.get_rect()
            sword_blue_2.rect.x = self.coor_hexes_x[self.coor_blue_sword[2]]
            sword_blue_2.rect.y = self.coor_hexes_y[self.coor_blue_sword[2]]
            self.hex_fill[self.coor_blue_sword[2]] = 'blue_sword_2'
            hp_sword_blue_2 = font1.render(str(self.hp_sword_blue[2]), 1, (0, 0, 255))
            place = hp_sword_blue_2.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[2]] + 9, self.coor_hexes_y[self.coor_blue_sword[2]] + 2))
            screen.blit(hp_sword_blue_2, place)
            stam_sword_blue_2 = font1.render(str(self.stam_sword_blue[2]), 1, (0, 0, 255))
            place1 = stam_sword_blue_2.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_sword[2]] + 21, self.coor_hexes_y[self.coor_blue_sword[2]] + 23))
            screen.blit(stam_sword_blue_2, place1)
            all_sprites.add(sword_blue_2)

            sword_blue_3 = pygame.sprite.Sprite()
            sword_blue_3.image = load_image("sword_blue.png")
            sword_blue_3.rect = sword_blue_3.image.get_rect()
            sword_blue_3.rect.x = self.coor_hexes_x[self.coor_blue_sword[3]]
            sword_blue_3.rect.y = self.coor_hexes_y[self.coor_blue_sword[3]]
            self.hex_fill[self.coor_blue_sword[3]] = 'blue_sword_3'
            hp_sword_blue_3 = font1.render(str(self.hp_sword_blue[3]), 1, (0, 0, 255))
            place = hp_sword_blue_3.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[3]] + 9, self.coor_hexes_y[self.coor_blue_sword[3]] + 2))
            screen.blit(hp_sword_blue_3, place)
            stam_sword_blue_3 = font1.render(str(self.stam_sword_blue[3]), 1, (0, 0, 255))
            place1 = stam_sword_blue_3.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_sword[3]] + 21, self.coor_hexes_y[self.coor_blue_sword[3]] + 23))
            screen.blit(stam_sword_blue_3, place1)
            all_sprites.add(sword_blue_3)

            sword_blue_4 = pygame.sprite.Sprite()
            sword_blue_4.image = load_image("sword_blue.png")
            sword_blue_4.rect = sword_blue_4.image.get_rect()
            sword_blue_4.rect.x = self.coor_hexes_x[self.coor_blue_sword[4]]
            sword_blue_4.rect.y = self.coor_hexes_y[self.coor_blue_sword[4]]
            self.hex_fill[self.coor_blue_sword[4]] = 'blue_sword_4'
            hp_sword_blue_4 = font1.render(str(self.hp_sword_blue[4]), 1, (0, 0, 255))
            place = hp_sword_blue_4.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[4]] + 9, self.coor_hexes_y[self.coor_blue_sword[4]] + 2))
            screen.blit(hp_sword_blue_4, place)
            stam_sword_blue_4 = font1.render(str(self.stam_sword_blue[4]), 1, (0, 0, 255))
            place1 = stam_sword_blue_4.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_sword[4]] + 21, self.coor_hexes_y[self.coor_blue_sword[4]] + 23))
            screen.blit(stam_sword_blue_4, place1)
            all_sprites.add(sword_blue_4)

            sword_blue_5 = pygame.sprite.Sprite()
            sword_blue_5.image = load_image("sword_blue.png")
            sword_blue_5.rect = sword_blue_5.image.get_rect()
            sword_blue_5.rect.x = self.coor_hexes_x[self.coor_blue_sword[5]]
            sword_blue_5.rect.y = self.coor_hexes_y[self.coor_blue_sword[5]]
            self.hex_fill[self.coor_blue_sword[5]] = 'blue_sword_5'
            hp_sword_blue_5 = font1.render(str(self.hp_sword_blue[5]), 1, (0, 0, 255))
            place = hp_sword_blue_5.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[5]] + 9, self.coor_hexes_y[self.coor_blue_sword[5]] + 2))
            screen.blit(hp_sword_blue_5, place)
            stam_sword_blue_5 = font1.render(str(self.stam_sword_blue[5]), 1, (0, 0, 255))
            place1 = stam_sword_blue_5.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_sword[5]] + 21, self.coor_hexes_y[self.coor_blue_sword[5]] + 23))
            screen.blit(stam_sword_blue_5, place1)
            all_sprites.add(sword_blue_5)

            sword_blue_6 = pygame.sprite.Sprite()
            sword_blue_6.image = load_image("sword_blue.png")
            sword_blue_6.rect = sword_blue_6.image.get_rect()
            sword_blue_6.rect.x = self.coor_hexes_x[self.coor_blue_sword[6]]
            sword_blue_6.rect.y = self.coor_hexes_y[self.coor_blue_sword[6]]
            self.hex_fill[self.coor_blue_sword[6]] = 'blue_sword_6'
            hp_sword_blue_6 = font1.render(str(self.hp_sword_blue[6]), 1, (0, 0, 255))
            place = hp_sword_blue_6.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[6]] + 9, self.coor_hexes_y[self.coor_blue_sword[6]] + 2))
            screen.blit(hp_sword_blue_6, place)
            stam_sword_blue_6 = font1.render(str(self.stam_sword_blue[6]), 1, (0, 0, 255))
            place1 = stam_sword_blue_6.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_sword[6]] + 21, self.coor_hexes_y[self.coor_blue_sword[6]] + 23))
            screen.blit(stam_sword_blue_6, place1)
            all_sprites.add(sword_blue_6)

            sword_blue_7 = pygame.sprite.Sprite()
            sword_blue_7.image = load_image("sword_blue.png")
            sword_blue_7.rect = sword_blue_7.image.get_rect()
            sword_blue_7.rect.x = self.coor_hexes_x[self.coor_blue_sword[7]]
            sword_blue_7.rect.y = self.coor_hexes_y[self.coor_blue_sword[7]]
            self.hex_fill[self.coor_blue_sword[7]] = 'blue_sword_7'
            hp_sword_blue_7 = font1.render(str(self.hp_sword_blue[7]), 1, (0, 0, 255))
            place = hp_sword_blue_7.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[7]] + 9, self.coor_hexes_y[self.coor_blue_sword[7]] + 2))
            screen.blit(hp_sword_blue_7, place)
            stam_sword_blue_7 = font1.render(str(self.stam_sword_blue[7]), 1, (0, 0, 255))
            place1 = stam_sword_blue_7.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_sword[7]] + 21, self.coor_hexes_y[self.coor_blue_sword[7]] + 23))
            screen.blit(stam_sword_blue_7, place1)
            all_sprites.add(sword_blue_7)

            sword_blue_8 = pygame.sprite.Sprite()
            sword_blue_8.image = load_image("sword_blue.png")
            sword_blue_8.rect = sword_blue_8.image.get_rect()
            sword_blue_8.rect.x = self.coor_hexes_x[self.coor_blue_sword[8]]
            sword_blue_8.rect.y = self.coor_hexes_y[self.coor_blue_sword[8]]
            self.hex_fill[self.coor_blue_sword[8]] = 'blue_sword_8'
            hp_sword_blue_8 = font1.render(str(self.hp_sword_blue[8]), 1, (0, 0, 255))
            place = hp_sword_blue_8.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[8]] + 9, self.coor_hexes_y[self.coor_blue_sword[8]] + 2))
            screen.blit(hp_sword_blue_8, place)
            stam_sword_blue_8 = font1.render(str(self.stam_sword_blue[8]), 1, (0, 0, 255))
            place1 = stam_sword_blue_8.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_sword[8]] + 21, self.coor_hexes_y[self.coor_blue_sword[8]] + 23))
            screen.blit(stam_sword_blue_8, place1)
            all_sprites.add(sword_blue_8)

            sword_blue_9 = pygame.sprite.Sprite()
            sword_blue_9.image = load_image("sword_blue.png")
            sword_blue_9.rect = sword_blue_9.image.get_rect()
            sword_blue_9.rect.x = self.coor_hexes_x[self.coor_blue_sword[9]]
            sword_blue_9.rect.y = self.coor_hexes_y[self.coor_blue_sword[9]]
            self.hex_fill[self.coor_blue_sword[9]] = 'blue_sword_9'
            hp_sword_blue_9 = font1.render(str(self.hp_sword_blue[9]), 1, (0, 0, 255))
            place = hp_sword_blue_9.get_rect(center=(self.coor_hexes_x[self.coor_blue_sword[9]] + 9, self.coor_hexes_y[self.coor_blue_sword[9]] + 2))
            screen.blit(hp_sword_blue_9, place)
            stam_sword_blue_9 = font1.render(str(self.stam_sword_blue[9]), 1, (0, 0, 255))
            place1 = stam_sword_blue_9.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_sword[9]] + 21, self.coor_hexes_y[self.coor_blue_sword[9]] + 23))
            screen.blit(stam_sword_blue_9, place1)
            all_sprites.add(sword_blue_9)

            sword_red_1 = pygame.sprite.Sprite()
            sword_red_1.image = load_image("sword_red.png")
            sword_red_1.rect = sword_red_1.image.get_rect()
            sword_red_1.rect.x = self.coor_hexes_x[self.coor_red_sword[1]]
            sword_red_1.rect.y = self.coor_hexes_y[self.coor_red_sword[1]]
            hp_sword_red_1 = font1.render(str(self.hp_sword_red[1]), 1, (255, 0, 0))
            place = hp_sword_red_1.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[1]] + 17, self.coor_hexes_y[self.coor_red_sword[1]] + 2))
            screen.blit(hp_sword_red_1, place)
            stam_sword_red_1 = font1.render(str(self.stam_sword_red[1]), 1, (255, 0, 0))
            place1 = stam_sword_red_1.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[1]] + 6, self.coor_hexes_y[self.coor_red_sword[1]] + 23))
            screen.blit(stam_sword_red_1, place1)
            self.hex_fill[self.coor_red_sword[1]] = 'red_sword_1'
            all_sprites.add(sword_red_1)

            sword_red_2 = pygame.sprite.Sprite()
            sword_red_2.image = load_image("sword_red.png")
            sword_red_2.rect = sword_red_2.image.get_rect()
            sword_red_2.rect.x = self.coor_hexes_x[self.coor_red_sword[2]]
            sword_red_2.rect.y = self.coor_hexes_y[self.coor_red_sword[2]]
            self.hex_fill[self.coor_red_sword[2]] = 'red_sword_2'
            hp_sword_red_2 = font1.render(str(self.hp_sword_red[2]), 1, (255, 0, 0))
            place = hp_sword_red_2.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[2]] + 17, self.coor_hexes_y[self.coor_red_sword[2]] + 2))
            screen.blit(hp_sword_red_2, place)
            stam_sword_red_2 = font1.render(str(self.stam_sword_red[2]), 1, (255, 0, 0))
            place1 = stam_sword_red_2.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[2]] + 6, self.coor_hexes_y[self.coor_red_sword[2]] + 23))
            screen.blit(stam_sword_red_2, place1)
            all_sprites.add(sword_red_2)

            sword_red_3 = pygame.sprite.Sprite()
            sword_red_3.image = load_image("sword_red.png")
            sword_red_3.rect = sword_red_3.image.get_rect()
            sword_red_3.rect.x = self.coor_hexes_x[self.coor_red_sword[3]]
            sword_red_3.rect.y = self.coor_hexes_y[self.coor_red_sword[3]]
            self.hex_fill[self.coor_red_sword[3]] = 'red_sword_3'
            hp_sword_red_3 = font1.render(str(self.hp_sword_red[3]), 1, (255, 0, 0))
            place = hp_sword_red_3.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[3]] + 17, self.coor_hexes_y[self.coor_red_sword[3]] + 2))
            screen.blit(hp_sword_red_3, place)
            stam_sword_red_3 = font1.render(str(self.stam_sword_red[3]), 1, (255, 0, 0))
            place1 = stam_sword_red_3.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[3]] + 6, self.coor_hexes_y[self.coor_red_sword[3]] + 23))
            screen.blit(stam_sword_red_3, place1)
            all_sprites.add(sword_red_3)

            sword_red_4 = pygame.sprite.Sprite()
            sword_red_4.image = load_image("sword_red.png")
            sword_red_4.rect = sword_red_4.image.get_rect()
            sword_red_4.rect.x = self.coor_hexes_x[self.coor_red_sword[4]]
            sword_red_4.rect.y = self.coor_hexes_y[self.coor_red_sword[4]]
            self.hex_fill[self.coor_red_sword[4]] = 'red_sword_4'
            hp_sword_red_4 = font1.render(str(self.hp_sword_red[4]), 1, (255, 0, 0))
            place = hp_sword_red_4.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[4]] + 17, self.coor_hexes_y[self.coor_red_sword[4]] + 2))
            screen.blit(hp_sword_red_4, place)
            stam_sword_red_4 = font1.render(str(self.stam_sword_red[4]), 1, (255, 0, 0))
            place1 = stam_sword_red_4.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[4]] + 6, self.coor_hexes_y[self.coor_red_sword[4]] + 23))
            screen.blit(stam_sword_red_4, place1)
            all_sprites.add(sword_red_4)

            sword_red_5 = pygame.sprite.Sprite()
            sword_red_5.image = load_image("sword_red.png")
            sword_red_5.rect = sword_red_5.image.get_rect()
            sword_red_5.rect.x = self.coor_hexes_x[self.coor_red_sword[5]]
            sword_red_5.rect.y = self.coor_hexes_y[self.coor_red_sword[5]]
            self.hex_fill[self.coor_red_sword[5]] = 'red_sword_5'
            hp_sword_red_5 = font1.render(str(self.hp_sword_red[5]), 1, (255, 0, 0))
            place = hp_sword_red_5.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[5]] + 17, self.coor_hexes_y[self.coor_red_sword[5]] + 2))
            screen.blit(hp_sword_red_5, place)
            stam_sword_red_5 = font1.render(str(self.stam_sword_red[5]), 1, (255, 0, 0))
            place1 = stam_sword_red_5.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[5]] + 6, self.coor_hexes_y[self.coor_red_sword[5]] + 23))
            screen.blit(stam_sword_red_5, place1)
            all_sprites.add(sword_red_5)

            sword_red_6 = pygame.sprite.Sprite()
            sword_red_6.image = load_image("sword_red.png")
            sword_red_6.rect = sword_red_6.image.get_rect()
            sword_red_6.rect.x = self.coor_hexes_x[self.coor_red_sword[6]]
            sword_red_6.rect.y = self.coor_hexes_y[self.coor_red_sword[6]]
            self.hex_fill[self.coor_red_sword[6]] = 'red_sword_6'
            hp_sword_red_6 = font1.render(str(self.hp_sword_red[6]), 1, (255, 0, 0))
            place = hp_sword_red_6.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[6]] + 17, self.coor_hexes_y[self.coor_red_sword[6]] + 2))
            screen.blit(hp_sword_red_6, place)
            stam_sword_red_6 = font1.render(str(self.stam_sword_red[6]), 1, (255, 0, 0))
            place1 = stam_sword_red_6.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[6]] + 6, self.coor_hexes_y[self.coor_red_sword[6]] + 23))
            screen.blit(stam_sword_red_6, place1)
            all_sprites.add(sword_red_6)

            sword_red_7 = pygame.sprite.Sprite()
            sword_red_7.image = load_image("sword_red.png")
            sword_red_7.rect = sword_red_7.image.get_rect()
            sword_red_7.rect.x = self.coor_hexes_x[self.coor_red_sword[7]]
            sword_red_7.rect.y = self.coor_hexes_y[self.coor_red_sword[7]]
            self.hex_fill[self.coor_red_sword[7]] = 'red_sword_7'
            hp_sword_red_7 = font1.render(str(self.hp_sword_red[7]), 1, (255, 0, 0))
            place = hp_sword_red_7.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[7]] + 17, self.coor_hexes_y[self.coor_red_sword[7]] + 2))
            screen.blit(hp_sword_red_7, place)
            stam_sword_red_7 = font1.render(str(self.stam_sword_red[7]), 1, (255, 0, 0))
            place1 = stam_sword_red_7.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[7]] + 6, self.coor_hexes_y[self.coor_red_sword[7]] + 23))
            screen.blit(stam_sword_red_7, place1)
            all_sprites.add(sword_red_7)

            sword_red_8 = pygame.sprite.Sprite()
            sword_red_8.image = load_image("sword_red.png")
            sword_red_8.rect = sword_red_8.image.get_rect()
            sword_red_8.rect.x = self.coor_hexes_x[self.coor_red_sword[8]]
            sword_red_8.rect.y = self.coor_hexes_y[self.coor_red_sword[8]]
            self.hex_fill[self.coor_red_sword[8]] = 'red_sword_8'
            hp_sword_red_8 = font1.render(str(self.hp_sword_red[8]), 1, (255, 0, 0))
            place = hp_sword_red_8.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[8]] + 17, self.coor_hexes_y[self.coor_red_sword[8]] + 2))
            screen.blit(hp_sword_red_8, place)
            stam_sword_red_8 = font1.render(str(self.stam_sword_red[8]), 1, (255, 0, 0))
            place1 = stam_sword_red_8.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[8]] + 6, self.coor_hexes_y[self.coor_red_sword[8]] + 23))
            screen.blit(stam_sword_red_8, place1)
            all_sprites.add(sword_red_8)

            sword_red_9 = pygame.sprite.Sprite()
            sword_red_9.image = load_image("sword_red.png")
            sword_red_9.rect = sword_red_9.image.get_rect()
            sword_red_9.rect.x = self.coor_hexes_x[self.coor_red_sword[9]]
            sword_red_9.rect.y = self.coor_hexes_y[self.coor_red_sword[9]]
            self.hex_fill[self.coor_red_sword[9]] = 'red_sword_9'
            hp_sword_red_9 = font1.render(str(self.hp_sword_red[9]), 1, (255, 0, 0))
            place = hp_sword_red_9.get_rect(center=(self.coor_hexes_x[self.coor_red_sword[9]] + 17, self.coor_hexes_y[self.coor_red_sword[9]] + 2))
            screen.blit(hp_sword_red_9, place)
            stam_sword_red_9 = font1.render(str(self.stam_sword_red[9]), 1, (255, 0, 0))
            place1 = stam_sword_red_9.get_rect(center=(
                self.coor_hexes_x[self.coor_red_sword[9]] + 6, self.coor_hexes_y[self.coor_red_sword[9]] + 23))
            screen.blit(stam_sword_red_9, place1)
            all_sprites.add(sword_red_9)

            bow_blue_1 = pygame.sprite.Sprite()
            bow_blue_1.image = load_image("bow_blue.png")
            bow_blue_1.rect = bow_blue_1.image.get_rect()
            bow_blue_1.rect.x = self.coor_hexes_x[self.coor_blue_bow[1]]
            bow_blue_1.rect.y = self.coor_hexes_y[self.coor_blue_bow[1]]
            self.hex_fill[self.coor_blue_bow[1]] = 'blue_bow_1'
            hp_bow_blue_1 = font1.render(str(self.hp_bow_blue[1]), 1, (0, 0, 255))
            place = hp_bow_blue_1.get_rect(center=(self.coor_hexes_x[self.coor_blue_bow[1]] + 13, self.coor_hexes_y[self.coor_blue_bow[1]] - 1))
            screen.blit(hp_bow_blue_1, place)
            stam_bow_blue_1 = font1.render(str(self.stam_bow_blue[1]), 1, (0, 0, 255))
            place1 = stam_bow_blue_1.get_rect(center=(
            self.coor_hexes_x[self.coor_blue_bow[1]] - 1, self.coor_hexes_y[self.coor_blue_bow[1]] + 13))
            screen.blit(stam_bow_blue_1, place1)
            all_sprites.add(bow_blue_1)

            bow_blue_2 = pygame.sprite.Sprite()
            bow_blue_2.image = load_image("bow_blue.png")
            bow_blue_2.rect = bow_blue_2.image.get_rect()
            bow_blue_2.rect.x = self.coor_hexes_x[self.coor_blue_bow[2]]
            bow_blue_2.rect.y = self.coor_hexes_y[self.coor_blue_bow[2]]
            self.hex_fill[self.coor_blue_bow[2]] = 'blue_bow_2'
            hp_bow_blue_2 = font1.render(str(self.hp_bow_blue[2]), 1, (0, 0, 255))
            place = hp_bow_blue_2.get_rect(center=(self.coor_hexes_x[self.coor_blue_bow[2]] + 13, self.coor_hexes_y[self.coor_blue_bow[2]] - 1))
            screen.blit(hp_bow_blue_2, place)
            stam_bow_blue_2 = font1.render(str(self.stam_bow_blue[2]), 1, (0, 0, 255))
            place1 = stam_bow_blue_2.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_bow[2]] - 1, self.coor_hexes_y[self.coor_blue_bow[2]] + 13))
            screen.blit(stam_bow_blue_2, place1)
            all_sprites.add(bow_blue_2)

            bow_blue_3 = pygame.sprite.Sprite()
            bow_blue_3.image = load_image("bow_blue.png")
            bow_blue_3.rect = bow_blue_3.image.get_rect()
            bow_blue_3.rect.x = self.coor_hexes_x[self.coor_blue_bow[3]]
            bow_blue_3.rect.y = self.coor_hexes_y[self.coor_blue_bow[3]]
            self.hex_fill[self.coor_blue_bow[3]] = 'blue_bow_3'
            hp_bow_blue_3 = font1.render(str(self.hp_bow_blue[3]), 1, (0, 0, 255))
            place = hp_bow_blue_3.get_rect(center=(self.coor_hexes_x[self.coor_blue_bow[3]] + 13, self.coor_hexes_y[self.coor_blue_bow[3]] - 1))
            screen.blit(hp_bow_blue_3, place)
            stam_bow_blue_3 = font1.render(str(self.stam_bow_blue[3]), 1, (0, 0, 255))
            place1 = stam_bow_blue_3.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_bow[3]] - 1, self.coor_hexes_y[self.coor_blue_bow[3]] + 13))
            screen.blit(stam_bow_blue_3, place1)
            all_sprites.add(bow_blue_3)

            bow_blue_4 = pygame.sprite.Sprite()
            bow_blue_4.image = load_image("bow_blue.png")
            bow_blue_4.rect = bow_blue_4.image.get_rect()
            bow_blue_4.rect.x = self.coor_hexes_x[self.coor_blue_bow[4]]
            bow_blue_4.rect.y = self.coor_hexes_y[self.coor_blue_bow[4]]
            self.hex_fill[self.coor_blue_bow[4]] = 'blue_bow_4'
            hp_bow_blue_4 = font1.render(str(self.hp_bow_blue[4]), 1, (0, 0, 255))
            place = hp_bow_blue_4.get_rect(center=(self.coor_hexes_x[self.coor_blue_bow[4]] + 13, self.coor_hexes_y[self.coor_blue_bow[4]] - 1))
            screen.blit(hp_bow_blue_4, place)
            stam_bow_blue_4 = font1.render(str(self.stam_bow_blue[4]), 1, (0, 0, 255))
            place1 = stam_bow_blue_4.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_bow[4]] - 1, self.coor_hexes_y[self.coor_blue_bow[4]] + 13))
            screen.blit(stam_bow_blue_4, place1)
            all_sprites.add(bow_blue_4)

            bow_red_1 = pygame.sprite.Sprite()
            bow_red_1.image = load_image("bow_red.png")
            bow_red_1.rect = bow_red_1.image.get_rect()
            bow_red_1.rect.x = self.coor_hexes_x[self.coor_red_bow[1]]
            bow_red_1.rect.y = self.coor_hexes_y[self.coor_red_bow[1]]
            self.hex_fill[self.coor_red_bow[1]] = 'red_bow_1'
            hp_bow_red_1 = font1.render(str(self.hp_bow_red[1]), 1, (255, 0, 0))
            place = hp_bow_red_1.get_rect(center=(self.coor_hexes_x[self.coor_red_bow[1]] + 13, self.coor_hexes_y[self.coor_red_bow[1]] - 1))
            screen.blit(hp_bow_red_1, place)
            stam_bow_red_1 = font1.render(str(self.stam_bow_red[1]), 1, (255, 0, 0))
            place1 = stam_bow_red_1.get_rect(center=(
                self.coor_hexes_x[self.coor_red_bow[1]] + 26, self.coor_hexes_y[self.coor_red_bow[1]] + 13))
            screen.blit(stam_bow_red_1, place1)
            all_sprites.add(bow_red_1)

            bow_red_2 = pygame.sprite.Sprite()
            bow_red_2.image = load_image("bow_red.png")
            bow_red_2.rect = bow_red_2.image.get_rect()
            bow_red_2.rect.x = self.coor_hexes_x[self.coor_red_bow[2]]
            bow_red_2.rect.y = self.coor_hexes_y[self.coor_red_bow[2]]
            self.hex_fill[self.coor_red_bow[2]] = 'red_bow_2'
            hp_bow_red_2 = font1.render(str(self.hp_bow_red[2]), 1, (255, 0, 0))
            place = hp_bow_red_2.get_rect(center=(self.coor_hexes_x[self.coor_red_bow[2]] + 13, self.coor_hexes_y[self.coor_red_bow[2]] - 1))
            screen.blit(hp_bow_red_2, place)
            stam_bow_red_2 = font1.render(str(self.stam_bow_red[2]), 1, (255, 0, 0))
            place1 = stam_bow_red_2.get_rect(center=(
                self.coor_hexes_x[self.coor_red_bow[2]] + 26, self.coor_hexes_y[self.coor_red_bow[2]] + 13))
            screen.blit(stam_bow_red_2, place1)
            all_sprites.add(bow_red_2)

            bow_red_3 = pygame.sprite.Sprite()
            bow_red_3.image = load_image("bow_red.png")
            bow_red_3.rect = bow_red_3.image.get_rect()
            bow_red_3.rect.x = self.coor_hexes_x[self.coor_red_bow[3]]
            bow_red_3.rect.y = self.coor_hexes_y[self.coor_red_bow[3]]
            self.hex_fill[self.coor_red_bow[3]] = 'red_bow_3'
            hp_bow_red_3 = font1.render(str(self.hp_bow_red[3]), 1, (255, 0, 0))
            place = hp_bow_red_3.get_rect(center=(self.coor_hexes_x[self.coor_red_bow[3]] + 13, self.coor_hexes_y[self.coor_red_bow[3]] - 1))
            screen.blit(hp_bow_red_3, place)
            stam_bow_red_3 = font1.render(str(self.stam_bow_red[3]), 1, (255, 0, 0))
            place1 = stam_bow_red_3.get_rect(center=(
                self.coor_hexes_x[self.coor_red_bow[3]] + 26, self.coor_hexes_y[self.coor_red_bow[3]] + 13))
            screen.blit(stam_bow_red_3, place1)
            all_sprites.add(bow_red_3)

            bow_red_4 = pygame.sprite.Sprite()
            bow_red_4.image = load_image("bow_red.png")
            bow_red_4.rect = bow_red_4.image.get_rect()
            bow_red_4.rect.x = self.coor_hexes_x[self.coor_red_bow[4]]
            bow_red_4.rect.y = self.coor_hexes_y[self.coor_red_bow[4]]
            self.hex_fill[self.coor_red_bow[4]] = 'red_bow_4'
            hp_bow_red_4 = font1.render(str(self.hp_bow_red[4]), 1, (255, 0, 0))
            place = hp_bow_red_4.get_rect(center=(self.coor_hexes_x[self.coor_red_bow[4]] + 13, self.coor_hexes_y[self.coor_red_bow[4]] - 1))
            screen.blit(hp_bow_red_4, place)
            stam_bow_red_4 = font1.render(str(self.stam_bow_red[4]), 1, (255, 0, 0))
            place1 = stam_bow_red_4.get_rect(center=(
                self.coor_hexes_x[self.coor_red_bow[4]] + 26, self.coor_hexes_y[self.coor_red_bow[4]] + 13))
            screen.blit(stam_bow_red_4, place1)
            all_sprites.add(bow_red_4)

            cavalry_blue_1 = pygame.sprite.Sprite()
            cavalry_blue_1.image = load_image("cavalry_blue.png")
            cavalry_blue_1.rect = cavalry_blue_1.image.get_rect()
            cavalry_blue_1.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[1]]
            cavalry_blue_1.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[1]]
            self.hex_fill[self.coor_blue_cavalry[1]] = 'blue_cavalry_1'
            hp_cavalry_blue_1 = font1.render(str(self.hp_cavalry_blue[1]), 1, (0, 0, 255))
            place = hp_cavalry_blue_1.get_rect(center=(self.coor_hexes_x[self.coor_blue_cavalry[1]] + 17, self.coor_hexes_y[self.coor_blue_cavalry[1]]))
            screen.blit(hp_cavalry_blue_1, place)
            stam_cavalry_blue_1 = font1.render(str(self.stam_cavalry_blue[1]), 1, (0, 0, 255))
            place1 = stam_cavalry_blue_1.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_cavalry[1]] + 3, self.coor_hexes_y[self.coor_blue_cavalry[1]] + 10))
            screen.blit(stam_cavalry_blue_1, place1)
            all_sprites.add(cavalry_blue_1)

            cavalry_blue_2 = pygame.sprite.Sprite()
            cavalry_blue_2.image = load_image("cavalry_blue.png")
            cavalry_blue_2.rect = cavalry_blue_2.image.get_rect()
            cavalry_blue_2.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[2]]
            cavalry_blue_2.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[2]]
            self.hex_fill[self.coor_blue_cavalry[2]] = 'blue_cavalry_2'
            hp_cavalry_blue_2 = font1.render(str(self.hp_cavalry_blue[2]), 1, (0, 0, 255))
            place = hp_cavalry_blue_2.get_rect(center=(self.coor_hexes_x[self.coor_blue_cavalry[2]] + 17, self.coor_hexes_y[self.coor_blue_cavalry[2]]))
            screen.blit(hp_cavalry_blue_2, place)
            stam_cavalry_blue_2 = font1.render(str(self.stam_cavalry_blue[2]), 1, (0, 0, 255))
            place1 = stam_cavalry_blue_2.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_cavalry[2]] + 3, self.coor_hexes_y[self.coor_blue_cavalry[2]] + 10))
            screen.blit(stam_cavalry_blue_2, place1)
            all_sprites.add(cavalry_blue_2)

            cavalry_blue_3 = pygame.sprite.Sprite()
            cavalry_blue_3.image = load_image("cavalry_blue.png")
            cavalry_blue_3.rect = cavalry_blue_3.image.get_rect()
            cavalry_blue_3.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[3]]
            cavalry_blue_3.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[3]]
            self.hex_fill[self.coor_blue_cavalry[3]] = 'blue_cavalry_3'
            hp_cavalry_blue_3 = font1.render(str(self.hp_cavalry_blue[3]), 1, (0, 0, 255))
            place = hp_cavalry_blue_3.get_rect(center=(self.coor_hexes_x[self.coor_blue_cavalry[3]] + 17, self.coor_hexes_y[self.coor_blue_cavalry[3]]))
            screen.blit(hp_cavalry_blue_3, place)
            stam_cavalry_blue_3 = font1.render(str(self.stam_cavalry_blue[3]), 1, (0, 0, 255))
            place1 = stam_cavalry_blue_3.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_cavalry[3]] + 3, self.coor_hexes_y[self.coor_blue_cavalry[3]] + 10))
            screen.blit(stam_cavalry_blue_3, place1)
            all_sprites.add(cavalry_blue_3)

            cavalry_blue_4 = pygame.sprite.Sprite()
            cavalry_blue_4.image = load_image("cavalry_blue.png")
            cavalry_blue_4.rect = cavalry_blue_4.image.get_rect()
            cavalry_blue_4.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[4]]
            cavalry_blue_4.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[4]]
            self.hex_fill[self.coor_blue_cavalry[4]] = 'blue_cavalry_4'
            hp_cavalry_blue_4 = font1.render(str(self.hp_cavalry_blue[4]), 1, (0, 0, 255))
            place = hp_cavalry_blue_4.get_rect(center=(self.coor_hexes_x[self.coor_blue_cavalry[4]] + 17, self.coor_hexes_y[self.coor_blue_cavalry[4]]))
            screen.blit(hp_cavalry_blue_4, place)
            stam_cavalry_blue_4 = font1.render(str(self.stam_cavalry_blue[4]), 1, (0, 0, 255))
            place1 = stam_cavalry_blue_4.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_cavalry[4]] + 3, self.coor_hexes_y[self.coor_blue_cavalry[4]] + 10))
            screen.blit(stam_cavalry_blue_4, place1)
            all_sprites.add(cavalry_blue_4)

            cavalry_blue_5 = pygame.sprite.Sprite()
            cavalry_blue_5.image = load_image("cavalry_blue.png")
            cavalry_blue_5.rect = cavalry_blue_5.image.get_rect()
            cavalry_blue_5.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[5]]
            cavalry_blue_5.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[5]]
            self.hex_fill[self.coor_blue_cavalry[5]] = 'blue_cavalry_5'
            hp_cavalry_blue_5 = font1.render(str(self.hp_cavalry_blue[5]), 1, (0, 0, 255))
            place = hp_cavalry_blue_5.get_rect(center=(self.coor_hexes_x[self.coor_blue_cavalry[5]] + 17, self.coor_hexes_y[self.coor_blue_cavalry[5]]))
            screen.blit(hp_cavalry_blue_5, place)
            stam_cavalry_blue_5 = font1.render(str(self.stam_cavalry_blue[5]), 1, (0, 0, 255))
            place1 = stam_cavalry_blue_5.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_cavalry[5]] + 3, self.coor_hexes_y[self.coor_blue_cavalry[5]] + 10))
            screen.blit(stam_cavalry_blue_5, place1)
            all_sprites.add(cavalry_blue_5)

            cavalry_blue_6 = pygame.sprite.Sprite()
            cavalry_blue_6.image = load_image("cavalry_blue.png")
            cavalry_blue_6.rect = cavalry_blue_6.image.get_rect()
            cavalry_blue_6.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[6]]
            cavalry_blue_6.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[6]]
            self.hex_fill[self.coor_blue_cavalry[6]] = 'blue_cavalry_6'
            hp_cavalry_blue_6 = font1.render(str(self.hp_cavalry_blue[6]), 1, (0, 0, 255))
            place = hp_cavalry_blue_6.get_rect(center=(self.coor_hexes_x[self.coor_blue_cavalry[6]] + 17, self.coor_hexes_y[self.coor_blue_cavalry[6]]))
            screen.blit(hp_cavalry_blue_6, place)
            stam_cavalry_blue_6 = font1.render(str(self.stam_cavalry_blue[6]), 1, (0, 0, 255))
            place1 = stam_cavalry_blue_6.get_rect(center=(
                self.coor_hexes_x[self.coor_blue_cavalry[6]] + 3, self.coor_hexes_y[self.coor_blue_cavalry[6]] + 10))
            screen.blit(stam_cavalry_blue_6, place1)
            all_sprites.add(cavalry_blue_6)

            cavalry_red_1 = pygame.sprite.Sprite()
            cavalry_red_1.image = load_image("cavalry_red.png")
            cavalry_red_1.rect = cavalry_red_1.image.get_rect()
            cavalry_red_1.rect.x = self.coor_hexes_x[self.coor_red_cavalry[1]]
            cavalry_red_1.rect.y = self.coor_hexes_y[self.coor_red_cavalry[1]]
            self.hex_fill[self.coor_red_cavalry[1]] = 'red_cavalry_1'
            hp_cavalry_red_1 = font1.render(str(self.hp_cavalry_red[1]), 1, (255, 0, 0))
            place = hp_cavalry_red_1.get_rect(center=(self.coor_hexes_x[self.coor_red_cavalry[1]] + 10, self.coor_hexes_y[self.coor_red_cavalry[1]]))
            screen.blit(hp_cavalry_red_1, place)
            stam_cavalry_red_1 = font1.render(str(self.stam_cavalry_red[1]), 1, (255, 0, 0))
            place1 = stam_cavalry_red_1.get_rect(center=(
                self.coor_hexes_x[self.coor_red_cavalry[1]] + 24, self.coor_hexes_y[self.coor_red_cavalry[1]] + 10))
            screen.blit(stam_cavalry_red_1, place1)
            all_sprites.add(cavalry_red_1)

            cavalry_red_2 = pygame.sprite.Sprite()
            cavalry_red_2.image = load_image("cavalry_red.png")
            cavalry_red_2.rect = cavalry_red_2.image.get_rect()
            cavalry_red_2.rect.x = self.coor_hexes_x[self.coor_red_cavalry[2]]
            cavalry_red_2.rect.y = self.coor_hexes_y[self.coor_red_cavalry[2]]
            self.hex_fill[self.coor_red_cavalry[2]] = 'red_cavalry_2'
            hp_cavalry_red_2 = font1.render(str(self.hp_cavalry_red[2]), 1, (255, 0, 0))
            place = hp_cavalry_red_2.get_rect(center=(self.coor_hexes_x[self.coor_red_cavalry[2]] + 10, self.coor_hexes_y[self.coor_red_cavalry[2]]))
            screen.blit(hp_cavalry_red_2, place)
            stam_cavalry_red_2 = font1.render(str(self.stam_cavalry_red[2]), 1, (255, 0, 0))
            place1 = stam_cavalry_red_2.get_rect(center=(
                self.coor_hexes_x[self.coor_red_cavalry[2]] + 24, self.coor_hexes_y[self.coor_red_cavalry[2]] + 10))
            screen.blit(stam_cavalry_red_2, place1)
            all_sprites.add(cavalry_red_2)

            cavalry_red_3 = pygame.sprite.Sprite()
            cavalry_red_3.image = load_image("cavalry_red.png")
            cavalry_red_3.rect = cavalry_red_3.image.get_rect()
            cavalry_red_3.rect.x = self.coor_hexes_x[self.coor_red_cavalry[3]]
            cavalry_red_3.rect.y = self.coor_hexes_y[self.coor_red_cavalry[3]]
            self.hex_fill[self.coor_red_cavalry[3]] = 'red_cavalry_3'
            hp_cavalry_red_3 = font1.render(str(self.hp_cavalry_red[3]), 1, (255, 0, 0))
            place = hp_cavalry_red_3.get_rect(center=(self.coor_hexes_x[self.coor_red_cavalry[3]] + 10, self.coor_hexes_y[self.coor_red_cavalry[3]]))
            screen.blit(hp_cavalry_red_3, place)
            stam_cavalry_red_3 = font1.render(str(self.stam_cavalry_red[3]), 1, (255, 0, 0))
            place1 = stam_cavalry_red_3.get_rect(center=(
                self.coor_hexes_x[self.coor_red_cavalry[3]] + 24, self.coor_hexes_y[self.coor_red_cavalry[3]] + 10))
            screen.blit(stam_cavalry_red_3, place1)
            all_sprites.add(cavalry_red_3)

            cavalry_red_4 = pygame.sprite.Sprite()
            cavalry_red_4.image = load_image("cavalry_red.png")
            cavalry_red_4.rect = cavalry_red_4.image.get_rect()
            cavalry_red_4.rect.x = self.coor_hexes_x[self.coor_red_cavalry[4]]
            cavalry_red_4.rect.y = self.coor_hexes_y[self.coor_red_cavalry[4]]
            self.hex_fill[self.coor_red_cavalry[4]] = 'red_cavalry_4'
            hp_cavalry_red_4 = font1.render(str(self.hp_cavalry_red[4]), 1, (255, 0, 0))
            place = hp_cavalry_red_4.get_rect(center=(self.coor_hexes_x[self.coor_red_cavalry[4]] + 10, self.coor_hexes_y[self.coor_red_cavalry[4]]))
            screen.blit(hp_cavalry_red_4, place)
            stam_cavalry_red_4 = font1.render(str(self.stam_cavalry_red[4]), 1, (255, 0, 0))
            place1 = stam_cavalry_red_4.get_rect(center=(
                self.coor_hexes_x[self.coor_red_cavalry[4]] + 24, self.coor_hexes_y[self.coor_red_cavalry[4]] + 10))
            screen.blit(stam_cavalry_red_4, place1)
            all_sprites.add(cavalry_red_4)

            cavalry_red_5 = pygame.sprite.Sprite()
            cavalry_red_5.image = load_image("cavalry_red.png")
            cavalry_red_5.rect = cavalry_red_5.image.get_rect()
            cavalry_red_5.rect.x = self.coor_hexes_x[self.coor_red_cavalry[5]]
            cavalry_red_5.rect.y = self.coor_hexes_y[self.coor_red_cavalry[5]]
            self.hex_fill[self.coor_red_cavalry[5]] = 'red_cavalry_5'
            hp_cavalry_red_5 = font1.render(str(self.hp_cavalry_red[5]), 1, (255, 0, 0))
            place = hp_cavalry_red_5.get_rect(center=(self.coor_hexes_x[self.coor_red_cavalry[5]] + 10, self.coor_hexes_y[self.coor_red_cavalry[5]]))
            screen.blit(hp_cavalry_red_5, place)
            stam_cavalry_red_5 = font1.render(str(self.stam_cavalry_red[5]), 1, (255, 0, 0))
            place1 = stam_cavalry_red_5.get_rect(center=(
                self.coor_hexes_x[self.coor_red_cavalry[5]] + 24, self.coor_hexes_y[self.coor_red_cavalry[5]] + 10))
            screen.blit(stam_cavalry_red_5, place1)
            all_sprites.add(cavalry_red_5)

            cavalry_red_6 = pygame.sprite.Sprite()
            cavalry_red_6.image = load_image("cavalry_red.png")
            cavalry_red_6.rect = cavalry_red_6.image.get_rect()
            cavalry_red_6.rect.x = self.coor_hexes_x[self.coor_red_cavalry[6]]
            cavalry_red_6.rect.y = self.coor_hexes_y[self.coor_red_cavalry[6]]
            self.hex_fill[self.coor_red_cavalry[6]] = 'red_cavalry_6'
            hp_cavalry_red_6 = font1.render(str(self.hp_cavalry_red[6]), 1, (255, 0, 0))
            place = hp_cavalry_red_6.get_rect(center=(self.coor_hexes_x[self.coor_red_cavalry[6]] + 10, self.coor_hexes_y[self.coor_red_cavalry[6]]))
            screen.blit(hp_cavalry_red_6, place)
            stam_cavalry_red_6 = font1.render(str(self.stam_cavalry_red[6]), 1, (255, 0, 0))
            place1 = stam_cavalry_red_6.get_rect(center=(
                self.coor_hexes_x[self.coor_red_cavalry[6]] + 24, self.coor_hexes_y[self.coor_red_cavalry[6]] + 10))
            screen.blit(stam_cavalry_red_6, place1)
            all_sprites.add(cavalry_red_6)

            if self.chosen_on:
                if self.chosen_x % 2 == 1:
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y + 20),
                                     (self.width_hex * self.chosen_x // 2 + 10 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 10 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y),
                                     (self.width_hex * self.chosen_x // 2 + 30 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 30 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y),
                                     (self.width_hex * self.chosen_x // 2 + 40 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y + 20), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 40 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y + 20),
                                     (self.width_hex * self.chosen_x // 2 + 30 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y + 40), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 30 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y + 40),
                                     (self.width_hex * self.chosen_x // 2 + 10 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y + 40), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 10 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                      self.height_hex * self.chosen_y + 40),
                                     (self.width_hex * self.chosen_x // 2 + self.chosen_x * 20 // 2 + self.StartPositionX,
                                     self.height_hex * self.chosen_y + 20), 5)
                    if self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1]:
                        self.can_go1 = True
                        if self.can_go2:
                            self.can_go2 = False
                else:
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y +
                                      self.StartPositionY + 40),
                                     (self.width_hex * self.chosen_x // 2 + 10 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y - 20
                                      + self.StartPositionY + 40), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 10 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y - 20
                                      + self.StartPositionY + 40),
                                     (self.width_hex * self.chosen_x // 2 + 30 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y - 20
                                      + self.StartPositionY + 40), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 30 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y - 20
                                      + self.StartPositionY + 40),
                                     (self.width_hex * self.chosen_x // 2 + 40 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y
                                      + self.StartPositionY + 40), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 40 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y
                                      + self.StartPositionY + 40),
                                     (self.width_hex * self.chosen_x // 2 + 30 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y + 20
                                      + self.StartPositionY + 40), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 30 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y + 20
                                      + self.StartPositionY + 40),
                                     (self.width_hex * self.chosen_x // 2 + 10 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y + 20
                                      + self.StartPositionY + 40), 5)
                    pygame.draw.line(screen, colors[3],
                                     (self.width_hex * self.chosen_x // 2 + 10 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y + 20
                                      + self.StartPositionY + 40),
                                     (self.width_hex * self.chosen_x // 2 + self.chosen_x // 2 * 20 + self.StartPositionX, self.height_hex * self.chosen_y
                                      + self.StartPositionY + 40), 5)
                    if self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y]:
                        self.can_go2 = True
                        if self.can_go1:
                            self.can_go1 = False
        else:
            font = pygame.font.Font(None, 72)
            text = font.render('Здесь будут правила.', 1, (0, 0, 0))
            place = text.get_rect(center=(290, 100))
            screen.blit(text, place)
            white_spr = pygame.sprite.Sprite()
            white_spr.image = load_image("white.png")
            white_spr.rect = white_spr.image.get_rect()
            white_spr.rect.x = 0
            white_spr.rect.y = 0
            all_sprites.add(white_spr)
            back_spr = pygame.sprite.Sprite()
            back_spr.image = load_image("back.png")
            back_spr.rect = back_spr.image.get_rect()
            back_spr.rect.x = 0
            back_spr.rect.y = 0
            all_sprites.add(back_spr)

    def get_cell(self, pos):
        coor_x = pos[0]
        coor_y = pos[1]
        return coor_x, coor_y

    def get_click(self, pos):
        cell = self.get_cell(pos)
        if cell:
            self.on_click(cell)

    def on_click(self, cell):
        if cell[0] <= 40 and cell[1] <= 40:
            if not self.show_rules:
                self.show_rules = True
            else:
                self.show_rules = False
        if cell[0] >= 675 and cell[0] <= 725 and cell[1] >= 100 and cell[1] <= 140 and self.show_rules == False:
            if self.can_go1 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_sword[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] = 'blue_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_bow[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_cavalry[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] = 'blue_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_sword[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] = 'red_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_bow[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_cavalry[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 2] = 'red_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_y > 1:
                    self.chosen_y -= 1
                self.can_go1 = False
            elif self.can_go2 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_y > 0:
                            self.coor_blue_sword[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] = 'blue_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_y > 0:
                            self.coor_blue_bow[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_y > 0:
                            self.coor_blue_cavalry[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] = 'blue_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_y > 0:
                            self.coor_red_sword[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] = 'red_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_y > 0:
                            self.coor_red_bow[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_y > 0:
                            self.coor_red_cavalry[index] -= 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 1] = 'red_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] + 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] + 1]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_y > 0:
                    self.chosen_y -= 1
                self.can_go2 = False
        if cell[0] >= 675 and cell[0] <= 725 and cell[1] >= 250 and cell[1] <= 290 and self.show_rules == False:
            if self.can_go1 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_sword[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] = 'blue_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_bow[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_cavalry[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] = 'blue_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_sword[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] = 'red_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_bow[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_cavalry[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y] = 'red_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_y < 13:
                    self.chosen_y += 1
                self.can_go1 = False
            elif self.can_go2 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_y < 11:
                            self.coor_blue_sword[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] = 'blue_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_y < 11:
                            self.coor_blue_bow[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_y < 11:
                            self.coor_blue_cavalry[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] = 'blue_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_y < 11:
                            self.coor_red_sword[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] = 'red_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_y < 11:
                            self.coor_red_bow[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_y < 11:
                            self.coor_red_cavalry[index] += 1
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 1] = 'red_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] - 1]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] - 1]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_y < 11:
                    self.chosen_y += 1
                self.can_go2 = False
        if cell[0] >= 625 and cell[0] <= 665 and cell[1] >= 125 and cell[1] <= 165 and self.show_rules == False:
            if self.can_go1 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_sword[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] = 'blue_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_bow[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_cavalry[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] = 'blue_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_sword[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] = 'red_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_bow[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_cavalry[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 14] = 'red_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_y > 1:
                    self.chosen_x -= 1
                    self.chosen_y -= 2
                self.can_go1 = False
            elif self.can_go2 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_blue_sword[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] = 'blue_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_blue_bow[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_blue_cavalry[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] = 'blue_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_red_sword[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] = 'red_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_red_bow[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_red_cavalry[index] -= 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] = 'red_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] + 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] + 13]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_x > 0 and self.chosen_y >= 0:
                    self.chosen_x -= 1
                    self.chosen_y += 1
                self.can_go2 = False
        if cell[0] >= 725 and cell[0] <= 765 and cell[1] >= 120 and cell[1] <= 165 and self.show_rules == False:
            if self.can_go1 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_sword[index] += 12
                            self.hex_fill[
                                (self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] = 'blue_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_bow[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] = 'blue_bow_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_blue_cavalry[index] += 12
                            self.hex_fill[
                                (self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] = 'blue_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_sword[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] = 'red_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_bow[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_y > 1:
                            self.coor_red_cavalry[index] += 12
                            self.hex_fill[
                                (self.chosen_x // 2) * 25 + 12 + self.chosen_y + 11] = 'red_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_y > 1:
                    self.chosen_x += 1
                    self.chosen_y -= 2
                self.can_go1 = False
            elif self.can_go2 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y >= 0:
                            self.coor_blue_sword[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] = 'blue_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y >= 0:
                            self.coor_blue_bow[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y >= 0:
                            self.coor_blue_cavalry[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] = 'blue_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y >= 0:
                            self.coor_red_sword[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] = 'red_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y >= 0:
                            self.coor_red_bow[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y >= 0:
                            self.coor_red_cavalry[index] += 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 12] = 'red_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] - 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] - 12]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_x < 16 and self.chosen_y >= 0:
                    self.chosen_x += 1
                    self.chosen_y += 1
                self.can_go2 = False
        if cell[0] >= 625 and cell[0] <= 665 and cell[1] >= 225 and cell[1] <= 265 and self.show_rules == False:
            if self.can_go1 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_sword[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] = 'blue_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_bow[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] = 'blue_bow_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_cavalry[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] = 'blue_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_sword[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] = 'red_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_bow[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_cavalry[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 13] = 'red_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_y < 13:
                    self.chosen_x -= 1
                    self.chosen_y -= 1
                self.can_go1 = False
            elif self.can_go2 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_blue_sword[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] = 'blue_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_blue_bow[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_blue_cavalry[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] = 'blue_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_red_sword[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] = 'red_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_red_bow[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_x > 0 and self.chosen_y >= 0:
                            self.coor_red_cavalry[index] -= 12
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 12] = 'red_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] + 12]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] + 12]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_x > 0 and self.chosen_y >= 0:
                    self.chosen_x -= 1
                    self.chosen_y += 2
                self.can_go2 = False
        if cell[0] >= 725 and cell[0] <= 765 and cell[1] >= 225 and cell[1] <= 265 and self.show_rules is False:
            if self.can_go1 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_sword[index] += 13
                            self.hex_fill[
                                (self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] = 'blue_sword_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_bow[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] = 'blue_bow_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_blue_cavalry[index] += 13
                            self.hex_fill[
                                (self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] = 'blue_cavalry_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_sword[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] = 'red_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_bow[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_y < 13:
                            self.coor_red_cavalry[index] += 13
                            self.hex_fill[
                                (self.chosen_x // 2) * 25 + 12 + self.chosen_y + 12] = 'red_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + 12 + self.chosen_y - 1] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_y < 13:
                    self.chosen_x += 1
                    self.chosen_y -= 1
                self.can_go1 = False
            elif self.can_go2 and self.now_move in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y]:
                index = 0
                rs = []
                for el in self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y].split('_'):
                    rs.append(el)
                    if el.isdigit():
                        index = int(el)
                if 'blue' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] == '' and self.stam_sword_blue[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y < 12:
                            self.coor_blue_sword[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] = 'blue_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_sword[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_sword[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_blue[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y - 13] == '' and self.stam_bow_blue[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y < 12:
                            self.coor_blue_bow[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] = 'blue_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_bow[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_bow[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_blue[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] == '' and self.stam_cavalry_blue[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y < 12:
                            self.coor_blue_cavalry[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] = 'blue_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_blue_cavalry[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_blue_cavalry[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_blue[index] -= 1
                elif 'red' in rs:
                    if 'sword' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] == '' and self.stam_sword_red[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y < 12:
                            self.coor_red_sword[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] = 'red_sword_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_sword[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_sword[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_sword_red[index] -= 1
                    elif 'bow' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] == '' and self.stam_bow_red[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y < 12:
                            self.coor_red_bow[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] = 'red_bow_' + str(index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_bow[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_bow[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_bow_red[index] -= 1
                    elif 'cavalry' in rs and self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] == '' and self.stam_cavalry_red[index] > 0:
                        if self.chosen_x < 16 and self.chosen_y < 12:
                            self.coor_red_cavalry[index] += 13
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y + 13] = 'red_cavalry_' + str(
                                index)
                            self.hex_fill[(self.chosen_x // 2) * 25 + self.chosen_y] = ''
                            clearing_spr = pygame.sprite.Sprite()
                            clearing_spr.image = load_image("white_2.png")
                            clearing_spr.rect = clearing_spr.image.get_rect()
                            clearing_spr.rect.x = self.coor_hexes_x[self.coor_red_cavalry[index] - 13]
                            clearing_spr.rect.y = self.coor_hexes_y[self.coor_red_cavalry[index] - 13]
                            all_sprites.add(clearing_spr)
                            self.stam_cavalry_red[index] -= 1
                rs.clear()
                index = 0
                if self.chosen_x < 16 and self.chosen_y < 12:
                    self.chosen_x += 1
                    self.chosen_y += 2
                self.can_go2 = False
        if cell[0] >= 670 and cell[1] >= 170 and cell[0] <= 720 and cell[1] <= 225 and self.show_rules == False:
            print('def')
        if cell[0] >= 625 and cell[0] <= 675 and cell[1] >= 325 and cell[1] <= 375 and  self.show_rules == False:
            print('go')
        if cell[0] >= 725 and cell[0] <= 775 and cell[1] >= 325 and cell[1] <= 375 and  self.show_rules == False:
            if self.now_move == 'blue':
                self.now_move = 'red'
                self.stam_sword_blue = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
                self.stam_bow_blue = [0, 2, 2, 2, 2]
                self.stam_cavalry_blue = [0, 4, 4, 4, 4, 4, 4]
            else:
                self.now_move = 'blue'
                self.stam_cavalry_red = [0, 4, 4, 4, 4, 4, 4]
                self.stam_sword_red = [0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
                self.stam_bow_red = [0, 2, 2, 2, 2]
        if cell[0] >= 40 and cell[0] <= 560 and cell[1] >= 40 and cell[1] <= 560:
            x = (cell[0] - self.StartPositionX) // 10
            y = (cell[1] - self.StartPositionY) // 10
            if (x % 3) > 0 and (x % 3) < 3 and self.show_rules == False:
                if x // 3 % 2 == 1:
                    self.chosen_y = y // 4 + 1
                    self.chosen_on = True
                    self.chosen_x = x // 3
                elif x // 3 % 2 == 0 and cell[1] >= 60 and cell[1] <= 540:
                    self.chosen_y = (y - 2) // 4
                    self.chosen_on = True
                    self.chosen_x = x // 3

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            print(args[0].pos)


pygame.init()
size = width, height = 800, 580
screen = pygame.display.set_mode(size)
field = Field(8, 12)


def load_image(name):
    fullname = os.path.join('', name)
    image = pygame.image.load(fullname)
    return image


all_sprites = pygame.sprite.Group()

run = True
while run:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            field.get_click(ev.pos)
            all_sprites.update(ev)
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_w:
            field.get_click((700, 120))
            all_sprites.update(ev)
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_s:
            field.get_click((700, 270))
            all_sprites.update(ev)
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_q:
            field.get_click((640, 140))
            all_sprites.update(ev)
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_e:
            field.get_click((740, 140))
            all_sprites.update(ev)
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_a:
            field.get_click((640, 240))
            all_sprites.update(ev)
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_d:
            field.get_click((740, 240))
    pygame.display.flip()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    field.render()
pygame.quit()
0
