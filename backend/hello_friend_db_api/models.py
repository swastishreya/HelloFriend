# from django.db import models

from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo


class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    gender = StringProperty(index=True, default="Female")

    #Relations
    friends = RelationshipTo('User', 'FRIEND')