import os
import subprocess
from App import *
from uuid import uuid4

class GenericWorkGenerator:

    def __init__(self, generator_path, image_path, height = 10, width = 10):
        self.generator_path = generator_path
        self.image_path = image_path
        self.height = height
        self,width = width
    
    def create_work(self, app):
        image_folder = uuid4().hex
        subprocess.call(["mkdir", image_folder], cwd = self.generator_path+"/..")
        subprocess.call([self.generator_path, self.image_path, self.height, self.width])
        #se recorren todos los archivo de determinado directorio
        images = os.listdir(self.generator_path + "/../" + image_folder)
        for image in images:
            app.create_work_unit([image])
        #limpiar los resultados que ya estan staged
        #subprocess.call(["rm","-rf",image_folder])        





