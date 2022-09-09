import tkinter as tk
import tkinter.ttk
import tkinter.font
import tkinter.filedialog
import tkfilebrowser as tkfb
import subprocess
import os
import shutil
import webbrowser
import PyInstaller.__main__
import pyautogui as pag
import threading
import time


root = tk.Tk()

root.tk.call('source', 'tkthemes/azure-ttk-theme/azure.tcl')  # Put here the path of your theme file
root.tk.call("set_theme", "dark")

root.resizable(0,0)
root.title("Python to EXE converter")
root.iconbitmap("favicon.ico")

left_frame = tk.ttk.Frame(root)
right_frame = tk.ttk.Frame(root)

#Required

target_file_path_frame = tk.ttk.Frame(left_frame)
target_file_path_label = tk.ttk.Label(target_file_path_frame, text = "Path to the target python file -")
target_file_path_entry = tk.ttk.Entry(target_file_path_frame, width=80)
def target_file_path_browsefunc():
    filepath =tk.filedialog.askopenfilename(filetypes=(("python files","*.py *.pyw"),("All files","*.*")))
    target_file_path_entry.delete(0, "end")
    target_file_path_entry.insert(0, filepath) 
    if name_entry.get().strip() == "":
    	 name_entry.insert(0, os.path.splitext(os.path.basename(filepath))[0])
    if destination_folder_path_entry.get().strip() == "":
    	destination_folder_path_entry.insert(0, os.path.dirname(filepath))
target_file_path_browse_button = tk.ttk.Button(target_file_path_frame,text="Browse",command=target_file_path_browsefunc)

#Optional

name_frame = tk.ttk.Frame(left_frame)
name_label = tk.ttk.Label(name_frame, text="Name to assign to the EXE file -")
name_entry = tk.ttk.Entry(name_frame, width=30)

destination_folder_path_frame = tk.ttk.Frame(left_frame)
destination_folder_path_label = tk.ttk.Label(destination_folder_path_frame, text="Path to folder to store the EXE file -")
destination_folder_path_entry = tk.ttk.Entry(destination_folder_path_frame, width=80)
def destination_folder_path_browsefunc():
    folderpath =tk.filedialog.askdirectory()
    destination_folder_path_entry.delete(0, "end")
    destination_folder_path_entry.insert(0, folderpath) 
destination_folder_path_browse_button = tk.ttk.Button(destination_folder_path_frame,text="Browse",command=destination_folder_path_browsefunc)

icon_path_frame = tk.ttk.Frame(left_frame)
icon_path_label = tk.ttk.Label(icon_path_frame, text="Path to icon for EXE file -")
icon_path_entry = tk.ttk.Entry(icon_path_frame, width=80)
def icon_path_browsefunc():
    filepath =tk.filedialog.askopenfilename(filetypes=((".ico files","*.ico"),("All files","*.*")))
    icon_path_entry.delete(0, "end")
    icon_path_entry.insert(0, filepath) 
icon_path_browse_button = tk.ttk.Button(icon_path_frame,text="Browse",command=icon_path_browsefunc)

onefile_onedir_frame = tk.ttk.Frame(right_frame)
onefile_switch_intvar = tk.IntVar()
onedir_label = tk.ttk.Label(onefile_onedir_frame, text="Single directory")
onefile_switch = tk.ttk.Checkbutton(onefile_onedir_frame, text="Single file", style="Switch.TCheckbutton", variable=onefile_switch_intvar)

delete_unnecessary_files_switch_intvar = tk.IntVar()
delete_unnecessary_files_switch = tk.ttk.Checkbutton(right_frame, text="Exclude unnecessary files", style="Switch.TCheckbutton", variable=delete_unnecessary_files_switch_intvar)

console_switch_intvar = tk.IntVar(value=0)
console_switch = tk.ttk.Checkbutton(right_frame, text="Disable console", style="Switch.TCheckbutton", variable=console_switch_intvar)

clean_switch_intvar = tk.IntVar()
clean_switch = tk.ttk.Checkbutton(right_frame, text="Clear pyinstaller cache", style="Switch.TCheckbutton", variable=clean_switch_intvar)

clear_destination_dir_switch_intvar = tk.IntVar()
clear_destination_dir_switch = tk.ttk.Checkbutton(right_frame, text="Clear destination directory", style="Switch.TCheckbutton", variable=clear_destination_dir_switch_intvar)


stopwatch = tk.ttk.Label(right_frame)
progress_bar = tk.ttk.Progressbar(right_frame, orient="horizontal", length=150, maximum=100, mode="indeterminate")


