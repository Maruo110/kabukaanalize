

def doExec(conn, cur, meigaraid, filename):
    import csv
    from util import utils
    from dao import moduleDao
    ' 株価取込'
    csv_file = open(filename, "r", encoding="ms932", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    ctr = 0

    for row in f:

        if ctr > 0:
            #print(row)
            insertvalue =  str(meigaraid) + ", "
            insertvalue =  insertvalue + utils.getInsertValues(row)
            insertvalue =  insertvalue + ", " + str(utils.getRousokuasiKbn(row).value)

            moduleDao.insertTbl(conn, cur, 't_kabuka', "" , insertvalue)

        else:
            pass
        ctr = ctr + 1

