#jeg henter data fra dataSamling, filtrere det og laver passende dataframes

import pandas as pd
import dataSamling

#tester lige filtrering af 2 sojler i min lille csv fil

mineData = dataSamling.filtreretDataframe(["dato","oliepris"])


mineData.hentedata("nasdq.csv",0,1)

print(mineData.data.head(5))
