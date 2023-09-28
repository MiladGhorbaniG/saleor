import graphene
from graphene import ObjectType, ID, InputObjectType, String
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.core.exceptions import PermissionDenied
from graphql_jwt.decorators import permission_required

from ...product.models import Product, ProductVariant

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"
        interfaces = (graphene.relay.Node,)

class ProductVariantType(DjangoObjectType):
    class Meta:
        model = ProductVariant
        fields = "__all__"
        interfaces = (graphene.relay.Node,)

class ProductInput(InputObjectType):
    name = String(required=True)
    slug = String(required=True)

class ProductVariantInput(InputObjectType):
    name = String()
    sku = String()

class CreateProductMutation(graphene.Mutation):
    class Arguments:
        input_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @permission_required("add_product")  # Adjust the permission as needed
    def mutate(self, info, input_data):
        product = Product(**input_data)
        product.save()
        return CreateProductMutation(product=product)


class UpdateProductMutation(graphene.Mutation):
    class Arguments:
        id = ID(required=True)
        input_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @permission_required("change_product")  # Adjust the permission as needed
    def mutate(self, info, id, input_data):
        if not info.context.user.has_perm('change_product'):
            raise PermissionDenied("You do not have permission to update this product.")

        product = Product.objects.get(pk=id)
        for attr, value in input_data.items():
            setattr(product, attr, value)
        product.save()
        return UpdateProductMutation(product=product)

class CreateProductVariantMutation(graphene.Mutation):
    class Arguments:
        input_data = ProductVariantInput(required=True)

    product_variant = graphene.Field(ProductVariantType)

    @permission_required("add_productvariant")  # Adjust the permission as needed
    def mutate(self, info, input_data):
        if not info.context.user.has_perm('add_productvariant'):
            raise PermissionDenied("You do not have permission to create a product variant.")
        product_variant = ProductVariant(**input_data)
        product_variant.save()
        return CreateProductVariantMutation(product_variant=product_variant)

class UpdateProductVariantMutation(graphene.Mutation):
    class Arguments:
        id = ID(required=True)
        input_data = ProductVariantInput(required=True)

    product_variant = graphene.Field(ProductVariantType)

    @permission_required("change_productvariant")  # Adjust the permission as needed
    def mutate(self, info, id, input_data):
        if not info.context.user.has_perm('change_productvariant'):
            raise PermissionDenied("You do not have permission to update this product variant.")
        
        product_variant = ProductVariant.objects.get(pk=id)
        for attr, value in input_data.items():
            setattr(product_variant, attr, value)
        product_variant.save()
        return UpdateProductVariantMutation(product_variant=product_variant)

class Query(ObjectType):
    product = graphene.Field(ProductType, id=ID(required=True))
    all_products = DjangoFilterConnectionField(ProductType)
    product_variant = graphene.Field(ProductVariantType, id=ID(required=True))
    all_product_variants = DjangoFilterConnectionField(ProductVariantType)

    def resolve_product(self, info, id):
        if info.context.user.has_perm('view_product'):
            return Product.objects.get(pk=id)
        else:
            raise PermissionDenied("You do not have permission to view this product.")

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product_variant(self, info, id):
        return ProductVariant.objects.get(pk=id)

    def resolve_all_product_variants(self, info, **kwargs):
        return ProductVariant.objects.all()

class Mutation(ObjectType):
    create_product = CreateProductMutation.Field()
    update_product = UpdateProductMutation.Field()
    create_product_variant = CreateProductVariantMutation.Field()
    update_product_variant = UpdateProductVariantMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
