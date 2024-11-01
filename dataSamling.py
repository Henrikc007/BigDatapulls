#her vil jeg lave en klasse om indeholder en funktion der læser en csv fil

import pandas as pd

import csv

def returnOneLine(filen):
    with open(filen) as file:
        csv_reader = csv.reader(file,delimiter=",")
        for row in csv_reader:
            yield(row)

class filtreretDataframe():
    def __init__(self,rakker):
        sojleEt=rakker[0]
        sojleTo=rakker[1]
        databeholder = {
            sojleEt: [],
            sojleTo: []
        }
        self.data = pd.DataFrame(databeholder)

    
    def hentedata(self,fil,sojle1,sojle2):
        for line in returnOneLine(fil):
            nylinjedata=pd.Series([line[sojle1], line[sojle2]],index=["dato","oliepris"])
            self.data=pd.concat([self.data,nylinjedata.to_frame().T],ignore_index=False)
            




    
