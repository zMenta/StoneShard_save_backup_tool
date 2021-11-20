import os
import shutil

local_directory = os.getcwd()
# print(local_directory)

# os.mkdir(local_directory + "/folder")

os.unlink(local_directory + "/folder")
