# Folder Watcher Service


## Description

This is project is a part of larger project, which had to use orderly named csv files as input. Installed folder watcher windows service works in background and **renames any new csv file within hardcoded directory** based on parent directory name.

Naming is based on parent folder directory following 3 digits (i.e. COM001.csv)

### Example

Below is an example when service is running:
![Running Service Example](/Sample%20Files/watcher-demo-gif.gif)

## Requirements

- Python 3.7.3+
- watchdog module install via `pip install watchdog` (also in requirements.txt)

## Installation and Configuration



## Acknowledgements

- Project is based on online tutorial by [ThePythonCorner](https://www.thepythoncorner.com/2018/08/how-to-create-a-windows-service-in-python/)
- Robertas Skalskas in fighting Windows Permissions