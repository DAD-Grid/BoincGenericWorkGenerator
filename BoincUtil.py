import os
import subprocess
import os, os.path as osp
import logging
from uuid import uuid4


"""
    metodo que genera un template de salida simple y lo guarda en templates del proyecto
"""
def create_output_template(app_name, project_dir):

    template_name = app_name + "_out"
    xml = """
    <output_template>
        <file_info>
            <name><OUTFILE_0/></name>
            <generated_locally/>
            <upload_when_present/>
            <max_nbytes>5000000</max_nbytes>
            <url><UPLOAD_URL/></url>
        </file_info>
        <result>
            <file_ref>
                <file_name><OUTFILE_0/></file_name>
                <open_name>fruit1_salida.png</open_name>
                <copy_file/>
            </file_ref>
        </result>
    </output_template>
    """

    fo = open(osp.join(project_dir, "templates", template_name), "wb")
    logging.info("Output template %s generated" % template_name)
    fo.write(xml)
    fo.close()
    return template_name

"""
    metodo que crea un input template simple y lo guarda en la carpeta templates del proyecto
"""
def create_input_template(app_name, project_dir):
    template_name = app_name + "_in"
    xml = """
    <input_template>
        <file_info>
            <number>0</number>
        </file_info>
        <workunit>
            <file_ref>
                <file_number>0</file_number>
                <open_name>fruit1.png</open_name>
                <copy_file/>
            </file_ref>
            <rsc_fpops_bound>1e12</rsc_fpops_bound>
            <rsc_fpops_est>1e14</rsc_fpops_est>
            <rsc_memory_bound>1e8</rsc_memory_bound>
        </workunit>
    </input_template>
    """
    logging.info("Input template %s generated" % template_name)
    fo = open(osp.join(project_dir, "templates", template_name), "wb")
    fo.write(xml)
    fo.close()
    return template_name

"""
    metodo que agrega un archivo con determinado nombre a un proyecto que esta en ese directorio
"""
def stage_file(filename, project_dir):
    head, tail = os.path.split(filename)
    name, ext = osp.splitext(tail)
    fullname = name + '_' + uuid4().hex + ext
    logging.info(' '.join(['bin/dir_hier_path', fullname]))
    download_path = subprocess.check_output(['bin/dir_hier_path', fullname], cwd = project_dir).strip()
    subprocess.call(["cp", filename, download_path])
    return fullname


"""
    metodo que crea un trabajo dado un conjunto de archivos, que primero son agregados
"""
def create_work(appname, work_unit_name, filenames, project_dir):
    args = ["bin/create_work", "--appname", appname, "--wu_name",  work_unit_name]
    for filename in filenames:
        real_name = stage_file(filename, project_dir)
        args.append(real_name)
    logging.info(' '.join(args))
    subprocess.call(args, cwd = project_dir)
