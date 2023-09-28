import graphene
from graphene import ObjectType, Decimal, ID, InputObjectType, String
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ...product.models import Product, ProductVariant

# Define the GraphQL types for Product and ProductVariant
class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = "__all__"  # Include all fields from the Product model
        interfaces = (graphene.relay.Node,)

class ProductVariantType(DjangoObjectType):
    class Meta:
        model = ProductVariant
        fields = "__all__"  # Include all fields from the ProductVariant model
        interfaces = (graphene.relay.Node,)

# Define input types for creating or updating Product and ProductVariant
class ProductInput(InputObjectType):
    name = String(required=True)
    slug = String(required=True)
    # Include other fields that you want to allow for creation or update

class ProductVariantInput(InputObjectType):
    name = String()
    sku = String()
    # Include other fields that you want to allow for creation or update

# Define mutations for creating and updating Product instances
class CreateProductMutation(graphene.Mutation):
    class Arguments:
        input_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, input_data):
        product = Product(**input_data)
        product.save()
        return CreateProductMutation(product=product)

class UpdateProductMutation(graphene.Mutation):
    class Arguments:
        id = ID(required=True)
        input_data = ProductInput(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, id, input_data):
        product = Product.objects.get(pk=id)
        for attr, value in input_data.items():
            setattr(product, attr, value)
        product.save()
        return UpdateProductMutation(product=product)

# Define mutations for creating and updating ProductVariant instances (similar to Product mutations)
class CreateProductVariantMutation(graphene.Mutation):
    class Arguments:
        input_data = ProductVariantInput(required=True)

    product_variant = graphene.Field(ProductVariantType)

    def mutate(self, info, input_data):
        product_variant = ProductVariant(**input_data)
        product_variant.save()
        return CreateProductVariantMutation(product_variant=product_variant)

class UpdateProductVariantMutation(graphene.Mutation):
    class Arguments:
        id = ID(required=True)
        input_data = ProductVariantInput(required=True)

    product_variant = graphene.Field(ProductVariantType)

    def mutate(self, info, id, input_data):
        product_variant = ProductVariant.objects.get(pk=id)
        for attr, value in input_data.items():
            setattr(product_variant, attr, value)
        product_variant.save()
        return UpdateProductVariantMutation(product_variant=product_variant)

# Define your custom queries related to products and variants
class Query(ObjectType):
    product = graphene.Field(ProductType, id=ID(required=True))
    all_products = DjangoFilterConnectionField(ProductType)
    product_variant = graphene.Field(ProductVariantType, id=ID(required=True))
    all_product_variants = DjangoFilterConnectionField(ProductVariantType)

    def resolve_product(self, info, id):
        return Product.objects.get(pk=id)

    def resolve_all_products(self, info, **kwargs):
        return Product.objects.all()

    def resolve_product_variant(self, info, id):
        return ProductVariant.objects.get(pk=id)

    def resolve_all_product_variants(self, info, **kwargs):
        return ProductVariant.objects.all()

# Define mutations by creating a Mutation class
class Mutation(ObjectType):
    create_product = CreateProductMutation.Field()
    update_product = UpdateProductMutation.Field()
    create_product_variant = CreateProductVariantMutation.Field()
    update_product_variant = UpdateProductVariantMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
