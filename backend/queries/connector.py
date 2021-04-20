import logging as log
import time
from json import dumps
import matplotlib.pyplot as plt

from neo4j import GraphDatabase

log.basicConfig(level=log.INFO)

class Connector:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)

    def Session(self):
        return self._driver.session()

    def Close(self):
        self._driver.close()

    def RemoveAll(self):
        with self._driver.session() as session:
            session.write_transaction(self._remove_all)

    def InsertUsers(self, users):
        with self._driver.session() as session:
            session.write_transaction(self._create_users, users)

    def QueryUserData(self):
        # NOTE: This a simple function that will query user data.
        # Then It will build and return a json representation of the network

        db = self.Session()
        results = db.run("")
        return results


    @staticmethod
    def _remove_all(tx):
        tx.run("MATCH (n) DETACH DELETE n")

    @staticmethod
    def _create_users(tx, classes):
        pass


    def InsertTest(self):
        # Dummy function for inserting test data
        # remove it if you do not need it
        with self._driver.session() as session:
            session.write_transaction(self._create_test)

    @staticmethod
    def _create_test(tx):
        pass
