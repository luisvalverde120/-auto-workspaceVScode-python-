from shutil import copy
from config_manager import ConfigManager
import os
from pathlib import Path

class CreateConfig:
	def __init__(self ) -> None:
		self.name_file = "settings.json"
		self.git_file = ".gitignore"
		self.name_dir = "" 
		self.config: str = "" 
		self.path_configs = "workspaces"
	
	"""
		save data of file in var config	
		@param file 
	"""
	def get_data_configs(self, file) -> None:
		try:
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workspaces", file)
			with open(path, "r") as f:
				self.config = f.read()

		except Exception as e:
			print(e)
			exit(1)

	"""
		this method find to file by name and return file name of config
		@param name 	
		@return path.name = this is a name file
	"""
	def get_path_config(self, name) -> any:
		try:
			configs = ConfigManager().list_configs()
			path = ""
			for conf in configs:
				if (conf["name"] == name):
					path = Path(conf["path"])
		

			return path.name

		except Exception as e:
			print(e)
			exit(1)

	"""
		init configs to vscode project 
		@param name_dir = name of directory to add configs vscode
		@param name = this is name of config
		@param make_dir boolean = if true make a folder	
	"""
	def make_setting_VScode(self, name_dir, name, make_dir: bool) -> None:
		# create files
		self.name_dir = name_dir
		file_config = self.get_path_config(name)

		if (make_dir == True):
			path_new_folder = os.path.join(os.getcwd(), self.name_dir)
			os.mkdir(path_new_folder)

		try:
			path = os.path.join(os.getcwd(), self.name_dir, ".vscode")
			os.mkdir(path)

			self.get_data_configs(file_config)

			file = os.path.join(path, self.name_file)
			with open(file, "w") as f:
				f.write(self.config)
				f.close()

		except Exception as e: 
			print(e)
			exit(1)

	"""
		init a .gitignore in project
		@param name_dir = directory to add .gitignore	
	"""
	def init_git(self, name_dir: str = "") -> None:
		try:
			file = os.path.join(os.getcwd(), name_dir, self.git_file)

			self.get_data_configs("gitfile.txt")

			with open(file, "w") as f:
				f.write(self.config)
				f.close()
		
		except Exception as e:
			print(e)
			exit(1)

	"""
		add config .json this need file and name to find file config
		@param file this file need will json
		@param name 	
	"""	
	def add_config_json(self, file, name) -> None:
		try:
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workspaces")

			if not os.path.exists(file):
				print(f"file {file} not find.")
				exit(1)
			
			file_path = os.path.join(path, file)

			
			copy(file, file_path)
			ConfigManager(name, file_path).add()

		except Exception as e:
			print(e)
			exit(1)
	
	"""
		remove config and delete config in configs.json
		@param name name of configs to delete	
	"""
	def remove_config_json(self, name) -> None:
		try:
			remove = ConfigManager().remove(name)
			
			print(remove)

			os.remove(remove)

		except Exception as e:
			print(e)
			exit(1)


	"""
		list a configs existents	
	"""
	def list_config_json(self) -> None:
		data = ConfigManager().list_configs()

		print("List configs: \n")

		for i in data:
			print(i)