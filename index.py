import os
import shutil

os.chdir('/your/path/to/temporary/folder')

path = os.getcwd()

if os.path.exists("tmp"):
    dir = path + '/tmp'
    for f in os.listdir(dir):
        try:
            os.remove(os.path.join(dir, f))
        except:
            shutil.rmtree(os.path.join(dir, f))
else:
    os.mkdir(path + '/tmp')
