import os
import shutil
from datetime import datetime

src = "C:\\Users\\\\AppData\\Roaming\\DarkSoulsIII"
des = "e:\\backups\\savegames\\ds3"


def take_backup():
    date_m = os.path.getmtime(src) * 1000
    if check_last_modified(date_m):
        if copy_files(date_m):
            save_last_backup_time(date_m)


def check_last_modified(date_m):
    if not os.path.isfile(os.path.join(des, "lastbackup.txt")):
        save_last_backup_time(date_m, "x")
        return True
    else:
        with open(os.path.join(des, "lastbackup.txt")) as file:
            last_backup = file.read()
            if int(last_backup) != date_m:
                return True
    return False


def save_last_backup_time(date_m, mod="w"):
    if not os.path.exists(des):
        os.makedirs(des)
    with open(os.path.join(des, "lastbackup.txt"), mod) as file:
        file.write(str(date_m).split(".")[0])


def copy_files(date_m):
    try:
        date_m = int(date_m)
        shutil.copytree(src,
                        os.path.join(des, str(datetime.fromtimestamp(date_m / 1000).strftime("%Y-%m-%d %H.%M.%S"))))
        return True
    except Exception as e:
        print(e)


take_backup()
