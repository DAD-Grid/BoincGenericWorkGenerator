import os
import subprocess
import os, os.path as osp
from uuid import uuid4
import xml.etree.cElementTree as ET


def create_input_template(filename, project_dir, number):
    xml = """<file_info>
            <number>%i</number>
        </file_info>
        <workunit>
            <file_ref>
                <file_number>%i</file_number>
                <open_name>%s</open_name>
                <copy_file/>
            </file_ref>
            <rsc_fpops_bound>1e12</rsc_fpops_bound>
            <rsc_fpops_est>1e14</rsc_fpops_est>
        </workunit>
    """ % (number, number, filename)
    fo = open(osp.join(project_dir, "templates", filename), "wb")
    fo.write(xml)
    fo.close()

def stage_file(filename, project_dir):
    head, tail = os.path.split(filename)
    name, ext = osp.splitext(tail)
    fullname = name + '_' + uuid4().hex + ext
    create_input_template(fullname, project_dir,0) # ojo, esta quemado el cero ahora
    download_path = subprocess.check_output(['bin/dir_hier_path', fullname], cwd = project_dir).strip()
    subprocess.call(["cp", filename, download_path])
    return fullname

def create_work(appname, work_unit_name, filenames, project_dir):
    args = []
    args.append("bin/create_work")
    args.append("--appname")
    args.append(appname)
    args.append("--wu_name")
    args.append(work_unit_name)
    for filename in filenames:
        real_name = stage_file(filename, project_dir)
        args.append("--wu_template")
        args.append("templates/"+real_name)
        args.append(real_name)
    arguments = arguments[:-1]
    subprocess.call(args, cwd = project_dir)