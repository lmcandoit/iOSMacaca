#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'mengdegong'

import random
from Data_.MonkeyConfig import *

class random_math():
    def __init__(self):
        self.EVENT_TYPE_CELL = Cell
        self.EVENT_TYPE_BUTTON = Button
        self.EVENT_TYPE_BACK = BACK
        self.EVENT_TYPE_Image = Image
        self.EVENT_TYPE_TextView = TextView
        self.EVENT_TYPE_Key = Key
        self.EVENT_TYPE_Switch = Switch
        self.EVENT_TYPE_drag=Drag
        self.EVENT_TYPE_click= TAP
        self.EVENT_TYPE_HOME = HOME
        self.EVENT_TYPE_Header = Header
        self.EVENT_TYPE_Body = Body
        self.EVENT_TYPE_Table = Table


    def percentage_random(self):
        random_number = random.random()

        if random_number >= 0 and random_number <= self.EVENT_TYPE_Header:
            return 11
        elif random_number >= self.EVENT_TYPE_Header and random_number <= self.EVENT_TYPE_Header + self.EVENT_TYPE_Body:
            return 12
        elif self.EVENT_TYPE_Header + self.EVENT_TYPE_Body<=random_number<=self.EVENT_TYPE_Header + self.EVENT_TYPE_Body+self.EVENT_TYPE_Table:
            return 13
        elif self.EVENT_TYPE_Header + self.EVENT_TYPE_Body+self.EVENT_TYPE_Table<=random_number<=self.EVENT_TYPE_Header + self.EVENT_TYPE_Body+self.EVENT_TYPE_Table+self.EVENT_TYPE_BACK:
            return 14
        elif self.EVENT_TYPE_Header + self.EVENT_TYPE_Body+self.EVENT_TYPE_Table+self.EVENT_TYPE_BACK<=random_number<=self.EVENT_TYPE_Header + self.EVENT_TYPE_Body+self.EVENT_TYPE_Table+self.EVENT_TYPE_BACK+self.EVENT_TYPE_drag:
            return 15
        return -1





        # if random_number >= 0 and random_number <= self.EVENT_TYPE_CELL:
        #     return 0
        # elif random_number >= self.EVENT_TYPE_CELL and random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON:
        #     return 1
        # elif self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON <= random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK:
        #     return 2
        # elif self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK <= random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image:
        #     return 3
        # elif self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image <= random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image \
        #         + self.EVENT_TYPE_TextView:
        #     return 4
        # elif self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image + self.EVENT_TYPE_TextView <= random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image \
        #         + self.EVENT_TYPE_TextView + self.EVENT_TYPE_Key:
        #     return 5
        # elif self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image + self.EVENT_TYPE_TextView \
        #         + self.EVENT_TYPE_Key <= random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image \
        #                 + self.EVENT_TYPE_TextView + self.EVENT_TYPE_Key + self.EVENT_TYPE_Switch:
        #     return 6
        # elif self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image + self.EVENT_TYPE_TextView \
        #         + self.EVENT_TYPE_Key + self.EVENT_TYPE_Switch <= random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image \
        #                 + self.EVENT_TYPE_TextView + self.EVENT_TYPE_Key + self.EVENT_TYPE_Switch + self.EVENT_TYPE_HOME:
        #     return 7
        # elif self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image + self.EVENT_TYPE_TextView \
        #         + self.EVENT_TYPE_Key + self.EVENT_TYPE_Switch+ self.EVENT_TYPE_HOME <= random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image \
        #                 + self.EVENT_TYPE_TextView + self.EVENT_TYPE_Key + self.EVENT_TYPE_Switch + self.EVENT_TYPE_HOME + self.EVENT_TYPE_drag:
        #     return 8
        # elif self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image + self.EVENT_TYPE_TextView \
        #         + self.EVENT_TYPE_Key + self.EVENT_TYPE_Switch+ self.EVENT_TYPE_HOME+ self.EVENT_TYPE_drag <= random_number <= self.EVENT_TYPE_CELL + self.EVENT_TYPE_BUTTON + self.EVENT_TYPE_BACK + self.EVENT_TYPE_Image \
        #                 + self.EVENT_TYPE_TextView + self.EVENT_TYPE_Key + self.EVENT_TYPE_Switch + self.EVENT_TYPE_HOME + self.EVENT_TYPE_drag+ self.EVENT_TYPE_click:
        #     return 9
        # return -1
