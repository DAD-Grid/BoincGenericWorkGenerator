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
    arguments = "--appname %s --wu_name %s" % (appname, work_unit_name)
    for filename in filenames:
        real_name = stage_file(filename, project_dir)
        arguments += "--wu_template %s" % real_name
        arguments += " %s" % real_name
    subprocess.call([project_dir + "/bin/create_work", arguments])
