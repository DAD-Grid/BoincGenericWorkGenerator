import BoincUtil as util

class App:
    """
        Constructor de la aplicacion boinc
    """
    def __init__(name, directory):
        self.name = name
        self.directory = directory
        self.work_units = []
    

    """
        Metodo que agrega un archivo a la aplicacion
    """
    def stage_file(filename):
        return util.stage_file(filename, self.directory)

    """
        Metodo que crea un worunit
    """
    def create_work_unit(work_unit_name = None, filenames):
        for filename in filenames:
	    stage_file(filename)
	workUnit = WorkUnit(this, filenames)
	self.work_units.append(workUnit)
	return workUnit.create_work()
