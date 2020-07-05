# -*- coding: utf-8 -*-
from numpy import float

import codecs
import pandas as pd

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
    resultvalue = kbn_rousoku.KbnRousoku.BLANK

    if openclosingrate == 0.0:
        resultvalue = kbn_rousoku.KbnRousoku.YORIHIKI_DOUJISEN

    elif (openprice == lowprice) and (closingprice == highprice):
        # 陽の丸坊主
        resultvalue = kbn_rousoku.KbnRousoku.YOUNO_MARUBOUZU

    elif (openprice == highprice) and (closingprice == lowprice):
        # 陰の丸坊主
        resultvalue = kbn_rousoku.KbnRousoku.KAGENO_MARUBOUZU

    elif openprice < closingprice:

        if (closingprice < highprice) and (highprice - closingprice) > (openprice - lowprice):

            if (openprice == lowprice):

                if (closingprice - openprice) < (highprice - closingprice):
                    # トンカチ上影陽線
                    resultvalue = kbn_rousoku.KbnRousoku.TONKATI_UWAKAGE_YOUSEN
                else:
                    # 陽の寄付坊主
                    resultvalue = kbn_rousoku.KbnRousoku.YOUNO_YORITUKIBOUZU
            else:
                # 上影陽線
                resultvalue = kbn_rousoku.KbnRousoku.UWAKAGE_YOUSEN

        else:
            if (lowprice < openprice) and (openprice - lowprice) > (highprice - closingprice):

                if highprice == closingprice:

                    if (highprice - openprice) < (openprice - lowprice):
                        # カラカサ下影陽線
                        resultvalue = kbn_rousoku.KbnRousoku.KARASAKA_SITAKAGE_YOUSEN
                    else:
                        # 陽の大引坊主
                        resultvalue = kbn_rousoku.KbnRousoku.YOUNO_DAIHIKIBOUZU
                else:
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

            if closingprice == lowprice:

                if (openprice - closingprice) < (highprice - openprice):
                    # トンカチ上影陰線
                    resultvalue = kbn_rousoku.KbnRousoku.TONKATI_UWAKAGE_INSEN
                else:
                    # 陰の大引坊主
                    resultvalue = kbn_rousoku.KbnRousoku.KAGENO_DAIHIKIBOUZU
            else:
                # 上影陰線
                resultvalue = kbn_rousoku.KbnRousoku.UWAKAGE_INSEN

        else:
            if lowprice < closingprice and (closingprice - lowprice) > (highprice - openprice):

                if openprice == highprice:

                    if  (highprice - openprice) < (closingprice - lowprice):
                        # カラカサ下影陰線
                        resultvalue = kbn_rousoku.KbnRousoku.KARASAKA_SITAKAGE_INSEN
                    else:
                        # 陰の寄付坊主
                        resultvalue = kbn_rousoku.KbnRousoku.KAGENO_YORITUKIBOUZU
                else:
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

