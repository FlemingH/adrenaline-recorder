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
def on_click(x, y, button, pressed):
    if button == Button.left:

        # get window rect every mouse press
        formControl = FormControl()
        formControl.bindActiveWindow()
        formControl.bindWindowByName(win_name = "AMD Software: Adrenalin Edition")

        pos = formControl.toWindowPos(x=x, y=y)
        isWinVisible = formControl.isWinVisible()
        getForegroundWindow = formControl.getForegroundWindow()

        # if click pos in the window bbox
        # if window opend
        # if window focused
        if pos is not None and isWinVisible and getForegroundWindow:
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

def startControlProcess():
    # Collect events until released
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()