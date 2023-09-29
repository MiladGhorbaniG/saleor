from django.db import models
from ..graphql.attribute.enums import AttributeInputTypeEnum, AttributeEntityTypeEnum

# Define choices for the input_type and entity_type fields
INPUT_TYPE_CHOICES = [
    (choice.name, choice.name)
    for choice in AttributeInputTypeEnum._meta.enum.values()
]

ENTITY_TYPE_CHOICES = [
    (choice.name, choice.name)
    for choice in AttributeEntityTypeEnum._meta.enum.values()
]

class CustomAttribute(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    input_type = models.CharField(
        max_length=50,
        choices=INPUT_TYPE_CHOICES,
    )
    entity_type = models.CharField(
        max_length=50,
        choices=ENTITY_TYPE_CHOICES,
    )
    unit = models.CharField(max_length=50, blank=True, null=True)
    choices = models.JSONField(default=list)  # Store choices as JSON data

    def __str__(self):
        return self.name
