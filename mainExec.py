# -*- coding: utf-8 -*-

def run_mainExec():

    import json, sqlite3, datetime, logging.config, requests
    from config import app_config
    from dao import tweetdbDao
    from util import utils
    from datetime import datetime
    from logging import getLogger

    logging.config.fileConfig('logging.conf')
    logger = getLogger()
    logger.info('▼▼▼▼▼▼START▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼')
    date_today = datetime.now().strftime("%Y-%m-%d")
    date_time = datetime.now().strftime("%H:%M:%S")

    logger.info('｜処理日: %s', date_today)
    logger.info('｜処理時間: %s', date_time)

    db_connection = sqlite3.connect(app_config.DB_NAME)
    db_cursol = db_connection.cursor()


    logger.info('｜正常終了')

    db_connection.commit()
    db_connection.close()

    logger.info('▲▲▲▲▲▲END▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲')



if __name__ == '__main__':
    run_mainExec()


"""
def schedule(interval, f, wait=True):
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)


if __name__ == '__main__':
    schedule(300, run_searchTrendInfo)
    #run_searchTrendInfo()
"""
