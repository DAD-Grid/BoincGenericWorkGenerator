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
    def create_work():
        pass # ver como se puede hacer esto mejor