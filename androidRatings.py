from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

urlAndroid = [
    "https://play.google.com/store/apps/details?id=com.windstream.residential&hl=en_US&gl=US", #Windstream
    "https://play.google.com/store/apps/details?id=com.altafiber.myaltafiber&hl=en_US&gl=US", #MyAltaFiber
    "https://play.google.com/store/apps/details?id=com.spectrum.access&hl=en_US&gl=US", #SpectrumAcces
    "https://play.google.com/store/apps/details?id=com.cox.android.mobileconnect&hl=en_US&gl=US", #CoxApp
    "https://play.google.com/store/apps/details?id=com.vzw.hss.myverizon&hl=en_US&gl=US", #MyVerizon
    "https://play.google.com/store/apps/details?id=com.mizmowireless.acctmgt&hl=en_US&gl=US", #MyCricket
    "https://play.google.com/store/apps/details?id=com.dish.mydish&hl=en_US&gl=US", #MyDishAccount
    "https://play.google.com/store/apps/details?id=com.tmobile.pr.mytmobile&hl=en_US&gl=US", #T-Mobile
    "https://play.google.com/store/apps/details?id=com.xfinitymobile.myaccount&hl=en_US&gl=US", #XfinityMobile
    "https://play.google.com/store/apps/details?id=com.twcable.twcnews&hl=en_US&gl=US", #SpectrumNews
    "https://play.google.com/store/apps/details?id=com.brighthouse.mybhn&hl=en_US&gl=US", #MySpectrumApp
    "https://play.google.com/store/apps/details?id=com.sprint.care&hl=en_US&gl=US", #MySprintMobile
    "https://play.google.com/store/apps/details?id=com.verizon.myfios&hl=en_US&gl=US", #VerizonMyFios
    "https://play.google.com/store/apps/details?id=com.centurylink.ctl_droid_wrap&hl=en_US&gl=US", #MyCenturyLink
    "https://play.google.com/store/apps/details?id=com.visiblemobile.flagship&hl=en_US&gl=US", #VisibleMobile
    "https://play.google.com/store/apps/details?id=com.charter.university&hl=en_US&gl=US", #SpectrumU
    "https://play.google.com/store/apps/details?id=com.TWCableTV&hl=en_US&gl=US", #SpectrumTV
    "https://play.google.com/store/apps/details?id=com.att.myWireless&hl=en_US&gl=US", #MyATT
    "https://play.google.com/store/apps/details?id=com.twcsports.android&hl=en_US&gl=US", #SpectrumSportsNet
    "https://play.google.com/store/apps/details?id=com.speechcycle.smartcare.android.mediacom&hl=en_US&gl=US", #MediacomConnect
    "https://play.google.com/store/apps/details?id=com.nuance.nmc.sihome.metropcs&hl=en_US&gl=US", #MyMetro
    "https://play.google.com/store/apps/details?id=com.frontier.selfserve&hl=en_US&gl=US", #MyFrontier
    "https://play.google.com/store/apps/details?id=com.xfinity.digitalhome&hl=en_US&gl=US", #XfinityMyAccount
    "https://play.google.com/store/apps/details?id=com.google.android.apps.fiber.myfiber&hl=en_US&gl=US", #GoogleFiber
    "https://play.google.com/store/apps/details?id=com.viasat.cts.store.ViasatInternet&hl=en_US&gl=US", #MyViasat
    "https://play.google.com/store/apps/details?id=agoc.mobile.account&hl=en_US&gl=US", #ArmStrong
    "https://play.google.com/store/apps/details?id=com.astound.mobile.rcn&hl=en_US&gl=US", #RCN_Mobile #Astound_Mobile
    "https://play.google.com/store/apps/details?id=com.hughesnet.HughesNetMobile&hl=en_US&gl=US", #HughesNet_Mobile
    "https://play.google.com/store/apps/details?id=com.hawaiiantel.myht&hl=en_US&gl=US", #HT_MyAccount
    "https://play.google.com/store/apps/details?id=com.midco.consumerapp&hl=en_US&gl=US", #MidcoMyAccount
    "https://play.google.com/store/apps/details?id=com.optimum.lbsaopt&hl=en_US&gl=US", #OptimumSupport
    "https://play.google.com/store/apps/details?id=com.uscc.myaccount&hl=en_US&gl=US", #US_Cellular_My_Account
    "https://play.google.com/store/apps/details?id=com.sectv.mysectv&hl=en_US&gl=US", #MySecTV
    "https://play.google.com/store/apps/details?id=com.alticeusa.alticeone.prod&hl=en_US&gl=US", #OptimumTV
    "https://play.google.com/store/apps/details?id=com.tivo.android.abb&hl=en_US&gl=US", #BreezelineTV
    "https://play.google.com/store/apps/details?id=com.brctv.myblueridge&hl=en_US&gl=US", #MyBlueRidge
    "https://play.google.com/store/apps/details?id=com.buckeyebroadband.mybuckeye&hl=en_US&gl=US" #MyBuckeye
]
dataAndroid = []
for link in urlAndroid:
    resultAndroid = requests.get(link)
    soupAndroid = BeautifulSoup(resultAndroid.content, "html.parser")
    starRatingRaw = soupAndroid.find("div", {"class": "TT9eCd"})

    if starRatingRaw is not None:
        starRating = starRatingRaw.text.replace("star", "")
    else:
        starRating = ""

    appName = soupAndroid.find("h1", {"itemprop": "name"})
    appName = appName.text

    temp_list = [None] * 8
    temp_list[0] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Date
    temp_list[6] = starRating  # Star Rating
    temp_list[7] = appName  # App Name

    divReviews = soupAndroid.find_all("div", {"class": "RutFAf wcB8se"})
    if divReviews:
        for i, div in enumerate(divReviews):
            countReviewsRaw = div['title']
            countReviews = countReviewsRaw.replace(",", "")
            temp_list[i + 1] = int(countReviews)

    dataAndroid.append(temp_list)

dataAndroid = pd.DataFrame(dataAndroid, columns=['Date', 'Android 5 Star Reviews', 'Android 4 Star Reviews', 'Android 3 Star Reviews', 'Android 2 Star Reviews', 'Android 1 Star Reviews', 'Android App Rating', 'App Name'])

dataAndroid['Android Total Reviews'] = dataAndroid.loc[:, 'Android 5 Star Reviews':'Android 1 Star Reviews'].sum(1)
dataAndroid = dataAndroid[['Date', 'App Name', 'Android App Rating', 'Android Total Reviews', 'Android 5 Star Reviews', 'Android 4 Star Reviews', 'Android 3 Star Reviews', 'Android 2 Star Reviews', 'Android 1 Star Reviews']]

dataAndroid.to_excel('AndroidRatings.xlsx', index=False)