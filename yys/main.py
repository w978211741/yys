#encoding=utf-8
from Cgame import Game, SceneKey
from Chandle import Handle
import time
from yys.game.Cliaojiejie import Liaojiejie
from yys.game.Cteam_kun_25_captain import Team_kun_25_captain
from yys.game.Cteam_kun_25_teammate import Team_kun_25_teammate
from yys.game.Cpersonal_jiejie import Personal_jiejie
from yys.game.Cteam_hun_10 import Team_hun_10
from MainWindow import My_MainWindow
from PyQt5 import QtWidgets
import sys


def da_liao_jie_jie():
    game = Liaojiejie()
    yys1 = Handle()
    #set_yys(2, game, yys1)
    index = 1
    flag = True
    old_f = flag
    while 1:
        index = index + 1
        if index > 5500:
            return
        if flag != old_f:
            old_f = flag
            time.sleep(10)
        if flag:
            scene = game.get_scene(yys1)
            print(scene)
            re = game.do_work(scene, yys1)
            if re == 0:
                print("0：完成")
                time.sleep(1)
            elif re == 1:
                print("1：无法判断是在个人还是寮突破（右侧按钮无法识别）")
                flag = False
            elif re == 2:
                print("2：会长未选择寮进行突破")
                flag = False
            elif re == 3:
                print("3：次数已经用完（十分钟回复一次，最高存储6次）")
                flag = False
            elif re == 4:
                print("4：分块后找不到没打过的（理应不出现，因为是先识别出没打过的数量之后才会调用到的）")
                flag = False
            time.sleep(1)
        else:
            scene = game.get_scene(yys1)
            print(scene)
            re = game.do_work(scene, yys1)
            if re == 0:
                print("0：完成")
                time.sleep(1)
            elif re == 1:
                print("1：打完三个冷却中")
                flag = True
            elif re == 2:
                print("2：分块后找不到没打过的（理应不出现，因为是先识别出没打过的数量之后才会调用到的）")
                flag = True
            time.sleep(1)


if __name__ == "__main__":
    print("开始")
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = My_MainWindow()
    my_pyqt_form.show()
    sys.exit(app.exec_())