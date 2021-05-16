from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, ArrayProperty,  Relationship
from neomodel.match import Traversal, EITHER
from hello_friend_db_api.models.interest import Interest

class User(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    gender = StringProperty(index=True, default="Female")
    password = StringProperty(index=True)
    email = StringProperty(index=True)
    interests = ArrayProperty(StringProperty(),index=True, required=True)

    #Relations
    friends = Relationship('User', 'FRIEND')
    interestedIn = Relationship('Interest', 'INTERESTED')

    def getSimilarity(user1, user2):
        user1 = User.nodes.get(name=user1)
        user2 = User.nodes.get(name=user2)
        set1 = set(user1.interests)
        set2 = set(user2.interests)
        common_interest = set1.intersection(set2)
        print(common_interest)
        return len(common_interest), common_interest

    def getSimilarityWithInterests(interests1, interests2):
        set1 = set(interests1)
        set2 = set(interests2)
        common_interest = set1.intersection(set2)
        print(common_interest)
        return len(common_interest), common_interest

    def getTraversal(user1):
        user1 = User.nodes.get(name=user1)
        definition = dict(node_class=User, direction=EITHER,
                  relation_type=None, model=None)
        relations_traversal1 = Traversal(user1, User.__label__,
                                definition)
        all_user1_relations = relations_traversal1.all()
        return all_user1_relations