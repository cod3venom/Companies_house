from Kernel.Browser import Browser
from Kernel.CsvCore import CsvCore
from Kernel.Settings import Logo
from Kernel.Settings import Settings
import sys, os, threading
 
if __name__ == '__main__':
    Logo().Draw()
    try:
         Browser("","extract")

    except IndexError as ieror:
         print(ieror)
         Settings().Debug(1,'Please enter : python3 Main.py path/to/links.txt')
    except KeyboardInterrupt:
        Settings().Debug(0,'Terminated by user')