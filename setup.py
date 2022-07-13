# python setup.py build
# pip install cx_Freeze
from cx_Freeze import setup, Executable

executables = [Executable('main.py', base="Win32GUI", target_name="WindowTime")]

setup(name='WindowTime',
      version='1.0.0',
      description='Ivan.Koss_developer',
      executables=executables)
