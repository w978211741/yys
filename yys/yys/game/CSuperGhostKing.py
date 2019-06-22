from Cteam_kun_25 import Team_kun_25
from Cgame import Game
from Chandle import SceneKey
from Cimg import Img
from Cmouse import Mouse
from CfightUp import FightUp
import sys
import time
import codedef
from win32api import GetSystemMetrics
from Cgouliang import Gouliang


class SuperGhostKing(Game):

    def __init__(self):
        super(Game, self).__init__()
        pass

    # 重置庭院位置，进町中再回庭院，这样能更好找到探索按钮
    def reset_ting_yuan(self, handle):
        self.click_img("yys/町中.bmp", handle)
        time.sleep(1)
        self.click_img("yys/庭院.bmp", handle)





