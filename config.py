import os

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://molasa7348:29TiLiVemOcKUmxf@cluster0.9dkky.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "offerlinks.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "2b491547a49b1d8274e9a619c8258029ef2b8bd0")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/ultroid_official/18") # shareus ka tut_vid he 