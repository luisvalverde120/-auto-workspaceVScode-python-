from asyncore import read
import os

class CreateConfig:
	def __init__(self, name_dir: str) -> None:
		self.name_file = "settings.json"
		self.name_dir = name_dir
		self.config: str = "" 
	
	def get_data_configs(self) -> None:
		try:
			path = os.path.join(os.getcwd(), "workspaces", "default.json")
			with open(path, "r") as f:
				self.config = f.read()

		except Exception as e:
			print(e)
			exit(1)

	def makeSettingVScode(self) -> None:
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