def getSakatagohou(rowinfo_before2, rowinfo_before1, rowinfo_today):

    from kbn import kbn_sakatagohou

    resultvalue = kbn_sakatagohou.KbnSakataGohou.BLANK

    if (rowinfo_before2 is None) or (rowinfo_before1 is None) or (rowinfo_today is None):
        return resultvalue
    else:
        pass

    openprice_before2 = float(rowinfo_before2[1])
    highprice_before2 = float(rowinfo_before2[2])
    lowprice_before2 = float(rowinfo_before2[3])
    closingprice_before2 = float(rowinfo_before2[4])

    openprice_before1 = float(rowinfo_before1[1])
    highprice_before1 = float(rowinfo_before1[2])
    lowprice_before1 = float(rowinfo_before1[3])
    closingprice_before1 = float(rowinfo_before1[4])

    openprice_today = float(rowinfo_today[1])
    highprice_today = float(rowinfo_today[2])
    lowprice_today = float(rowinfo_today[3])
    closingprice_today = float(rowinfo_today[4])

    #print('▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽▽')
    #print(rowinfo_before2)
    #print(rowinfo_before1)
    #print(rowinfo_today)

    if (openprice_before2 > closingprice_before2):
        if ( openprice_before1 < closingprice_before1) and (closingprice_before2 > openprice_before1):
            if (openprice_today < closingprice_today) and (closingprice_before1 <= openprice_today):
                # 三川明けの明星（買い）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.BUY_SANSENAKENOMYOUJYOU
            else:
                pass

        elif (openprice_before1 > closingprice_before1) and (openprice_before2 >= closingprice_before1):
            if (openprice_today > closingprice_today) and (openprice_before1 >= closingprice_today):
                # 三羽烏（売り）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.SELL_SANBAGARASU
            else:
                pass
        else:
            pass

    elif (openprice_before2 < closingprice_before2):
        if (openprice_before1 < closingprice_before1) and (closingprice_before2 <= closingprice_before1):
            if (openprice_today < closingprice_today) and (closingprice_before1 <= closingprice_today):
                # 赤三兵（買い）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.BUY_AKASANPEI
            else:
                pass

        elif (openprice_before1 > closingprice_before1) and (closingprice_before2 < openprice_before1 ):
            if (openprice_today > closingprice_today) and (closingprice_before1 <= openprice_today ):
                # 三川宵の明星（売り）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.SELL_SANSENYOINOMYOUJYOU
            else:
                pass
        else:
            pass

    elif (openprice_before1 < closingprice_before1):
        if (openprice_today > closingprice_today):

            if (closingprice_before1 < openprice_today):
                if (openprice_before1 < closingprice_today) and (closingprice_before1 > closingprice_today):
                    # かぶせ線（売り）
                    resultvalue = kbn_sakatagohou.KbnSakataGohou.SELL_KABURISEN

                elif (openprice_before1 > closingprice_today):
                    # つつみ線（売り）
                    resultvalue = kbn_sakatagohou.KbnSakataGohou.SELL_TUTUMISEN
                else:
                    pass

            elif (closingprice_before1 > openprice_today):
                if (openprice_before1 < closingprice_today):
                    # はらみ線（売り）
                    resultvalue = kbn_sakatagohou.KbnSakataGohou.SELL_HARAMISEN

                elif (openprice_before1 > closingprice_today):
                    # たすき線（売り）
                    resultvalue = kbn_sakatagohou.KbnSakataGohou.SELL_TASUKISEN

                else:
                    pass

            elif (closingprice_before1 == closingprice_today):
                # 出会い線（売り）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.SELL_DEAISEN

            elif (openprice_before1 == openprice_today):
                # 振り分け線（売り）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.SELL_HURIWAKESEN

            else:
                pass

        else:
            pass

    elif (openprice_before1 > closingprice_before1):

        if (closingprice_today > openprice_today):

            if (closingprice_before1 > openprice_today) and abs(closingprice_before1 - closingprice_today) <= 5:
                # 出会い線（買い）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.BUY_DEAISEN

            elif (openprice_today < lowprice_before1) and (closingprice_today > ((openprice_before1 + closingprice_before1) / 2)):
                # 切り込み線（買い）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.BUY_KIRIKOMISEN

            elif (openprice_today > closingprice_before1) and (closingprice_today < openprice_before1):
                # はらみ線（買い）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.BUY_HARAMISEN

            elif (openprice_before1 > openprice_today) and (closingprice_before1 < openprice_today):
                # たすき線（買い）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.BUY_TASUKISEN

            elif abs(openprice_before1 - openprice_today) <=  5:
                #振り分け線（買い）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.BUY_HURIWAKESEN

            elif (openprice_today < closingprice_before1) and (openprice_before1 < closingprice_today):
                # つつみ線（買い）
                resultvalue = kbn_sakatagohou.KbnSakataGohou.BUY_TUTUMISEN
            else:
                pass

        else:
            pass
    else:
        pass

    #print('resultvalue＝' + str(resultvalue.value))
    #print('△△△△△△△△△△△△△△△△△△△△△△△△')

    return resultvalue

def sma(term, closeList=[]):
    '''単純移動平均の計算'''
    result = list(pd.Series(closeList).rolling(term).mean().fillna(0))
    #print(result)
    return result

def getIdouAve(filename, term):
    # 終値の用意
    with codecs.open(filename, 'r', encoding='ms932') as f:
        [next(f).encode('ms932') for _ in range(2)]
        closeList = [float(row.split(',')[4]) for row in f]

    #print(closeList)
    # pandas
    #df = pd.DataFrame(dict(close=closeList, sma=sma(term, closeList)))
    #print(df)

    return sma(term, closeList)



def getIdouAveValue(idouave, ctr):
    if len(idouave) <= ctr:
        return '0'
    else:
        return str(idouave[ctr])
