from iOSRatings import dataiOS
from androidRatings import dataAndroid
import pandas as pd

dataAndroid['App Name'] = dataiOS['App Name']
dataCombined = pd.merge(dataiOS, dataAndroid, on='App Name', how='outer')
dataCombined.to_excel('combinedRatings.xlsx')