def add_data_browsefunc(browsetype):
    if browsetype == "folder":
        paths_tuple = (tk.filedialog.askdirectory(),)
    elif browsetype == "file":
        paths_tuple = tk.filedialog.askopenfilenames(filetypes=((("All files","*.*"),)))
    print(repr(paths_tuple))
    if paths_tuple != ('',) and paths_tuple != '':
        paths = ','.join(str(path) for path in paths_tuple)
        if add_data_entry.get().strip()=="":
            add_data_entry.insert(0, paths)
        else:
            add_data_entry.insert("end", ','+paths) 


add_data_frame = tk.ttk.Frame(left_frame)

add_data_top_frame = tk.ttk.Frame(add_data_frame)
add_data_label = tk.ttk.Label(add_data_top_frame, text = "Include other non-binary files/folders -", anchor="w")

add_data_bottom_frame = tk.ttk.Frame(add_data_frame)
add_data_entry = tk.ttk.Entry(add_data_bottom_frame, width=66)
add_data_browse_folder_button = tk.ttk.Button(add_data_bottom_frame, text="Add folder", command=lambda:add_data_browsefunc("folder"))
add_data_browse_file_button = tk.ttk.Button(add_data_bottom_frame, text="Add file(s)", command=lambda:add_data_browsefunc("file"))

hidden_imports_label = tk.ttk.Label(left_frame, text = "Add hidden imports (Separate with commas) -")
hidden_imports_entry = tk.ttk.Entry(left_frame, width=40)


left_frame.grid(row=0, column=0, padx=(10,5))
right_frame.grid(row=0, column=1, padx=(5,10), sticky="ns", pady=(50,15))

target_file_path_frame.pack(anchor="w", pady=10)
target_file_path_label.pack(anchor="w")
target_file_path_entry.pack(anchor="w", side="left", padx=(0,5))
target_file_path_browse_button.pack(anchor="w", side="left")

name_frame.pack(anchor="w")
name_label.pack(anchor="w")
name_entry.pack(anchor="w")

destination_folder_path_frame.pack(anchor="w", pady=10)
destination_folder_path_label.pack(anchor="w")
destination_folder_path_entry.pack(anchor="w", side="left", padx=(0,5))
destination_folder_path_browse_button.pack(anchor="w", side="left")

icon_path_frame.pack(anchor="w", pady=10)
icon_path_label.pack(anchor="w")
icon_path_entry.pack(anchor="w", side="left", padx=(0,5))
icon_path_browse_button.pack(anchor="w", side="left")

onefile_onedir_frame.pack(anchor="w")

onedir_label.pack(side="left")

onefile_switch.pack(side="right")

delete_unnecessary_files_switch.pack(anchor="w")

console_switch.pack(anchor="w")

clean_switch.pack(anchor="w")

clear_destination_dir_switch.pack(anchor="w")

add_data_frame.pack(anchor="w", fill="both", pady=(2.5,10))

add_data_top_frame.grid(row=0, column=0, sticky="ew")
add_data_label.grid(row=0, column=0, sticky="w")
# add_data_row_button_frame.grid(row=0, column=4, sticky="e")
# add_data_new_row_button.grid(row=0, column=0, padx=(1,1))
# add_data_remove_row_button.grid(row=0, column=1)

add_data_bottom_frame.grid(row=1, column=0)
add_data_entry.grid(row=0, column=0, padx=(0,5))
add_data_browse_file_button.grid(row=0, column=1)
add_data_browse_folder_button.grid(row=0, column=2, padx=(2.5,0))

hidden_imports_label.pack(anchor="w")
hidden_imports_entry.pack(anchor="w")



