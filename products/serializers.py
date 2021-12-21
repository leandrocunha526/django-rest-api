from rest_flex_fields import FlexFieldsModelSerializer
from .models import Product, Category, Company, ProductSize, ProductSite, Comment, Image
from django.contrib.auth.models import User
from versatileimagefield.serializers import VersatileImageFieldSerializer


class CompanySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Company
        fields = ['pk', 'name', 'url']


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
            'products': ('products.ProductSerializer', {'many': True})
        }


class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']


class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name', 'content', 'created', 'update']
        expandable_fields = {
            'category': ('products.CategorySerializer', {'many': True}),
            'sites': ('products.ProductSiteSerializer', {'many': True}),
            'comments': ('products.CommentSerializer', {'many': True}),
            'image': ('products.ImageSerializer', {'many': True})
        }


class ProductSiteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSite
        fields = ['pk', 'name', 'price', 'url', 'created', 'updated']
        expandable_fields = {
            'product': 'products.ProductSerializer',
            'productsize': 'products.ProductSizeSerializer',
            'company': 'products.CompanySerializer',
        }


class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CommentSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'title', 'content', 'created', 'updated']
        expandable_fields = {
            'product': 'products.ProductSizeSerializer',
            'user': 'products.UserSerializer'
        }


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
            ('medium_square_crop', 'crop__400x400'),
            ('small_square_crop', 'crop__50x50')
        ]
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']
