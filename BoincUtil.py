import os
import subprocess
import os, os.path as osp
from uuid import uuid4


def stage_file(filename, project_dir):
    name,ext = osp.splitext(filename)
    fullname = name + '_' + uuid4().hex + ext
    download_path = subprocess.check_output(['bin/dir_hier_path', fullname], cwd = project_dir).strip()
    subprocess.call(["cp", filename, download_path])
    return fullname

def create_work(appname, work_unit_name, filenames, project_dir):
    arguments = "--appname %s --wu_name %s" % (appname, work_unit_name)
    for filename in filenames:
        real_name = stage_file(filename, project_dir)
        arguments += " %s" % real_name
    subprocess.call([project_dir + "/bin/create_work", arguments])