import os
import platform
import getpass
import time
import webbrowser

if platform.system() == "Windows":
    os.system("pip install flask")
    os.system("pip install matplotlib")
    cwd = os.getcwd()
    main_path = os.path.abspath("main.py")
    os.chdir(r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(getpass.getuser()))
    with open("blood_pressure_manager.bat", "w") as f:
        f.write("python3 \"" + main_path + "\"")
    webbrowser.open("http://localhost:7634/")
    os.chdir(cwd)
    os.system("python3 \"" + main_path + "\"")
elif platform.system() == "Darwin":
    os.system("sudo pip3 install flask")
    os.system("sudo pip3 install matplotlib")
    with open("main.py", "r") as f:
        to_write = f.read().replace("# This is a placeholder, please ignore this", "webbrowser.open('http://localhost:7634/')")
    with open("main.py", "w") as f:
        f.write(to_write)
    print("---------------------\n\nInstallation done! Please run main.py for the app.\n\n---------------------")
    time.sleep(5)
else:
    print("Operating system not supported!")
    time.sleep(5)