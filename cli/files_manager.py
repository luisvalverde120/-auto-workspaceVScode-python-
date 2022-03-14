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
	
	# TODO get a param to name a config
	def get_data_configs(self, file) -> None:
		try:
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workspaces", file)
			with open(path, "r") as f:
				self.config = f.read()

		except Exception as e:
			print(e)
			exit(1)

	def get_path_config(self, name) -> any:
		try:
			configs = ConfigManager().list_configs()
			path = ""
			for conf in configs:
				if (conf["name"] == name):
					path = Path(conf["path"])
		

			return path

		except Exception as e:
			print(e)
			exit(1)

	# TODO modify and add name to use the diferents configs
	def make_setting_VScode(self, name_dir, name) -> None:
		# create files
		self.name_dir = name_dir
		path_config = self.get_path_config(name)
		exit(0)		
		try:
			path = os.path.join(os.getcwd(), self.name_dir, ".vscode")
			os.mkdir(path)

			self.get_data_configs("default.json")

			file = os.path.join(path, self.name_file)
			with open(file, "w") as f:
				f.write(self.config)
				f.close()

		except Exception as e: 
			print(e)
			exit(1)

	def init_git(self) -> None:
		try:
			file = os.path.join(os.getcwd(), self.git_file)

			self.get_data_configs("gitfile.txt")

			with open(file, "w") as f:
				f.write(self.config)
				f.close()
		
		except Exception as e:
			print(e)
			exit(1)
	
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
	
	def remove_config_json(self, name) -> None:
		try:
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wokspaces")

			remove = ConfigManager().remove(name)
			
			os.remove(remove)

		except Exception as e:
			print(e)
			exit(1)

	def list_config_json(self) -> None:
		data = ConfigManager().list_configs()

		print("List configs: \n")

		for i in data:
			print(i)