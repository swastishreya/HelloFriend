from django.apps import AppConfig
import logging

logging.basicConfig(filename="logFile.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class HelloFriendDbApiConfig(AppConfig):
    logging.info("Setting up App Config for Hello Friend Backend...")
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello_friend_db_api'
