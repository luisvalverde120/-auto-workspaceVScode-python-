import os
import json

class ConfigManager:

	def __init__(self, name, path) -> None:
		self.file = "config.json"
		self.data = {
			"name": name,
			"path": path,
		}
	def add(self) -> None: 
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "configs.json")
		with open(path, "r") as f:
			data = json.load(f)

		data.append(self.data)

		with open(path, "w") as f:
			json.dump(data, f)


		