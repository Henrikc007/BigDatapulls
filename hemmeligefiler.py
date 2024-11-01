import os

ipadresse = os.getenv("db_lokal_ip")
brugernavn = os.getenv("db_lokal_brugernavn")
brugerpw = os.getenv("db.lokal.brugernavn")
mindatabase = "northwind"

class MySecrets:
    def __init__(self):
        self.name =  brugernavn
        self.pw = brugerpw
        self.mindb = mindatabase
        self.dbIP = ipadresse