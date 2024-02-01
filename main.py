import os
import shutil
import zipfile

dr = os.path.dirname(os.path.realpath(__file__))

def venv(filedir=None, name="venv"):
    if filedir == None:
        raise ("error, filedir can't Exist nonetype")
    else:
        if (os.path.exists(filedir) == True):
            os.system(f"cd {dr}")
            os.system(f"python -m venv {name}")
            # os.system(f"cd {name}\Lib\site-packages")
            fd = dr + f"\\{name}\\Lib\\site-packages\\"
            # shutil.move(filedir, fd)
            zipfile.ZipFile(filedir).extractall(path=fd)
        else:
            raise ("error, filedir isn't Exist")





