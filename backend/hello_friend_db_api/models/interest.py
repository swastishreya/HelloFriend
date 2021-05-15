from neomodel import StructuredNode, StringProperty, UniqueIdProperty


class Interest(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)