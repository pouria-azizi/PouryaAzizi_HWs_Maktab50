import shutil

original = r'original path where the file is currently stored\file name.file extension'
target = r'target path where the file will be copied\file name.file extension'

shutil.copyfile(original, target)
