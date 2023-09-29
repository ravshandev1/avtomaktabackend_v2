from rest_framework import serializers
from .models import Category, Car, Price, Percent


class PercentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percent
        fields = ['percent']


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['price', 'category']

    category = serializers.CharField(source='category.toifa')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['toifa']


class MoshinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'nomi']
