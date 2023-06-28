# App Store

- First Take Pull
- create environment
- install requirements ( pip install -r [requirements.txt](requirements.txt))
- for database run python manage.py migrate or python3 manage.py migrate

# Install RebbitMq Globally
- install **sudo apt-get install rabbitmq-server**
- After that, RabbitMQ starts and is enabled on boot. You can check this by using:
 **systemctl status rabbitmq-server.service** 
- If it reverts back disabled, enable it with the following command:
 **sudo systemctl enable rabbitmq-server**

# Start Server and Celery
- To start django server locally run: **python manage.py runserver**
- To start celery server locally run: **celery -A DjangoCeleryScrap worker --loglevel=INFO**

# API
- Scrape Packages : POST http://127.0.0.1:8000/package/ 
- List Scraped Packages : GET http://127.0.0.1:8000/package/ 
- Scrape App Details : POST http://127.0.0.1:8000/app_details/
- List Scraped App Details : GET http://127.0.0.1:8000/app_details/
