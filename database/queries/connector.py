import logging as log
from json import dumps

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

    def InsertLinks(self, links):
        with self._driver.session() as session:
            session.write_transaction(self._create_links, links)

    @staticmethod
    def _remove_all(tx):
        tx.run("MATCH (n) DETACH DELETE n")

    @staticmethod
    def _create_users(tx, users):
        for user in users:
            tx.run(
                "CREATE (u:User {name: $username, age: $user_age, gender: $user_gender})",
                parameters={
                    "username": user.Name,
                    "user_age": user.Age,
                    "user_gender": user.Gender,
                }
            )

    @staticmethod
    def _create_links(tx, links):
        for link in links:
            u1 = link[0]
            u2 = link[1]
            tx.run(
                "MATCH (u1:User{name: $username1})"
                "MATCH (u2:User{name: $username2})"
                "MERGE (u1)-[:FRIEND_OF]->(u2)"
                "MERGE (u1)<-[:FRIEND_OF]-(u2)",
                parameters={
                    "username1": u1,
                    "username2": u2,
                }
            )


    def InsertTest(self):
        # Dummy function for inserting test data
        # remove it if you do not need it
        with self._driver.session() as session:
            session.write_transaction(self._create_test)

    @staticmethod
    def _create_test(tx):
        pass
