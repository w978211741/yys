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

class Handle:
    hwnd = 0
    left = 0
    top = 0
    right = 0
    bottom = 0
    old_scene = SceneKey.NUKOWN
    iold_scene = 0
