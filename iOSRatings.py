from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from datetime import datetime

url = ["https://apps.apple.com/us/app/go-kinetic-by-windstream/id1342262959", #GoKinectByWindstream
    "https://apps.apple.com/us/app/my-altafiber/id1245014739", #MyAltafiber
    "https://apps.apple.com/us/app/spectrum-access-enabled-media/id1492182876", #SpectrumAccess
    "https://apps.apple.com/us/app/cox-app/id415894489", #CoxApp
    "https://apps.apple.com/us/app/my-verizon/id416023011", #MyVerizon
    "https://apps.apple.com/us/app/mycricket-app/id626392754", #MyCricket
    "https://apps.apple.com/us/app/mydish-account/id1123102087", #MyDishAccount
    "https://apps.apple.com/us/app/t-mobile/id561625752", #T-Mobile
    "https://apps.apple.com/us/app/xfinity-mobile/id1194745615", #XfinityMobile
    "https://apps.apple.com/us/app/spectrum-news-local-stories/id740948885", #SpectrumNews
    "https://apps.apple.com/us/app/my-spectrum/id942608209", #MySpectrumApp
    "https://apps.apple.com/us/app/my-sprint-mobile/id491126018", #MySprintMobile
    "https://apps.apple.com/us/app/verizon-my-fios/id476394945", #VerizonMyFios
    "https://apps.apple.com/us/app/my-centurylink/id1015059570", #MyCenturyLink
    "https://apps.apple.com/us/app/visible-mobile/id1367950045", #VisibleMobile
    "https://apps.apple.com/us/app/spectrumu/id827887111", #SpectrumU
    "https://apps.apple.com/us/app/spectrum-tv/id420455839", #SpectrumTV
    "https://apps.apple.com/us/app/myat-t/id309172177", #MyATT
    "https://apps.apple.com/us/app/spectrum-sportsnet-live-games/id563316826", #SpectrumSportsNet
    "https://apps.apple.com/us/app/mediacomconnect/id527680234", #MediacomConnect
    "https://apps.apple.com/us/app/mymetro/id1188830219", #MyMetro
    "https://apps.apple.com/us/app/myfrontier/id978439794", #MyFrontier
    "https://apps.apple.com/us/app/xfinity/id1178765645", #XfinityMyAccount
    "https://apps.apple.com/us/app/google-fiber/id1063844759", #GoogleFiber
    "https://apps.apple.com/us/app/my-viasat/id1341120640", #MyViasat
    "https://apps.apple.com/us/app/armstrong/id636522134", #ArmStrong
    "https://apps.apple.com/us/app/astound-mobile/id6449095899", #RCN_Mobile #AstoundMobile
    "https://apps.apple.com/us/app/hughesnet-mobile/id1097579916", #HughesNet_Mobile
    "https://apps.apple.com/us/app/ht-my-account/id1262963153", #HT_MyAccount
    "https://apps.apple.com/us/app/midco-my-account/id1090421908", #MidcoMyAccount
    "https://apps.apple.com/us/app/optimum-support/id1234273194", #OptimumSupport
    "https://apps.apple.com/us/app/uscellular-my-account/id1228669675", #US_Cellular_My_Account
    "https://apps.apple.com/us/app/se-next-powered-by-tivo/id1414862251", #MySecTV
    "https://apps.apple.com/us/app/optimum-tv/id1296704509", #OptimumTV
    "https://apps.apple.com/us/app/breezeline-tv/id787428890", #BreezelineTV
    "https://apps.apple.com/us/app/my-blue-ridge/id1425929491", #MyBlueRidge
    "https://apps.apple.com/us/app/mybuckeye/id1571340716" #MyBuckeye
]

def fetch_data(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.content, "lxml")
    rank_element = soup.find('a', {'class': 'inline-list__item'})
    rank = None
    if rank_element is not None:
        rank_text = rank_element.text.strip()
        rank_text = rank_text.split()[0]
        rank = int(rank_text.replace(',', '').replace('#', ''))
    script = soup.find(type="application/ld+json").text.strip()
    data = json.loads(script)

    app_rating = None
    review_count = None
    if 'aggregateRating' in data:
        app_rating = data['aggregateRating'].get('ratingValue')
        review_count = data['aggregateRating'].get('reviewCount')

    dataApp = {
        "App Name": data.get('name'),
        "iOS App Rating": app_rating,
        "iOS Total Reviews": review_count,
        "iOS Rank": rank
    }
    return dataApp

dataiOS = []
for link in url:
    dataApp = fetch_data(link)
    dataiOS.append(dataApp)

dataiOS = pd.DataFrame(dataiOS)
now = datetime.now()
dataiOS.insert(0, 'Date', now.strftime("%B %d, %Y"))
dataiOS.to_excel('iOSratings.xlsx')