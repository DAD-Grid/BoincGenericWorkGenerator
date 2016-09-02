from App import App

if __name__ == '__main__':
	print "Done!"
	app = App("worker","/home/boincadm/projects/testproject")
	app.stage_file("file1.txt")
	app.create_work_unit(["file.txt"])
