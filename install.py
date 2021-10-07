#!/bin/python3
import os
import time
import platform
print("="*50)
print("            [+] PLEAS WITE INSTALL TOL  ")
print("="*50)
if platform.system() == "Linux":
    os.system("pip install colorama")
    os.system("pip install ipaddress ")
    os.system("cp fastscan /bin/ &&  chmod 755  /bin/fastscan")
    print("done")
else:
    os.system("pip install ipaddress")
    os.system("pip install colorama")
print("================== DONE INASTALL ==============")
time.sleep(2)
