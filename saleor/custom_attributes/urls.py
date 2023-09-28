from django.urls import path
from . import views
from .schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path("", views.list_custom_attributes, name="list-custom-attributes"),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema), name="graphql"),
]