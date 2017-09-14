# -*- coding: utf-8 -*-

import random
import unittest
import time
from macaca import WebDriver

import Data_.common as common
from Utils import utils

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

    add_xpath = '//XCUIElementTypeApplication[@name="大象Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton[3]'
    input_xpath = 'xpath	//XCUIElementTypeApplication[@name="大象Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton[3]'
    pic_select = '(//XCUIElementTypeButton[@name="preview pic unchoosed"])[45]'
    pic = '//XCUIElementTypeApplication[@name="大象Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeCollectionView/XCUIElementTypeCell[1]'
    pic_send = '发送'
    emoji_self = '//XCUIElementTypeApplication[@name="大象Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton[2]'
    mt = 'mt'

    def setUp(self):
        self.driver = WebDriver(self.desired_caps, self.server_url)
        self.driver.init()
        Rect_Phone = self.driver.get_window_size()
        common.Height = Rect_Phone['height']
        common.width = Rect_Phone['width']

    def tearDown(self):
        self.driver.quit()

    def test_get_url(self):
        time.sleep(6)

        # utils.click_by_id(self.driver,'工作台')
        # utils.click_by_id(self.driver, '消息')
        #time.sleep(2)
        #utils.click_by_class_index(self.driver,'XCUIElementTypeCell',2)
        print(common.Height)
        print(common.width)

        utils.log('50,530')
        self.driver.touch('tap', {'x': 250, 'y': 530})
        time.sleep(5)

        # Els =self.driver.elements_by_class_name('XCUIElementTypeCell')
        # if len(Els)>10:
        #     #if self.driver.
        #     print('click')
        #     Els[9].click()
        # self.driver.alert_text()
        # assert self.driver.is_displayed()

        # utils.drag(self.driver,'UP')
        # utils.drag(self.driver,'UP')
        # utils.drag(self.driver,'DOWN')
        # utils.drag(self.driver,'DOWN')

        # self.driver.element('id','开启二维码群').click()
        # time.sleep(1)
        # self.driver.element_by_id('输入消息...').click()
        # Input = self.driver.element('xpath','//XCUIElementTypeApplication[@name="大象Dev"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextView')
        # Input.send_keys('ceshi')
        # self.driver.send_keys('\n')

        # self.driver.touch('tap', {'x': 255, 'y': 522})
        # self.driver.touch('tap', {'x': 255, 'y': 522})

    def click_x_y(self,Height,width):
        y = random.randint(15, Height*2)
        x = random.randint(0, width*2)
        print(x)
        print(y)
        self.driver.touch('tap', {'x': x, 'y': y})

    def drag(self,width,Height):
        Type =random.randint(1,2)
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