def create_exe(target_file_path, 
    file_name, destination_folder_path, icon_path, add_data_paths, hidden_imports,  onefile, noconsole, clean, # pyinstaller options
    delete_unnecessary_files, clear_destination_dir # custom options
    ):

    options = list()

    if file_name.strip() != "":
    	options.append(f"--name={file_name}")

    options.append(f"--distpath={os.path.join(destination_folder_path,'dist/')}")
    options.append(f"--workpath={os.path.join(destination_folder_path,'build/')}")
    options.append(f"--specpath={destination_folder_path}")

    if icon_path != "":
        options.append(f"--icon={icon_path}")


    for path in add_data_paths:
        if os.path.isfile(path):
            options.append(f"--add-data={path}{os.pathsep}.")
        elif os.path.isdir(path):
            options.append(f"--add-data={path}{os.pathsep}{os.path.basename(path)}")

    for hidden_import in hidden_imports:
        options.append(f"--hidden-import={hidden_import}")

    if onefile is True:
        options.append("--onefile")

    if noconsole is True:
        options.append("--noconsole")
    else:
        options.append("--console")

    if clean is True:
        options.append("--clean")
        options.append("--noconfirm")

    if clear_destination_dir is True:
        for filename in os.listdir(destination_folder_path):
            file_path = os.path.join(destination_folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                pag.alert(text=f'Failed to delete {file_path}.\nReason: {e}', title="Python to EXE converter - Error while clearing folder")
                return
    print(options)

    # subprocess.call(["python", "-m", "PyInstaller", *options, target_file_path], cwd=destination_folder_path)

    try:
        PyInstaller.__main__.run([target_file_path, *options])
    except Exception as e:
        pag.alert(text=e, title="Python to EXE converter - Error while converting")
        return

    try:
        if delete_unnecessary_files is True:
            shutil.rmtree(os.path.join(destination_folder_path, "build/"))
            os.remove(os.path.join(destination_folder_path, f"{file_name}.spec"))
            if onefile is True:
                shutil.move(os.path.join(destination_folder_path, "dist/", f"{file_name}.exe"), os.path.join(destination_folder_path, f"{file_name}.exe"))
                os.rmdir(os.path.join(destination_folder_path, "dist/"))
            else:
                shutil.move(os.path.join(destination_folder_path, "dist/", file_name), os.path.join(destination_folder_path, file_name))
                os.rmdir(os.path.join(destination_folder_path, "dist/"))
    except Exception as e:
        pag.alert(text=e, title="Python to EXE converter - Error while deleting unnecessary files")
        return

    webbrowser.open(destination_folder_path)


def create_exe_button_command():

    create_exe_button["state"] = "disabled"
    create_exe_button.configure(style = "Toggle.TButton")
    root.update_idletasks()

    target_file_path = target_file_path_entry.get().strip()
    file_name = name_entry.get().strip()
    destination_folder_path = destination_folder_path_entry.get().strip()
    icon_path = icon_path_entry.get().strip()
    
    add_data_paths = list()
    for path in add_data_entry.get().split(','):
        path = path.strip()
        if path != "" and (os.path.isfile(path) or os.path.isdir(path)):
            add_data_paths.append(path)

    hidden_imports = list()
    for hidden_import in hidden_imports_entry.get().split(','):
        hidden_import = hidden_import.strip()
        if hidden_import != "":
            hidden_imports.append(hidden_import)    

    onefile = bool(onefile_switch_intvar.get())
    noconsole = bool(console_switch_intvar.get())
    clean = bool(clean_switch_intvar.get())
    delete_unnecessary_files = bool(delete_unnecessary_files_switch_intvar.get())
    clear_destination_dir = bool(clear_destination_dir_switch_intvar.get())

    if target_file_path == "":
        create_exe_button["state"] = "normal"
        create_exe_button.configure(style = "Accent.TButton")
        return
    elif not os.path.isfile(target_file_path):
        create_exe_button["state"] = "normal"
        create_exe_button.configure(style = "Accent.TButton")
        pag.alert(text=f"No such file: {target_file_path}", title="Python to EXE converter")
        return

    if not os.path.isdir(destination_folder_path):
        create_exe_button["state"] = "normal"
        create_exe_button.configure(style = "Accent.TButton")
        pag.alert(text=f"No such directory: {destination_folder_path}", title="Python to EXE converter")
        return


    create_exe_thread = threading.Thread(target=lambda:create_exe(target_file_path, file_name, destination_folder_path, icon_path, add_data_paths, hidden_imports, onefile, noconsole, clean, delete_unnecessary_files, clear_destination_dir))
    create_exe_thread.start()

    #start progress bar

    progress_bar.pack(side="bottom", padx=10, pady=(1,10))
    stopwatch.pack(side="bottom")
    root.update_idletasks()


    sleep_time = 11
    start_time = time.time()
    def update_progress_bar(progress):
        progress += 2
        if progress_bar["value"] == 100:
            progress = 0
        seconds_taken = time.time()-start_time
        stopwatch['text']= time.strftime("%H:%M:%S",time.gmtime(seconds_taken))
        progress_bar["value"] = progress
        if not create_exe_thread.is_alive():
            create_exe_button["state"] = "normal"
            create_exe_button.configure(style = "Accent.TButton")
            stopwatch.pack_forget()
            progress_bar.pack_forget()
            root.update_idletasks()
        else:
            root.after(sleep_time, lambda:update_progress_bar(progress))

    update_progress_bar(0)


create_exe_button = tk.ttk.Button(left_frame, text="Create EXE file", style="Accent.TButton", command=create_exe_button_command)
create_exe_button.pack(pady=(25,15))

root.mainloop()
