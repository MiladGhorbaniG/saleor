from django.db import models
from ..attribute import AttributeInputTypeEnum, AttributeEntityTypeEnum

class CustomAttribute(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    input_type = models.CharField(
        max_length=50,
        choices=AttributeInputTypeEnum.CHOICES,
    )
    entity_type = models.CharField(
        max_length=50,
        choices=AttributeEntityTypeEnum.CHOICES,
    )
    unit = models.CharField(max_length=50, blank=True, null=True)
    choices = models.JSONField(default=list)  # Store choices as JSON data

    def __str__(self):
        return self.name
