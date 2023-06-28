from celery import shared_task

from play_store.soup import package_details_scrapper


@shared_task
def app_details_task():
    """
    This Function Fetch data From google-play-scraper and save to database
    """
    return package_details_scrapper()

