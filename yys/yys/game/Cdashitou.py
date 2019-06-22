from Cgame import Game
from Chandle import SceneKey
import codedef


class dashitou(Game):
    def __init__(self):
        Game.__init__(self)
        pass

    def judge_scenes(self, argument, handle):
        return Game.judge_scenes(self, argument, handle)

    def do_work(self, argument, handle):
        if self.judge_scenes(argument, handle) == codedef.SCENCE_REPEAT_END:
            return codedef.SCENCE_REPEAT_END
        switcher = {
            SceneKey.NUKOWN: self.da,
            SceneKey.ZHANG_DOU_SHI_BAI: self.fight_end,
            SceneKey.ZHANG_DOU_SHENG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_JIANG_LI: self.fight_end,
            SceneKey.ZHANG_DOU_ZHONG: self.zhunbei,
            SceneKey.XUAN_SHANG_FENG_YING_YAO_QING: self.hon_cha_exit
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        Game.do_work(self, argument, handle)
        return codedef.NORMAL_END

    def zhunbei(self, argument, handle):
        if self.click_img("yys/战斗中准备按钮.bmp", handle, 0.90) == 0:
            print("战斗中准备按钮")
        return codedef.NORMAL_END

    def da(self, argument, handle):
        if self.if_exist("yys/血月.bmp") == 0:
            if self.click_img("yys/挑战石头按钮.bmp", handle, 0.90) == 0:
                print("挑战石头按钮")
                return codedef.FIGHT_BEGIN
            pass
        return codedef.NORMAL_END
