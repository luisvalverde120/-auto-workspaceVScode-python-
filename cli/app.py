"""
	cli aplication to create preference workspace in vscode
	default make a dir to work
	save a file json in workspaces and add a name
	TODO: add in new proget 
	TODO: -g initialization file .gitignore
	TODO: --list list the configs with name and path
	TODO: hacer una funcion para ejecutar los comandos por medio de condicionales
	TODO: hacer que el paramatro add funcione si se incluye el parametro name
"""

import argparse
from urllib import request
from files_manager import CreateConfig

def cli(): 
	parser = argparse.ArgumentParser(
		prog='workspacePy',
		description='create a workspace vscode implementation in python',
	)
	parser.add_argument(
		"--start",
		help="Initialization config vscode",
		nargs=1,
		metavar=("dir"),
		required=False
	)
	parser.add_argument(
		"-d", "--dir",
		required=False,
		help="Name of dir to workspace"
	)
	parser.add_argument(
		"-np", "--newproject",
		action="store_true",
		required=False,
		help='create directory for work in new project'
	)
	parser.add_argument(
		"-g", "-gitinit", 
		required=False,
		action="store_true",
		help="initizlization of git and create .gitignore"	
	)
	parser.add_argument(
		"--add",
		required=False,
		help="add a file config vscode",
		nargs=2,
		metavar=("file", "name"),
	)
	parser.add_argument(
		"--remove",
		nargs=1,
		metavar=("name_config"),
		help="remove config with name"
	)
	parser.add_argument(
		"--list",
		required=False,
		help="Get a list of name of configs exists",
		action="store_true"
	)
	return parser.parse_args()

def main():
	args = cli()
	conf = CreateConfig()
	#conf.remove_config_json(args.remove)
	#conf.add_config_json(args.add, args.name)

	if (len(args.start) >= 1):
		conf.make_setting_VScode(args.start[0])
		return

	if (args.list == True):
		conf.list_config_json()
		return

	if (len(args.add) >= 2):
		conf.add_config_json(args.add[0], args.add[1])
		return
	
	if (len(args.remove) >= 1):
		conf.remove_config_json(args.remove[0])
		return

if __name__ == '__main__':
	main()
