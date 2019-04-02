from Cteam_kun_25 import Team_kun_25
from Cgame import Game, SceneKey

class Team_kun_25_teammate(Team_kun_25):
    def do_work(self, argument, handle):
        switcher = {
            SceneKey.TANG_SUO_ZHANG_JIE: self.team_kun_25_teammate_main,
            SceneKey.TANG_SUO_ZHONG: self.this_da_tang_suo,
            SceneKey.SHOU_DAO_YAO_QING: self.shou_dao_yai_qing
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        return Team_kun_25.do_work(self, argument, handle)

    def this_da_tang_suo(self, argument, handle):
        if self.da_tang_suo(handle) != -1:
            pass
        return 0

    def team_kun_25_teammate_main(self, argument, handle):
        pass
        return 0

    def shou_dao_yai_qing(self, argument, handle):
        ti_li = self.get_ti_li(handle)
        print(ti_li)
        if ti_li < 24:
            return -3
        if self.click_img("yys/接受邀请按钮.bmp", handle, 0.90) == 0:
            print("接受邀请按钮")
            return 0
        return 0

