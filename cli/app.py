"""
	cli aplication to create preference workspace in vscode
	default make a dir to work
"""

import argparse
from files_manager import CreateConfig

def cli(): 
	parser = argparse.ArgumentParser(
		prog='workspacePy',
		description='create a workspace vscode implementation in python',
	)
	parser.add_argument(
		"-n", "--namedir",
		required=True,
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
	return parser.parse_args()


def main():
	argv = cli()
	config = CreateConfig(argv.namedir)
	config.makeSettingVScode()


if __name__ == '__main__':
	main()
