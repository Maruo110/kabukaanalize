
from enum import Enum

class KbnSakataGohou(Enum):

    BLANK = 0

    # 出会い線（買い）
    BUY_DEAISEN = 1
    # 切り込み線（買い）
    BUY_KIRIKOMISEN = 2
    # はらみ線（買い）
    BUY_HARAMISEN = 3
    # たすき線（買い）
    BUY_TASUKISEN = 4
    # 振り分け線（買い）
    BUY_HURIWAKESEN = 5
    # つつみ線（買い）
    BUY_TUTUMISEN = 6
    # 赤三兵（買い）
    BUY_AKASANPEI = 7
    # 三川明けの明星（買い）（さんせんあけのみょうじょう）
    BUY_SANSENAKENOMYOUJYOU = 8

    # かぶせ線（売り）
    SELL_KABURISEN  = 9
    # はらみ線（売り）
    SELL_HARAMISEN = 10
    # 出会い線（売り）
    SELL_DEAISEN = 11
    # つつみ線（売り）
    SELL_TUTUMISEN = 12
    # たすき線（売り）
    SELL_TASUKISEN = 13
    # 振り分け線（売り）
    SELL_HURIWAKESEN = 14
    # 三羽烏（売り）（さんばがらす）
    SELL_SANBAGARASU = 15
    # 三川宵の明星（売り）
    SELL_SANSENYOINOMYOUJYOU = 16

    def __init__(self, params):
        '''
        Constructor
        '''
