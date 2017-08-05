import BoincUtil as util
import os.path
from WorkUnit import *

class App:
    """
        Constructor de la aplicacion boinc
    """
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
        self.work_units = []
    

    """
        Metodo que agrega un archivo a la aplicacion
    """
    def stage_file(self, filename):
        return util.stage_file(filename, self.directory)

    """
        Metodo que crea un workunit
    """
    def create_work_unit(self, filenames, work_unit_name = None):
        #for filename in filenames:
	        #real_filenames.append(self.stage_file(filename))
	if not os.path.exists(self.directory + '/templates/' + self.name + "_in"):
		util.create_input_template(self.name, self.directory)
	if not os.path.exists(self.directory + '/templates/' + self.name + "_out"):
		util.create_output_template(self.name, self.directory)
        workUnit = WorkUnit(self, filenames, work_unit_name)
        workUnit.create_work()
        self.work_units.append(workUnit)
