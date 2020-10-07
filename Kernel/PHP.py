from requests import requests

class PHP:
    def __init__(self):
        self.limit = 1
        self.start = 0
    #@TODO=LOAD LINKS FROM MYSQL USING LIMIT 1, START 0,1

    def nextLink(self):
        link = requests.get("http://localhost/silicon/?nextLink&machine=127.0.0.2").text
        return link