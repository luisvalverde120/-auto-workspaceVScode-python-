"""
	cli aplication to create preference workspace in vscode
	default make a dir to work
	save a file json in workspaces and add a name
	TODO: create chapter
"""

import argparse
from files_manager import CreateConfig

def cli(): 
	parser = argparse.ArgumentParser(
		prog='workspacePy',
		description='create a workspace vscode implementation in python',
	)
	parser.add_argument(
		"--start",
		help="Initialization config vscode this need a dir to workspace",
		nargs=2,
		metavar=("dir", "name"),
		required=False
	)
	parser.add_argument(
		"-m", "--makedir",
		action="store_true",
		default=False,
		required=False,
		help='create directory for work in new project'
	)
	parser.add_argument(
		"-g", "--gitinit", 
		required=False,
		action="store_true",
		default=False,
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

	if (args.start != None):
		conf.make_setting_VScode(args.start[0], args.start[1], args.makedir)

	if (args.list == True):
		conf.list_config_json()

	if (args.add != None):
		conf.add_config_json(args.add[0], args.add[1])
	
	if (args.remove != None):
		conf.remove_config_json(args.remove[0])

	if (args.gitinit == True):
		if (args.start != None):
			conf.init_git(args.start[0])
		else:
			conf.init_git()

if __name__ == '__main__':
	main()
