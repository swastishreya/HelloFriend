import logging as log
import os
import time
# from dotenv import load_dotenv

import pandas as pd

from models.user import User
from queries.connector import Connector

# Load environment variables
# load_dotenv()

# Database user credentials
DB_URI: str = os.getenv("DB_URI")
DB_USER: str = os.getenv("DB_USER")
DB_PASSWORD: str = os.getenv("DB_PASSWORD")

# Debugging
# log.basicConfig(level=log.DEBUG)
log.basicConfig(level=log.INFO)

def LoadData(filename):
    response = []
    return response


if __name__ == "__main__":
    # New connector (it will be used for querying the database)
    log.info("creating db connector...")
    connector = Connector(DB_URI, DB_USER, DB_PASSWORD)

    # NOTE: This will all nodes and links from the database
    # please omit this if you do not want to remove your data
    connector.RemoveAll()

    # Loading user from file (data/directory)
    log.info("loading user data...")
    users = LoadData("<user-data-file-path>")
    if len(users) == 0:
        raise Exception('Error while loading user data; no data')

    # Inserting user data into the database
    log.info("inserting user data...")
    connector.InsertUsers(users)

    # NOTE: This dummy method can be used for testing functionality of the database
    # connector.InsertTest()

    # NOTE: This method gives user info
    log.info("querying user data...")
    response = connector.QueryUserData()
    print(response)

    # Closing db connection
    log.info("closing connector...")
    connector.Close()
