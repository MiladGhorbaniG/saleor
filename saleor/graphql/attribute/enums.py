import graphene
from ...attribute import AttributeEntityType, AttributeInputType, AttributeType
from ..core.doc_category import DOC_CATEGORY_ATTRIBUTES
from ..core.enums import to_enum
from ..core.utils import str_to_enum

# Define AttributeInputTypeEnum
AttributeInputTypeEnum = to_enum(AttributeInputType)
AttributeInputTypeEnum._meta.description = "Attribute input types."
AttributeInputTypeEnum.doc_category = DOC_CATEGORY_ATTRIBUTES

# Define AttributeTypeEnum
AttributeTypeEnum = to_enum(AttributeType)
AttributeTypeEnum._meta.description = "Attribute types."
AttributeTypeEnum.doc_category = DOC_CATEGORY_ATTRIBUTES

# Define AttributeEntityTypeEnum
AttributeEntityTypeEnum = to_enum(AttributeEntityType)
AttributeEntityTypeEnum._meta.description = "Attribute entity types."
AttributeEntityTypeEnum.doc_category = DOC_CATEGORY_ATTRIBUTES

# Create a new Enum for AttributeEntityTypeEnum
NewAttributeEntityTypeEnum = graphene.Enum(
    "AttributeEntityTypeEnum",
    [(str_to_enum(name.upper()), code) for code, name in AttributeEntityType.CHOICES],
)
NewAttributeEntityTypeEnum._meta.description = "Attribute entity types."
NewAttributeEntityTypeEnum.doc_category = DOC_CATEGORY_ATTRIBUTES
