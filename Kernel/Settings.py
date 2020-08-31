from colorama import Fore, Back, Style
from colorama import init
from tqdm import tqdm
import datetime, time, os

init()
class Settings:
    HEADER_PATH = ''' //*[@class="heading-xlarge"]'''
    
    HEADER_NUMBER = '''//*[@id="company-number"]/strong'''
    
    BOX_PATH = '''//*[@class="appointments-list"]/div'''
    
    SUB_LINKS = '//*[@class="page"]'
    CSV_HEADERS = {
        'URL':'','COMPANY_NAME':'', 'COMPANY_NUMBER':'','NAME':'','Correspondence address':'', 'Role':'','Date of birth':'', 'Appointed on':''
        ,'Nationality':'','Country of residence':'','Occupation':''
    }

    EXPORT = 'export_{}.csv'.format(int(round(time.time()*1000)))
    CACHE_PAGES = 'Cache//Pages.txt'
    def Debug(self,status,data):
        Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if status > 1:
            print(Colors().CYAN() +"[+] ["+str(Now) +"] ========> "+ Colors().Success() +str(data))
        else:
            print(Colors().CYAN() +"[+] ["+str(Now) +"] ========> "+Colors().Error() + str(data))


    def Read(self,path):
        if os.path.isfile(path):
            with open(path,'r') as reader:
                return reader.read()
class Colors:
    def Default(self):
        return Fore.WHITE
    def Success(self):
        return Fore.GREEN
    def Error(self):
        return Fore.RED
    def Warrning(self):
        return Fore.YELLOW
    def CYAN(self):
        return Fore.CYAN


class Logo:
    def Draw(self):
        pass