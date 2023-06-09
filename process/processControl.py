# https://blog.csdn.net/hskjshs/article/details/113521216
from pynput.mouse import Listener,Button

from uiControl import FormControl

# 监听鼠标移动事件，将鼠标的位置打印出来
# on_move（x，y）是鼠标移动时回调的函数两个参数x，y描述的是鼠标的位置
def on_move(x, y):
    pass
    # print('mouse move to {0}'.format((x, y)))

# 监听鼠标按键
# on_click(x, y, button, pressed)是鼠标点击时回调的函数
# 四个参数x，y，button，pressed。
# x，y描述的是鼠标点击的位置
# button是鼠标的按键，值有三种Button.left(左键)、Button.right（右键）、Button.middle（中键）
# 注意鼠标button使用按下一次会有两次反馈（按下和松开）。想要使用一次可以把一个if pressed:语句放在它的外层
# pressed的值是bool类型是鼠标按键的按下时是True，松开时为False。

if_start_ocr_ = None
if_window_open_focus_ = None
mouse_click_pos_ = None
def on_click(x, y, button, pressed):
    if button == Button.left:

        # get window rect every mouse press
        formControl = FormControl()
        formControl.bindActiveWindow()
        formControl.bindWindowByName(win_name = "AMD Software: Adrenalin Edition")

        pos = formControl.toWindowPos(x=x, y=y)
        getWinRect = formControl.getWinRect()

        # if click pos in the window bbox
        # if window opend
        # if window focused
        # if mouse pressed not released
        if pos is not None and if_window_open_focus_.value == 1 and pressed:

            # send mouse click pos to ocr
            global mouse_click_pos_
            mouse_click_pos_['x'] = x
            mouse_click_pos_['y'] = y

            # call cnocr to do text recognition
            global if_start_ocr_
            if_start_ocr_.value = 1

            print(getWinRect.left, getWinRect.top, getWinRect.right, getWinRect.bottom)
            print(x, y)
            print(pos.x, pos.y, "\n")

    elif button == Button.right:
        print('{0}position{1}'.format('right press'if pressed else 'right release',(x, y)))
    elif button == Button.middle:  # 停止监听
        return False
    
# 滑轮滚动事件
# x，y指针位置
# dx，dy滚轮的动作方向
def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format((x, y)))
    print(dx, dy)

def startControlProcess(if_start_ocr, if_window_open_focus, mouse_click_pos):
    
    # Collect events until released
    global if_start_ocr_
    global if_window_open_focus_
    global mouse_click_pos_

    if_start_ocr_ = if_start_ocr
    if_window_open_focus_ = if_window_open_focus
    mouse_click_pos_ = mouse_click_pos

    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()