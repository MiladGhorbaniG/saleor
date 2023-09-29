import graphene
from ...attribute import AttributeEntityType, AttributeInputType, AttributeType
from ..core.doc_category import DOC_CATEGORY_ATTRIBUTES
from ..core.enums import to_enum
from ..core.utils import str_to_enum

# Define AttributeInputTypeEnum
AttributeInputTypeEnum = to_enum(AttributeInputType)

# Create a new Enum for AttributeInputTypeEnum with a description
class AttributeInputTypeEnumWithDescription(graphene.Enum):
    DESCRIPTION = "Attribute input types."
    DOC_CATEGORY = DOC_CATEGORY_ATTRIBUTES
    @classmethod
    def get_description(cls):
        return cls.DESCRIPTION

    @classmethod
    def get_doc_category(cls):
        return cls.DOC_CATEGORY

    @classmethod
    def get_enum_name(cls, enum_value):
        return enum_value.name

# Define AttributeTypeEnum
AttributeTypeEnum = to_enum(AttributeType)

# Create a new Enum for AttributeTypeEnum with a description
class AttributeTypeEnumWithDescription(graphene.Enum):
    DESCRIPTION = "Attribute types."
    DOC_CATEGORY = DOC_CATEGORY_ATTRIBUTES
    @classmethod
    def get_description(cls):
        return cls.DESCRIPTION

    @classmethod
    def get_doc_category(cls):
        return cls.DOC_CATEGORY

    @classmethod
    def get_enum_name(cls, enum_value):
        return enum_value.name

# Define AttributeEntityTypeEnum
AttributeEntityTypeEnum = to_enum(AttributeEntityType)

# Create a new Enum for AttributeEntityTypeEnum with a description
class AttributeEntityTypeEnumWithDescription(graphene.Enum):
    DESCRIPTION = "Attribute entity types."
    DOC_CATEGORY = DOC_CATEGORY_ATTRIBUTES
    @classmethod
    def get_description(cls):
        return cls.DESCRIPTION

    @classmethod
    def get_doc_category(cls):
        return cls.DOC_CATEGORY

    @classmethod
    def get_enum_name(cls, enum_value):
        return enum_value.name
