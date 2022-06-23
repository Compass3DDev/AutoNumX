from cx_Freeze import setup, Executable
import sys
import os

exe = Executable(
      script="App.py",
      base="Win32GUI",
      target_name="AutoNumX",
      icon= "logoautonum.ico",
      shortcut_name="AutoNumX",
      shortcut_dir="DesktopFolder"
     )

bexe= {
    "include_msvcr": True
    }

bmsi= {
    "all_users": True,
    "install_icon": "logoautonum.ico",
    "initial_target_dir": "C:/",
    "target_name": "AutoNumX"
    }

setup(
      name="AutoNumX",
      version="1.1",
      author="Gabriel Santos",
      description="Compass Copyright 2022",
      executables=[exe],
      options= {
          "buid_exe": bexe,
          "build_msi": bmsi
      }
      ) 
