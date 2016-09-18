import os
import subprocess
from App import *
from uuid import uuid4

class GenericWorkGenerator:

    def __init__(self, generator_path, image_path, height = 2, width = 2):
        self.generator_path = generator_path
        self.image_path = image_path
        self.height = height
        self.width = width
    
    def create_work(self, app):
        image_folder = uuid4().hex
        subprocess.call(["mkdir", image_folder], cwd = os.path.abspath(os.path.join(self.generator_path, '..')))
        
        # se obtiene el nombre del ejecutable
        head, tail = os.path.split(self.generator_path)
        executable_name = tail
        
        # se obtiene el nombre de la imagen
        head, tail = os.path.split(self.image_path)
        image_name = tail

        #se llama al ejecutable que divide trabajo desde su directorio
        subprocess.call(["./" + executable_name, image_name, image_folder, str(self.height), str(self.width) ], cwd = head)

        #se listan las imagenes que se guardan en ese directorio
        images = os.listdir(os.path.join(os.path.abspath(os.path.join(self.generator_path, '..')),image_folder))
        for image in images:
            image_location = os.path.abspath(os.path.join(head,image_folder,image))
            app.create_work_unit([image_location], image + uuid4().hex)
        #limpiar los resultados que ya estan stagged
        subprocess.call(["rm","-rf",image_folder], cwd = head)





