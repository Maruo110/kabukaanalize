
from enum import Enum

class KbnRousoku(Enum):

    SMALL_YOUSEN = 1
    SMALL_INSEN = 2
    BIB_YOUSEN = 3
    BIG_INSEN = 4
    UWAKAGE_YOUSEN = 5
    UWAKAGE_INSEN = 6
    SITAKAGE_YOUSEN = 7
    SITAKAGE_INSEN = 8
    YORIHIKI_DOUJISEN = 9

    def __init__(self, params):
        '''
        Constructor
        '''
