

def doExec(conn, cur, meigaraid, filename):
    import csv
    from util import utils
    from dao import moduleDao
    ' 株価取込'
    csv_file = open(filename, "r", encoding="ms932", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    ctr = 0

    rowinfo_before2 = None
    rowinfo_before1 = None
    rowinfo_today = None

    idouave_5day = utils.getIdouAve(filename, 5)
    idouave_25day = utils.getIdouAve(filename, 25)
    idouave_50day = utils.getIdouAve(filename, 50)
    idouave_75day = utils.getIdouAve(filename, 75)

    for row in f:

        if ctr > 0:
            #print(row)
            rowinfo_today = row

            insertvalue =  str(meigaraid) + ", "
            insertvalue =  insertvalue + utils.getInsertValues(row)
            insertvalue =  insertvalue + ", " + str(utils.getRousokuasiKbn(row).value)
            insertvalue =  insertvalue + ", " + str(utils.getSakatagohou(rowinfo_before2 ,rowinfo_before1, rowinfo_today).value)
            insertvalue =  insertvalue + ", " + utils.getIdouAveValue(idouave_5day, ctr)
            insertvalue =  insertvalue + ", " + utils.getIdouAveValue(idouave_25day, ctr)
            insertvalue =  insertvalue + ", " + utils.getIdouAveValue(idouave_50day, ctr)
            insertvalue =  insertvalue + ", " + utils.getIdouAveValue(idouave_75day, ctr)

            moduleDao.insertTbl(conn, cur, 't_kabuka', "" , insertvalue)

            rowinfo_before2 = rowinfo_before1
            rowinfo_before1 = rowinfo_today

        else:
            pass
        ctr = ctr + 1


