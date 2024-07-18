from rest_framework import serializers
from .models import Category, Product, Comment


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    class Meta:
        model = Product
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    product = ProductSerializers()
    class Meta:
        model = Comment
        fields = "__all__"