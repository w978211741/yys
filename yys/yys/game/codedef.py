# 返回值为0 正常结束，小于0是错误，大于0是延时
NORMAL_END = 0          # 正常结束
ERROR_END = -1          # 错误结束
FIGHT_END = -11          # 战斗结束
FIGHT_BEGIN = -4        # 战斗开始
NOT_ENOUGH_POWER = -3    # 体力不足
YAO_QING_DUI_YOU_JI_XU = -5 #邀请队友继续

SCENCE_NOT_REPEAT = -41     # 场景未重复
SCENCE_REPEAT_END = -42     # 场景重复，且超次数，退出
SCENCE_REPEAT = -43         # 场景重复，计数加1

# 打探索
TANG_CAN_EXIT = -50         # 打完识别到探索奖励，次数可退出
TANG_GO_RIGHT = -51         # 探索中，向右走
TANG_GO_RIGHT_MAX = 5      # 探索中，向右走最大值，到达后退出探索

# 次数定义
SCENCE_REPEAT_TIMES = 15    # 识别到场景重复次数

# UP BGR
UP_COIN = [112, 200, 217]
UP_EXP = [163, 203, 223]
UP_REWARD = [35, 45, 213]

# UP 选项
UP_C_NULL = 0
UP_C_COIN = 1
UP_C_EXP = 2
UP_C_REWARD = 3

# UP 对应界面中文
UP_Z_NULL = '不挑'
UP_Z_COIN = '金币'
UP_Z_EXP = '经验'
UP_Z_REWARD = '奖励'

# BOSS 对应界面中文
BOSS_TRUE = '打BOSS'
BOSS_FALSE = '不打BOSS'

# mod
MOD_SET = 0
MOD_JIE = 1
MOD_XUE = 2
MOD_TANG = 3
MOD_YU = 4
MOD_DOU = 5