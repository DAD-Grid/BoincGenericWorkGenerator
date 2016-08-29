import os
import subprocess
import os, os.path as osp
from uuid import uuid4

"""
    Metodo que llama al stage file de boinc
"""
def stage_file(filename):
    name,ext = osp.splitext(filename)
    fullname = name + '_' + uuid4().hex + ext
    download_path = subprocess.check_output(['bin/dir_hier_path',fullname]).strip()
    subprocess.call(["cp", filename, download_path])
    return fullname

#TODO: Generar el nombre del workunit aleatorio

"""
    Metodo que llama al create work con un work unit name aleatorio
"""
def create_work_random_wu(appname, filenames):
    work_unit_name = uuid4().hex
    create_work(appname, work_unit_name, filenames)


"""
    Metodo que crea un trabajo dado el nombre de un workuni
"""
def create_work(appname, work_unit_name, filenames):
    arguments = "--appname %s --wu_name %s" % (appname, work_unit_name)
    for filename in filenames:
        real_name = stage_file(filename)
        arguments += " %s" % real_name 
    subprocess.call(["bin/create_work " +arguments], shell=True)

def main():
    print "Hello World"

if __name__ == '__main__':
    main()