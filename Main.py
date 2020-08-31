from Kernel.Browser import Browser
from Kernel.CsvCore import CsvCore
from Kernel.Settings import Logo
from Kernel.Settings import Settings
import sys, os, threading
 
if __name__ == '__main__':
    Logo().Draw()
    try:
        input = sys.argv[1]
        path = sys.argv[2]
        if input == 'sublinks':
            if os.path.isfile(path):
                Browser(path,'sublinks')  
        if input == 'extract':
            if os.path.isfile(path):
                CsvCore().CreateHeaders() 
                Browser(path,'extract')
        else:
            Settings().Debug(0,"LINKS FILE DOESN'T EXISTS")

    except IndexError as ieror:
         print(ieror)
         Settings().Debug(1,'Please enter : python3 Main.py path/to/links.txt')
    except KeyboardInterrupt:
        Settings().Debug(0,'Terminated by user')