import os
import subprocess


def rename_compress_files(_file_format, _remove_str):
    files = os.listdir(".")
    for file in files:
        if file.endswith(_file_format):
            new_name = file.replace(_remove_str, "")
            os.rename(file, new_name)
            print("file:{} renamed to ==> {}".format(file, new_name))
            rar_file_name = ".".join(new_name.split(".")[:-1]) + "(www.TutDL.ir)" + ".rar"
            subprocess.run(["rar", "a", "-r", rar_file_name, file])


file_format = input("enter file format you want to compress:")
remove_str = input("enter text want to remove from file name:")
rename_compress_files(file_format, remove_str)

