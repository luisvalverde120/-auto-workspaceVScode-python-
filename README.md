
# Python Project Start Config

this is cli application to start a config .vscode
in this aplication we will add configs



## Initialization

this need execute setup.py to get a paths of configs defaults


## Comands app

execute next comands:

### Start
to start config:
``` bash
python app.py --start [dir] [name config]
```
this command need a dir to start the config and name of config

### add config
to add config:
``` bash
python app.py --add [file] [name config]
```
this need a file json and name of config and this command save config

### remove config
to remove config:
``` bash
python app.py --remove [name config]
```
this need name of config

### add .gitignore
to add .gitignore:
``` bash
python app.py -g
```
this command add .gitignore in path of work

### make dir 
if to create a folder when you start a config you add -m or --makedir
``` bash
python app.py --start [dir] [name config] -m
```
this command make a folder and save the config in that folder with name what you gave in --start

### list
list of configs existings
``` bash
python app.py --list 
```

