from enum import Enum, unique


@unique
class SceneKey(Enum):
    NUKOWN = 0
    TING_YUAN = 1
    TANG_SUO = 2
    DING_ZHONG = 3
    JIE_JIE_TU_PO = 4
    ZHANG_DOU_ZHONG = 5
    ZHANG_DOU_JIANG_LI = 6
    ZHANG_DOU_SHENG_LI = 7
    ZHANG_DOU_SHI_BAI = 8
    XIE_ZHAN_DUI_WU = 9
    DOU_JI = 10
    DOU_JI_ZHUN_BEI =11
    DOU_JI_ZHONG = 12
    GOU_MAI_TI_LI = 13
    XUAN_SHANG_FENG_YING_YAO_QING = 14
    TANG_SUO_ZHONG = 15
    MO_REN_YAOQ_QING_DUI_YOU = 16
    TANG_SUO_ZHANG_JIE = 17
    SHI_FOU_YAO_QING_JI_XU = 18
    ZU_DUI_XUAN_ZE_DUI_YOU = 19
    SHOU_DAO_YAO_QING = 20
    CHAO_GUI_WANG_LAI_XI = 21
    GOU_MAI_CHA = 22
    ZHAO_HUAN = 23
    CHOU_N_KA = 24
    BAI_GUI_YE_XING = 25
    BAI_GUI_QI_YUE_SHU = 26
    BAI_GUI_ZHONG = 27
    BAI_GUI_GUI_WANG = 28
    TU_YAO = 29
    FENG_MO_ZHI_SHI = 30
    GE_REN_SHE_ZHI = 31
    XUAN_QU = 32
    YOU_XIANG_DENG_LU = 33
    XUAN_ZHE_PING_TAI = 34
    YOU_XI_GONG_GAO = 35

    # 日轮之城
    LUN_HUI_MI_JING = 36    # 轮回秘境界面
    DA_GUAI_KAI_SHI = 37    # 打怪开始界面
    XUAN_ZI_YUAN = 38       # 过关后选资源


class Handle:
    hwnd = 0
    left = 0
    top = 0
    right = 0
    bottom = 0
    old_scene = SceneKey.NUKOWN
    iold_scene = 0
