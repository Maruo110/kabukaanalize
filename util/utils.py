# -*- coding: utf-8 -*-
from numpy import float

def getInsertValues(rowinfo):
    resultvalue = ''
    ctr = 0

    for list in rowinfo:
        if ctr > 0:
            resultvalue = resultvalue + ", "
            resultvalue = resultvalue + list
        else:
            resultvalue = resultvalue + "'" + list + "'"
        ctr = ctr + 1
    return resultvalue

def getRousokuasiKbn(rowinfo):
    from kbn import kbn_rousoku

    openprice = float(rowinfo[1])
    highprice = float(rowinfo[2])
    lowprice = float(rowinfo[3])
    closingprice = float(rowinfo[4])

    openclosingrate = abs(closingprice / openprice)
    resultvalue = 0

    if openclosingrate == 0.0:
        resultvalue = kbn_rousoku.KbnRousoku.YORIHIKI_DOUJISEN

    elif openprice < closingprice:

        if (closingprice < highprice) and (highprice - closingprice) > (openprice - lowprice):
            # 上影陽線
            resultvalue = kbn_rousoku.KbnRousoku.UWAKAGE_YOUSEN
        else:
            if (lowprice < openprice) and (openprice - lowprice) > (highprice - closingprice):
                # 下影陽線
                resultvalue = kbn_rousoku.KbnRousoku.SITAKAGE_YOUSEN
            else:
                if openclosingrate < 0.1:
                    # 小陽線
                    resultvalue = kbn_rousoku.KbnRousoku.BIB_YOUSEN
                else:
                    # 大陽線
                    resultvalue = kbn_rousoku.KbnRousoku.BIB_YOUSEN
    else:
        if openprice < highprice and (highprice - openprice) > (closingprice - lowprice):
            # 上影陰線
            resultvalue = kbn_rousoku.KbnRousoku.UWAKAGE_INSEN
        else:
            if lowprice < closingprice and (closingprice - lowprice) > (highprice - openprice):
                # 下影陰線
                resultvalue = kbn_rousoku.KbnRousoku.SITAKAGE_INSEN
            else:
                if openclosingrate < 0.1:
                    # 小陰線
                    resultvalue = kbn_rousoku.KbnRousoku.SMALL_INSEN
                else:
                    # 大陰線
                    resultvalue = kbn_rousoku.KbnRousoku.BIG_INSEN

    return resultvalue
