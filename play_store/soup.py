import pandas as pd
from bs4 import BeautifulSoup
import requests

from play_store.models import AppPackage, AppDetails, AppComments
from google_play_scraper import app

def package_name_scrapper():
    # create user agent
    headers = {"USer-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
                             "Safari/537.36"}

    # get website
    response = requests.get('https://play.google.com/store/games?hl=en&gl=US', headers=headers)

    # fetch content
    webpage = response.content

    # create beautiful soup object
    soup = BeautifulSoup(webpage, "html.parser")


    # here we get a tag which contains href having package name
    data_set = soup.find_all('a', class_='Si6A0c')

    #here we will delete old data packages we can store it, but always we need  new scraped packages
    AppPackage.objects.all().delete()

    for data in data_set:
        """here we will get href here and will extract app package name"""
        href = data['href']
        if '/store/apps/details?id' in href:
            """After that we will Store GamePackage in DB"""
            package_name = href.split('=')[1]
            AppPackage.objects.get_or_create(package_name=package_name)


def package_details_scrapper():

    packages = AppPackage.objects.all().values_list('package_name','id')
    AppDetails.objects.all().delete()
    AppComments.objects.all().delete()
    for package in packages:

        app_data = app(
            package[0],
            lang='en',  # defaults to 'en'
            country='us'  # defaults to 'us'
        )

        install_count = int(app_data['realInstalls']) if app_data['realInstalls'] else 0
        price = int(app_data['price']) if app_data['installs'] else 0
        ratings = int(app_data['ratings']) if app_data['ratings'] else 0
        score = float(app_data['score']) if app_data['score'] else 0.0

        AppDetails.objects.get_or_create(
            app_package=AppPackage.objects.get(id=package[1]),
            title=app_data['title'],
            description=app_data['description'],
            developerAddress=app_data['developerAddress'],
            summary=app_data['summary'],
            installs=app_data['installs'],
            install_count=install_count,
            score=score,
            ratings=ratings,
            reviews=app_data['reviews'],
            developerId=app_data['developerId'],
            version=app_data['version'],
            video=app_data['video'],
            icon=app_data['icon'],
            developerWebsite=app_data['developerWebsite'],
            privacyPolicy=app_data['privacyPolicy'],
            genre=app_data['genre'],
            developer=app_data['developer'],
            free=app_data['free'],
            price=price,
        )
        AppComments.objects.bulk_create(
            [AppComments(**{'app_details': AppDetails.objects.filter(title = app_data['title']).first(), 'comments': item}) for item in
             app_data['comments']])

