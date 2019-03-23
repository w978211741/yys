from Cteam_kun_25 import Team_kun_25
from Cgame import Game, SceneKey

class Team_kun_25_teammate(Team_kun_25):
    def do_work(self, argument, handle):
        switcher = {
            SceneKey.TANG_SUO_ZHANG_JIE: self.team_kun_25_teammate_main,
            SceneKey.TANG_SUO_ZHONG: self.this_da_tang_suo
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, self.father)(argument, handle)
        # Execute the function
        return func

    def father(self, argument, handle):
        Team_kun_25.do_work(self, argument, handle)
        return 0

    def this_da_tang_suo(self, argument, handle):
        if self.da_tang_suo(handle) != -1:
            pass
        return 0

    def team_kun_25_teammate_main(self, argument, handle):
        pass
        return 0

