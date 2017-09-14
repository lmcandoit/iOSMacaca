# -*- coding: utf-8 -*-

import random
import unittest
import time
from macaca import WebDriver
from requests import HTTPError
from Data_.MonkeyConfig import *
from Utils import utils
from Utils.Random import *


class MacacaTest(unittest.TestCase):

    desired_caps = {}
    desired_caps['platformName'] = 'iOS'
    desired_caps['platformVersion'] = '10.2'
    desired_caps['bundleId'] = 'com.meituan.message'
    desired_caps['udid'] = 'f513b9a31115988abc792cd53266a54d6e512197'

    server_url = {
        'hostname': '127.0.0.1',
        'port': 3456
    }

    def setUp(self):
        utils.log(str(self.desired_caps))
        utils.log(str(self.server_url))
        self.driver = WebDriver(self.desired_caps, self.server_url)
        self.driver.init()


    def tearDown(self):
        self.driver.quit()

    def test_get_url(self):
        time.sleep(6)
        Rect_Phone = self.driver.get_window_size()
        Height = Rect_Phone['height']
        width = Rect_Phone['width']
        Clikc_RECT = self.driver.element_by_class_name('XCUIElementTypeTable').rect
        utils.log(str(Clikc_RECT))
        limit_Height_up = Clikc_RECT.get('y')
        limit_Height_down = Clikc_RECT.get('height')
        back_int=0
        while True:
            back_int+=1
            utils.log('[ RUN ] Event number:  ' +str(back_int))
            # if back_int>10:
            #    Type='back'
            #    utils.log('Every 10 time,back need do one time')
            # else:
            #     if self.driver.element_if_exists('id','确认拨打网络电话？'):
            #         Type_call = random.randint(1,2)
            #         if Type_call==1:
            #             utils.click_by_id(self.driver,'取消')
            #         else:
            #             utils.click_by_id(self.driver, '继续')
            #     elif self.driver.element_if_exists('id','正在等待对方接受邀请...'):
            #         utils.click_by_id(self.driver, 'icon call hangUp')
            #     elif self.driver.element_if_exists('id','CameraMode'):
            #         utils.click_by_id(self.driver,'取消')
            #     elif self.driver.element_if_exists('id','按住录'):
            #         utils.click_by_id(self.driver,'返回')
            #     elif not self.driver.element_if_exists('id','工作台') and self.driver.element_if_exists('id','消息'):
            #         utils.click_by_id(self.driver,'消息')
            #     Type = random.choice(['Cell','Button','Image','TextView','Key','Switch','Cell','Button','Cell','Button','Button','Button','Button','click','click','drag','back'])
            Type =random_math().percentage_random()

            if Type==9:
                self.click_x_y(limit_Height_up,limit_Height_down,width)
            elif Type==8:
                self.drag(width,Height)
            elif Type == 2:
                self.back()
            elif Type == 7:
                utils.log('Home')
            elif Type == 0:
                self.click_by_class('XCUIElementTypeCell')
            elif Type == 1:
                self.click_by_class2('XCUIElementTypeButton')
            elif Type == 3:
                self.click_by_class('XCUIElementTypeImage')
            elif Type == 4:
                self.click_by_class('XCUIElementTypeStaticText')
            elif Type == 6:
                self.click_by_class('XCUIElementTypeSwitch')
            elif Type == 5:
                self.click_by_class('XCUIElementTypeKey')
            elif Type == 11:
                self.Tap(20,64)
            elif Type == 12:
                self.Tap(64,519)
            elif Type == 13:
                self.Tap(519,568)
            elif Type == 14:
                self.back()
            elif Type == 15:
                self.drag(width,Height)


    def Tap(self,up,down):
        y = random.randint(up, down)
        x = random.randint(0, 320)
        utils.log('click point:'+str(x)+','+str(y))
        self.driver.touch('tap', {'x': x, 'y': y})

    def click_by_class(self,ClassName):
        try:
            Elements = self.driver.elements_by_class_name(ClassName)
            length = len(Elements)
            if length >0:
                index = random.randint(1, length) - 1

                if Elements[index].rect.get('y') >= 455:
                    utils.log('element class:'+ClassName+' index:'+str(index)+' is invisible,rect:'+str(Elements[index].rect))
                elif Elements[index].rect.get('y')==0:
                    utils.log('element class:' + ClassName + ' index:' + str(index) + ' is invisible,rect:'+str(Elements[index].rect))
                else:
                    utils.click_by_class_index(self.driver, ClassName, index)
            else:
                utils.log('Key:'+ClassName+' can\'t get elements')
        except HTTPError as HT:
            utils.log('except:'+str(HT))

    def click_by_class2(self,ClassName):
        try:
            Elements = self.driver.elements_by_class_name(ClassName)
            length = len(Elements)
            if length >0:
                index = random.randint(1, length) - 1

                if Elements[index].rect.get('y')==0:
                    utils.log('element class:' + ClassName + ' index:' + str(index) + ' is invisible,rect:'+str(Elements[index].rect))
                else:
                    utils.click_by_class_index(self.driver, ClassName, index)
            else:
                utils.log('Key:'+ClassName+' can\'t get elements')
        except HTTPError as HT:
            utils.log('except:'+str(HT))

    def change_Tab(self):
        Type = random.randint(1, 4)
        if Type==1:
            utils.click_by_id(self.driver,'通讯录')
        elif Type==2:
            utils.click_by_id(self.driver,'工作台')
        elif Type==3:
            utils.click_by_id(self.driver,'我的')
        elif Type==4:
            utils.click_by_id(self.driver,'消息')

    def back(self):
        utils.click_by_id(self.driver, 'btn navigationBar back')
        utils.click_by_id(self.driver, '取消')
        utils.click_by_id(self.driver, '返回')


    def click_x_y(self,limit_Height_up,limit_Height_down,width):
        y = random.randint(limit_Height_up, limit_Height_down)
        x = random.randint(0, width)
        print(x)
        print(y)
        self.driver.touch('tap', {'x': x, 'y': y})

    def drag(self,width,Height):
        Type =random.randint(1,2)
        utils.log('drag')
        if Type==1:
            self.driver.touch('drag', {
                'fromX': width / 2,
                'fromY': Height / 4 * 3,
                'toX': width / 2,
                'toY': Height / 4 * 2,
                'duration': 10
            })
        else:
            self.driver.touch('drag', {
                'fromX': width / 2,
                'fromY': Height / 4 * 2,
                'toX': width / 2,
                'toY': Height / 4 * 3,
                'duration': 10
            })

if __name__ == '__main__':
    unittest.main()