from django.db import models
from ..graphql.attribute.enums import AttributeInputTypeEnum, AttributeEntityTypeEnum

class CustomAttribute(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    # Convert the enum to a list of tuples for choices
    input_type = models.CharField(
        max_length=50,
        choices=AttributeInputTypeEnum.get_choices(),
    )
    entity_type = models.CharField(
        max_length=50,
        choices=AttributeEntityTypeEnum.get_choices(),
    )

    unit = models.CharField(max_length=50, blank=True, null=True)
    choices = models.JSONField(default=list)  # Store choices as JSON data

    def __str__(self):
        return self.name
