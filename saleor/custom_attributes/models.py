from django.db import models
from ..graphql.attribute.enums import AttributeInputTypeEnum, AttributeEntityTypeEnum

# Function to convert GraphQL enum to Django model choices
def get_input_type_choices():
    return [(choice.name, choice.name) for choice in AttributeInputTypeEnum]

def get_entity_type_choices():
    return [(choice.name, choice.name) for choice in AttributeEntityTypeEnum]

class CustomAttribute(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    # Use the functions to get choices
    input_type = models.CharField(
        max_length=50,
        choices=get_input_type_choices(),
    )
    entity_type = models.CharField(
        max_length=50,
        choices=get_entity_type_choices(),
    )

    unit = models.CharField(max_length=50, blank=True, null=True)
    choices = models.JSONField(default=list)  # Store choices as JSON data

    def __str__(self):
        return self.name
