import time
from macaca import WebDriverException
from requests import HTTPError

import Data_.common as common


def click_by_id(drvier,id):
    try:
        if drvier.element_if_exists('id',id):
            log('click Element by id:'+id)
            drvier.element('id',id).click()
        else:
            log('Type:id ,can\'t get element,Please check ID value:'+id)
    except WebDriverException as Exception:
        log("Exception:"+str(Exception))
    except HTTPError as HT:
        log('except:' + str(HT))

def click_by_xpath(drvier,xpath):
    try:
        if drvier.element_if_exists('xpath',xpath):
            log('click Element by xpath:'+xpath)
            drvier.element('xpath',id).click()
        else:
            log('Type:xpath ,can\'t get element,Please check xpath value:'+xpath)
    except WebDriverException as Exception:
        log("Exception:"+str(Exception))
    except HTTPError as HT:
        log('except:' + str(HT))

def click_by_Name_index(driver,name,index):
    try:
        Elements = driver.elements_by_name(name)
        if len(Elements) >=index+1:
            if Elements[index].rect.get('y')==0 and Elements[index].rect.get('x')==0:
                log('element Name:' + name + ' index:' + str(index) + ' is invisible,rect:'+str(Elements[index].rect))
            else:
                log('click Element by Name:' + name + ',index:' + str(index))
                Elements[index].click()
        else:
            log('Can\'t get element by Name:'+name+',index:'+str(index))
    except WebDriverException as Exception:
        log('Exception:'+str(Exception))
    except HTTPError as HT:
        log('except:' + str(HT))

def click_by_Name(driver,name):
    try:
        if driver.element_if_exists('name',name):
            log('click Element by Name:' + name)
            driver.element('name',name).click()
        else:
            log('Type:Name ,can\'t get element,Please check Name value:' + name)
    except WebDriverException as Exception:
        log('Exception:'+str(Exception))
    except HTTPError as HT:
        log('except:' + str(HT))

def click_by_class_index(driver,className,index):
    try:
        Elements = driver.elements_by_class_name(className)
        if len(Elements)>=index+1:
            if Elements[index].rect.get('y')==0 and Elements[index].rect.get('x')==0:
                log('element class:' + className + ' index:' + str(index) + ' is invisible,rect:'+str(Elements[index].rect))
            else:
                log('click Element by ClassName:' + className + ',index:' + str(index))
                Elements[index].click()
        else:
            log('Can\'t get element by ClassName:' + className + ',index:' + str(index))
    except WebDriverException as Exception:
        log('Exception:'+str(Exception))
    except HTTPError as HT:
        log('except:' + str(HT))

def log(Keyword):
    print(Keyword)
    path = common.log_adress
    fw = open(path, 'a')
    content = str(getTime())+":"+Keyword + '\n'
    fw.write(content)
    fw.close()

def getTime():
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())

def drag(driver,Type):
    log('Drag '+Type)
    if Type=='UP':
        driver.touch('drag', {
            'fromX': common.width / 2,
            'fromY': common.Height / 4 * 3,
            'toX': common.width / 2,
            'toY': common.Height / 4 * 2,
            'duration': 10
        })
    elif Type=='DOWN':
        driver.touch('drag', {
            'fromX': common.width / 2,
            'fromY': common.Height / 4 * 2,
            'toX': common.width / 2,
            'toY': common.Height / 4 * 3,
            'duration': 10
        })
    elif Type=='LEFT':
        driver.touch('drag', {
            'fromX': common.width / 3*2,
            'fromY': common.Height / 2 ,
            'toX': common.width / 3,
            'toY': common.Height / 2,
            'duration': 10
        })
    elif Type=='RIGHT':
        driver.touch('drag', {
            'fromX': common.width / 3,
            'fromY': common.Height / 2,
            'toX': common.width / 3*2,
            'toY': common.Height /2,
            'duration': 10
        })