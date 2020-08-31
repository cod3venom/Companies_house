import csv,os
from Kernel.Settings import Settings
class CsvCore:
    
    def CreateHeaders(self):
        if os.path.isfile(Settings.EXPORT):
            os.remove(Settings.EXPORT)
        with open(Settings.EXPORT, 'a', encoding="utf-8") as cswriter:
                w = csv.DictWriter(cswriter, Settings().CSV_HEADERS.keys(),  delimiter=";", quoting=csv.QUOTE_NONE)
                w.writeheader()
    
    def Append(self,data,name):
        if os.path.isfile(name):
            with open(name,'a', newline='', encoding="utf-8") as writer:
                w = csv.writer(writer, delimiter=";")
                w.writerow(data)
