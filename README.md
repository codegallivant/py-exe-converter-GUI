# python-exe-converter-GUI

GUI Interface to create executables from python applications.

<br>

![Screenshot of application](https://user-images.githubusercontent.com/27366422/189177218-f86631fe-b92a-40b5-943a-4c3bf08a2125.png)

<br>

## Features implemented in the GUI

### `pyinstaller` options
The `pyinstaller` module is used to create the executables.
The following options of pyinstaller are supported in the GUI - 
- `--name`: Name to assign to the bundled app and spec file (default: first script’s basename)
- `--onefile`: Create a one-file bundled executable. 
- `--icon`: Apply the icon to a executable.
- `--add-data`: Additional non-binary files or folders to be added to the executable.
- `--noconsole`: Do not provide a console window for standard i/o. 
- `--clean`: Clean PyInstaller cache and remove temporary files before building.
- `--distpath`,`--workpath`,`--specpath`: Where to put to the bundled app, temporary work files and the spec file. Currently, the GUI allows you to input 1 directory, which will be used for all of these parameters. It is the destination folder path.
- `--hidden-import`: Name imports not visible in the code of the script(s).

### Other options
- Automatically deleting unnecessary files after creation of the executable
- Clearing the destination directory before creation of the executable

<br>

## Credits for external libraries and files
- `tkthemes/azure-ttk-theme` (Theme style for tkinter window) - 
  https://github.com/rdbende/Azure-ttk-theme
- `favicon.ico`-
  [Flaticon (freepik)](https://www.flaticon.com/free-icon/convert_1322164?term=convert%20files&page=1&position=1&page=1&position=1&related_id=1322164&origin=search)
