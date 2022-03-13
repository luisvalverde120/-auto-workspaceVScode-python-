from shutil import copy
from config_manager import ConfigManager
import os

class CreateConfig:
	def __init__(self, name_dir: str = "") -> None:
		self.name_file = "settings.json"
		self.name_dir = name_dir
		self.config: str = "" 
		self.path_configs = "workspaces"
	
	def get_data_configs(self) -> None:
		try:
			path = os.path.join(os.getcwd(), "workspaces", "default.json")
			with open(path, "r") as f:
				self.config = f.read()

		except Exception as e:
			print(e)
			exit(1)

	def make_setting_VScode(self) -> None:
		# create files
		try:
			path = os.path.join(os.getcwd(), self.name_dir, ".vscode")
			os.mkdir(path)

			self.get_data_configs()

			file = os.path.join(path, self.name_file)
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

