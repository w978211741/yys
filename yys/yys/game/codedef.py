# 返回值为0 正常结束，小于0是错误，大于0是延时
NORMAL_END = 0          # 正常结束
ERROR_END = -1          # 错误结束
FIGHT_END = -11          # 战斗结束
FIGHT_BEGIN = -4        # 战斗开始
NOT_ENOUGH_POWER = -3    # 体力不足
YAO_QING_DUI_YOU_JI_XU = -5 #邀请队友继续
ZAI_TANG_SUO = -6       # 队员 在探索界面
BEGIN_DA_GUAI = -21       # 开打小怪
BEGIN_DA_BOSS = -22       # 开打boss
EXIT_TANG_SUO = -23       # 退出探索

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

# 晴明是否满级 对应界面中文
QING_MAX_TRUE = '晴明满级'
QING_MAX_FALSE = '晴明没满级'

# 队长是否打手 对应界面中文
C_BEAT_TRUE = '队长打手'
C_BEAT_FALSE = '队员打手'

# 打手是否打满级 对应界面中文
BEAT_MAX_TRUE = '打手满级'
BEAT_MAX_FALSE = '打手没满级'

# 是否交叉打结界
LOOP_TRUE = '不交叉打'
LOOP_FALSE = '交叉打结界'

# mod
MOD_SET = 0
MOD_JIE = 1
MOD_XUE = 2
MOD_TANG = 3
MOD_YU = 4
MOD_DOU = 5

# n 卡分块
n_top = 0.7
n_left = 0.14
n_bottom = 0.92
n_right = 0.72

# 队员 左边式神
left_top = 0.42
left_left = 0.12
left_bottom = 0.6
left_right = 0.22

# 队员 中间式神
mid_top = 0.42
mid_left = 0.45
mid_bottom = 0.6
mid_right = 0.55

# 队员 右边式神
right_top = 0.42
right_left = 0.78
right_bottom = 0.6
right_right = 0.88

# 队长 左边式神
left_top_c = 0.42
left_left_c = 0.22
left_bottom_c = 0.6
left_right_c = 0.32

# 队长 右边式神
right_top_c = 0.42
right_left_c = 0.68
right_bottom_c = 0.6
right_right_c = 0.78
