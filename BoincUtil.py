import os
import subprocess
import os, os.path as osp
import logging
from uuid import uuid4



def create_output_template(filename, project_dir, number):

    head, tail = os.path.split(filename)
    filename_no_extension, ext = osp.splitext(tail)
    output_filename = filename_no_extension + "_salida" + ext
    logging.info("Se crea el archivo de salida " + output_filename)
    template_name = filename + ".out"
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
                <open_name>%s</open_name>
                <copy_file/>
            </file_ref>
        </result>
    </output_template>
    """ % (output_filename)

    fo = open(osp.join(project_dir, "templates", template_name), "wb")
    logging.info("Output template %s generated" % template_name)
    fo.write(xml)
    fo.close()
    return template_name

"""
    metodo que crea un input template por simple
"""
def create_input_template(filename, project_dir, number):
    template_name = filename + ".in"
    xml = """
    <input_template>
        <file_info>
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
            <rsc_memory_bound>1e8</rsc_memory_bound>
        </workunit>
    </input_template>
    """ % (number, number, filename)
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
    create_input_template(fullname, project_dir,0) # ojo, esta quemado el cero ahora
    create_output_template(fullname, project_dir, 0)
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
        args.append("--wu_template")
        args.append("templates/"+real_name+".in")
        args.append("--result_template")
        args.append("templates/"+real_name+".out")
        args.append(real_name)
    logging.info(' '.join(args))
    subprocess.call(args, cwd = project_dir)