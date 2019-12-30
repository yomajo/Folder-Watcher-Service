# Folder Watcher Service


## Description

This is project is a part of larger project, which had to use orderly named csv files as input.

Installed folder watcher windows service works in background and **renames any new csv file within hardcoded directory** based on parent directory name.

Naming is based on parent folder directory following 3 digits (i.e. COM001.csv)

Note, that observed folder path is hardcoded in `RenameFolderService.py`

### Example

Below is an example when service is running:
![Running Service Example](/Sample%20Files/watcher-demo-gif.gif)

## Requirements

- Python 3.7.3+
- watchdog module install via `pip install watchdog` (also in requirements.txt)

## Installation and Configuration

First, change watched path in `RenameFolderService.py`:
`watched_path = r'C:\Your\Desired\Path'`
Save changes

*All of the commands below, should be in command line* 

To install service, in command line (in `RenameFolderService.py` directory, or absolute path to it):

`python RenameFolderService.py install`


If later, you want to change path, after changing the hardcoded path, update service in command line:

`python RenameFolderService.py update`

To delete a service in:

`sc delete "RenameFolderService"`

Check service status:

`sc query "RenameFolderService"`

### Common 1053 Windows Permissions error

In services, at installed "Py Folder Observer" right click--> Properties --> Log On--> enter logon name / pass:
![Screenshot from Log On Tab in Service Properties](/Sample%20Files/service-logon-screenshot.JPG)

Configure startup options (manual/automatic) in "General" tab of Service Properties Window.

## Acknowledgements

- Project is based on online tutorial by [ThePythonCorner](https://www.thepythoncorner.com/2018/08/how-to-create-a-windows-service-in-python/)
- Robertas Skalskas in fighting Windows Permissions