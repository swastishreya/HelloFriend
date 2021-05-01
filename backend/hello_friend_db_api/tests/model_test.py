from django.test import TestCase
from neomodel import db, clear_neo4j_database
from hello_friend_db_api.models import User
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()

class ModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        clear_neo4j_database(db)
        user1 = User(name='Swasti', age=22, gender='Female')
        user1.save()
        user2 = User(name='Gurleen', age=21, gender='Female')
        user2.save()
        res = user1.friends.connect(user2)

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     clear_neo4j_database(db)

    def test_save_model_user(self):
        print("Method: test_save_model_user.")      
        fetch_user1 = User.nodes.get(name='Swasti')
        assert fetch_user1 is not None
        fetch_user2 = User.nodes.get(name='Gurleen')
        assert fetch_user2 is not None

    def test_unique_uid(self):
        print("Method: test_unique_uid.")    
        fetch_user1 = User.nodes.get(name='Swasti')
        fetch_user2 = User.nodes.get(name='Gurleen')
        self.assertNotEqual(fetch_user1.uid, fetch_user2.uid) 

    def test_model_user_relation(self):
        fetch_user1 = User.nodes.get(name='Swasti')
        fetch_user2 = User.nodes.get(name='Gurleen')
        self.assertTrue(fetch_user1.friends.is_connected(fetch_user2))

    def clearTestData(self):
        clear_neo4j_database(db)
        fetch_user1 = User.nodes.get(name='Swasti')
        fetch_user2 = User.nodes.get(name='Gurleen')
        self.assertIsNone(fetch_user1)
        self.assertIsNone(fetch_user2)
