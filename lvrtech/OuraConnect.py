import json
import requests
from datetime import datetime, timedelta

from .dbconnect import create_user_info
from .dbconnect import create_activity
from .dbconnect import get_all_users
from .dbconnect import get_all_userinfo

baseurl = "https://api.ouraring.com/v1"

def make_base_url(accesstoken, entity, start_date, end_date):
    if start_date == None:
        start_date = datetime.now() - timedelta(7)
        start_date = datetime.strftime(start_date, '%Y-%m-%d')
    url = ''
    
    if end_date == None:
        url = f"{baseurl}/{entity}?access_token={accesstoken}&start={start_date}"
    else:
        url = f"{baseurl}/{entity}?access_token={accesstoken}&end={end_date}"

    return url

def get_user_info(accesstoken):
    url = f"{baseurl}/userinfo/?access_token={accesstoken}"
    userinfo = requests.get(f"{baseurl}/userinfo?access_token={accesstoken}").json()
    create_user_info(accesstoken, userinfo["age"], userinfo["weight"], userinfo["height"], userinfo["gender"], userinfo["email"])
    return userinfo

def get_readiness_summary(accesstoken, start_date=None, end_date=None):
    readiness_summary = requests.get(make_base_url(accesstoken, "readiness", start_date, end_date)).json()    
    return readiness_summary

def get_activity_summary(accesstoken, start_date=None, end_date=None):
    activity_summary = requests.get(make_base_url(accesstoken, "activity", start_date, end_date)).json()
    create_activity(accesstoken, activity_summary)    
    return activity_summary

def get_sleep_summary(accesstoken, start_date=None, end_date=None):
    sleep_summary = requests.get(make_base_url(accesstoken, "sleep", start_date, end_date)).json()
    return sleep_summary   

def refresh_all_data():
    users = get_all_userinfo()
    for user in users:
        get_user_info(user[0])
        get_activity_summary(user[0])