from django.http import JsonResponse
from .models import CustomAttribute

def list_custom_attributes(request):
    attributes = CustomAttribute.objects.all()
    data = [
        {
            "name": attribute.name,
            "slug": attribute.slug,
            "input_type": attribute.input_type,
            "entity_type": attribute.entity_type,
            "unit": attribute.unit,
            "choices": [
                {
                    "name": choice.name,
                    "slug": choice.slug,
                }
                for choice in attribute.choices.all()
            ],
        }
        for attribute in attributes
    ]
    return JsonResponse(data, safe=False)