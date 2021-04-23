import logging as log
import os
import time
from dotenv import load_dotenv

import pandas as pd
import random

from models.user import User
from queries.connector import Connector

# Load environment variables
load_dotenv()

# Database user credentials
DB_URI: str = os.getenv("DB_URI")
DB_USER: str = os.getenv("DB_USER")
DB_PASSWORD: str = os.getenv("DB_PASSWORD")

# Debugging
# log.basicConfig(level=log.DEBUG)
log.basicConfig(level=log.INFO)

def LoadData(filename):
    # NOTE: Loading dummy data for now 
    users = []
    links = []
    for user in range(20):
        u = User("u_"+str(user+1), random.randrange(20,23), "M")
        users.append(u)

    for link in range(50):
        u1 = random.randrange(1,21)
        u2 = random.randrange(1,21)
        if u1 != u2:
            links.append(("u_"+str(u1), "u_"+str(u2)))
    return users, links


if __name__ == "__main__":
    # New connector (it will be used for querying the database)
    log.info("creating db connector...\n")
    connector = Connector(DB_URI, DB_USER, DB_PASSWORD)

    # NOTE: This will all nodes and links from the database
    # please omit this if you do not want to remove your data
    connector.RemoveAll()

    # Loading user from file (data/directory)
    log.info("loading user data...\n")
    users, links = LoadData("<user-data-file-path>")
    if len(users) == 0:
        raise Exception('Error while loading user data; no data')
    if len(links) == 0:
        log.warning('There are no links in the data...\n')

    # Inserting user data into the database
    log.info("inserting user data...\n")
    connector.InsertUsers(users)

    # Inserting friend links into the database
    log.info("inserting friend links...\n")
    connector.InsertLinks(links)

    # NOTE: This dummy method can be used for testing functionality of the database
    # connector.InsertTest()

    # NOTE: This method gives user info
    # log.info("querying user data...\n")
    # response = connector.QueryUserData()
    # print(response)

    # Closing db connection
    log.info("closing connector...\n")
    connector.Close()
