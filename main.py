#!/usr/bin/env python

import sys
from App import App
from GenericWorkGenerator import GenericWorkGenerator

if __name__ == '__main__':
    if len(sys.argv) < 5 :
	print 'usage: python main.py app_name project_path generator_path image_path'
    else: 
    	app = App(sys.argv[1], sys.argv[2])
    	generator = GenericWorkGenerator(sys.argv[3], sys.argv[4])
    	generator.create_work(app)
    	print "Done!"
