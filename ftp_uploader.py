#!/usr/bin/env python3
import logging
import ftplib
import os
import time
from datetime import datetime

logging.basicConfig(filename="log.log".format(datetime.now()), filemode="w", level=logging.INFO)
log = logging.getLogger("ex")
current_path = os.path.join((os.path.dirname(__file__)))
print(current_path)
_file_format = "rar"
FTP_URL = ""
FTP_USERNAME = ""
FTP_PASSWORD = ""

START_HOUR = 3
START_MIN = 0
END_HOUR = 6
END_MIN = 59


def upload(file_name):
    filer_path = os.path.join(current_path, file_name)
    logging.info("Start upload file {} in {}:{} Time".format(filer_path, datetime.now().hour, datetime.now().minute))
    session = ftplib.FTP(FTP_URL, FTP_USERNAME, FTP_PASSWORD)
    file = open(filer_path, 'rb')
    session.storbinary('STOR {}'.format(file_name), file)
    file.close()
    session.quit()
    return True


def start_upload():
    while True:
        now = datetime.now()
        if START_HOUR <= now.hour <= END_HOUR and START_MIN <= now.minute <= END_MIN:
            files = os.listdir(current_path)
            logging.info("Start upload in {}:{} Time".format(now.hour, now.minute))
            for file in files:
                if file.endswith(_file_format):
                    print(file)
                    if upload(file):
                        logging.info("Success upload file {} in {}:{} Time".format(file, datetime.now().hour,
                                                                                 datetime.now().minute))
                        os.remove(os.path.join(current_path, file))
                        logging.info("remove file file {} in {}:{} Time".format(file, datetime.now().hour,
                                                                                   datetime.now().minute))
            exit(0)
        else:
            logging.info("Sleep for 10 second in {}:{} Time".format(datetime.now().hour, datetime.now().minute))
            print("sleep")
            time.sleep(10)


while True:
    try:
        start_upload()
    except Exception as e:
        logging.info("error for {} in {}:{} Time".format(e, datetime.now().hour, datetime.now().minute))
        print(e)
        time.sleep(10)
