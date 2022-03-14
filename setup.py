import os
import json

"""
	add the paths configs to get paths of diferents path system operatings
"""
def add_path_configs():
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cli", "workspaces")
	files = os.listdir(path)
	file_config = os.path.join(os.path.dirname(os.path.abspath(__file__)), "configs.json")

	if (len(files) == 0):
		print("no se en contraron archivos de configuracion")
		return

	i = 0
	j = 0 

	with open(file_config, "r") as f:
		data = json.load(f)	

	while(i < len(files)):
		if (files[i].endswith(".json")):
			data[j]["path"] = os.path.join(path, files[i])
			j += 1
		i += 1

	with open(file_config, "w") as f:
		json.dump(data, f)


if __name__ == "__main__":
	add_path_configs()	