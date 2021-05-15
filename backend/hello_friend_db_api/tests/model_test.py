from django.test import TestCase
from neomodel import db, clear_neo4j_database
from hello_friend_db_api.models import *
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()

class ModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        clear_neo4j_database(db)
        user1 = User(name='Swasti', age=22, gender='Female', email='swamishr@adobe.com', password='swasti123', interests=['Anime', 'Painting', 'Dancing', 'Computer Vision', 'Dogs'])
        user1.save()
        user2 = User(name='Gurleen', age=21, gender='Female', email='ginni@goldmansachs.com', password='ginni123', interests=['Painting', 'Computer Vision', 'Dogs', 'Writing'])
        user2.save()
        res = user1.friends.connect(user2)

    def test_save_model_user(self):
        print("Method: test_save_model_user.")      
        fetch_user1 = User.nodes.get(name='Swasti')
        for interest in fetch_user1.interests:
            interest_node = None
            try:
                interest_node = Interest.nodes.get(name=interest)
            except:
                interest_node = Interest(name=interest)
                interest_node.save()
            fetch_user1.interestedIn.connect(interest_node)
        assert fetch_user1 is not None
        fetch_user2 = User.nodes.get(name='Gurleen')
        for interest in fetch_user2.interests:
            interest_node = None
            try:
                interest_node = Interest.nodes.get(name=interest)
            except:
                interest_node = Interest(name=interest)
                interest_node.save()
            fetch_user2.interestedIn.connect(interest_node)
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

    def test_model_user_similarity(self):
        sim, common_interest = User.getSimilarity('Swasti', 'Gurleen')
        self.assertEqual(sim, 3)

    def clearTestData(self):
        clear_neo4j_database(db)
        fetch_user1 = User.nodes.get(name='Swasti')
        fetch_user2 = User.nodes.get(name='Gurleen')
        self.assertIsNone(fetch_user1)
        self.assertIsNone(fetch_user2)
