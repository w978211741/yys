from Cteam_kun_25 import Team_kun_25
from Chandle import SceneKey
from Cgame import Game
from Chandle import SceneKey
import codedef


class Team_kun_25_teammate(Team_kun_25):
    def __init__(self):
        super(Team_kun_25, self).__init__()

    def judge_scenes(self, argument, handle):
        return Game.judge_scenes(self, argument, handle)

    def do_work(self, argument, handle):
        if self.judge_scenes(argument, handle) == codedef.SCENCE_REPEAT_END:
            return codedef.SCENCE_REPEAT_END
        switcher = {
            SceneKey.TANG_SUO_ZHONG: self.this_da_tang_suo,
            SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yai_qing
        }
        func = switcher.get(argument, self.father)(argument, handle)
        return func

    def father(self, argument, handle):
        return Team_kun_25.do_work(self, argument, handle)

    def shou_dao_yai_qing(self, argument, handle):
        if self.click_img("yys/接受邀请按钮.bmp", handle, 0.90) == 0:
            print("接受邀请按钮")
            return 0
        return 0

    def this_da_tang_suo(self, argument, handle):
        return codedef.NORMAL_END

