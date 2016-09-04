import BoincUtil as util
from uuid import uuid4
from App import *

class WorkUnit:
    """
        Constructor de la aplicacion boinc, si el nombre es none genera un hexadecimal aleatorio, recibe una referencia a la aplicacion que lo crea
    """
    def __init__(self, app, files, name = None):
        self.app = app
        self.files = files
        if name is None:
            self.name  = uuid4().hex
        else:
            self.name = name
    
    """
        Metodo que crea un trabajo
    """
    def create_work(self):
        util.create_work(self.app.name, self.name, self.files, self.app.directory)