import graphene

from ...attribute import AttributeEntityType, AttributeInputType, AttributeType
from ..core.doc_category import DOC_CATEGORY_ATTRIBUTES
from ..core.utils import str_to_enum

# Create a GraphQL enum for AttributeInputType
class AttributeInputTypeEnum(graphene.Enum):
    STRING = "STRING"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"

    # Add more attribute input types as needed

    class Meta:
        description = "Attribute input types."
        doc_category = DOC_CATEGORY_ATTRIBUTES

# Create a GraphQL enum for AttributeType
class AttributeTypeEnum(graphene.Enum):
    PRODUCT = "PRODUCT"
    VARIANT = "VARIANT"

    # Add more attribute types as needed

    class Meta:
        description = "Attribute types."
        doc_category = DOC_CATEGORY_ATTRIBUTES

# Create a GraphQL enum for AttributeEntityType
class AttributeEntityTypeEnum(graphene.Enum):
    PRODUCT = "PRODUCT"
    VARIANT = "VARIANT"

    # Add more attribute entity types as needed

    class Meta:
        description = "Attribute entity types."
        doc_category = DOC_CATEGORY_ATTRIBUTES

# Optionally, you can set descriptions and doc categories for each enum.
AttributeInputTypeEnum._meta.description = "Attribute input types."
AttributeTypeEnum._meta.description = "Attribute types."
AttributeEntityTypeEnum._meta.description = "Attribute entity types."

# Map Django enum choices to GraphQL enum values for AttributeEntityTypeEnum
AttributeEntityTypeEnum._meta.enum = {
    str_to_enum(name.upper()): code for code, name in AttributeEntityType.CHOICES
}
