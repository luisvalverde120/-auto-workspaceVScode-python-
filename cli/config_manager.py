import os
import json

class ConfigManager:

	def __init__(self, name = "", path = "") -> None:
		self.file = "configs.json"
		self.data = {
			"name": name,
			"path": path,
		}
	def add(self) -> None: 
		try:
			path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", self.file)
			with open(path, "r") as f:
				data = json.load(f)

			data.append(self.data)

			with open(path, "w") as f:
				json.dump(data, f)

		except Exception as e:
			print(e)
			exit(0)
	
	# TODO: controlar si existe el nombre dado
	def remove(self, name) -> str:
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", self.file)
		path_file = "" 
		with open(path, "r") as f:
			data = json.load(f)

		for i in range(len(data)):
			if data[i]["name"] == name:
				path_file = data[i]["path"]
				data.pop(i)
				break
		
		with open(path, "w") as f:
			json.dump(data, f)
		
		return path_file

	def getConfigs(self) -> None:
		pass
