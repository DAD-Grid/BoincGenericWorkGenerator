from App import App
from GenericWorkGenerator import GenericWorkGenerator

if __name__ == '__main__':
	app = App("transparency","/home/boincadm/projects/testproject")
    generator = GenericWorkGenerator("bin/generator", "bin/fruit1.png")
    generator.create_work(app)
    print "Done!"
