import graphene
from ...attribute import AttributeEntityType, AttributeInputType, AttributeType
from ..core.doc_category import DOC_CATEGORY_ATTRIBUTES
from ..core.enums import to_enum
from ..core.utils import str_to_enum

# Define AttributeInputTypeEnum
AttributeInputTypeEnum = to_enum(AttributeInputType)

# Create a new Enum for AttributeInputTypeEnum with a description
AttributeInputTypeEnumWithDescription = graphene.Enum(
    "AttributeInputTypeEnumWithDescription",
    [(str_to_enum(name.upper()), code) for code, name in AttributeInputType.CHOICES],
)
AttributeInputTypeEnumWithDescription._meta.description = "Attribute input types."
AttributeInputTypeEnumWithDescription.doc_category = DOC_CATEGORY_ATTRIBUTES

# Define AttributeTypeEnum
AttributeTypeEnum = to_enum(AttributeType)

# Create a new Enum for AttributeTypeEnum with a description
AttributeTypeEnumWithDescription = graphene.Enum(
    "AttributeTypeEnumWithDescription",
    [(str_to_enum(name.upper()), code) for code, name in AttributeType.CHOICES],
)
AttributeTypeEnumWithDescription._meta.description = "Attribute types."
AttributeTypeEnumWithDescription.doc_category = DOC_CATEGORY_ATTRIBUTES

# Define AttributeEntityTypeEnum
AttributeEntityTypeEnum = to_enum(AttributeEntityType)

# Create a new Enum for AttributeEntityTypeEnum with a description
AttributeEntityTypeEnumWithDescription = graphene.Enum(
    "AttributeEntityTypeEnumWithDescription",
    [(str_to_enum(name.upper()), code) for code, name in AttributeEntityType.CHOICES],
)
AttributeEntityTypeEnumWithDescription._meta.description = "Attribute entity types."
AttributeEntityTypeEnumWithDescription.doc_category = DOC_CATEGORY_ATTRIBUTES
