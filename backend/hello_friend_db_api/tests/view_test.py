from django.test import TestCase
from neomodel import db, clear_neo4j_database
from hello_friend_db_api.models import User
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
import django
django.setup()

class ViewTestClass(TestCase):

    def test_view_user(self):
        print("Method: test_view_user.")
        pass
