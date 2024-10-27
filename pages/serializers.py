from rest_framework import serializers
from .models import Product, Material, Warehouse, ProductMaterial


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'code']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'material', 'remainder', 'price']


class ProductMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()

    class Meta:
        model = ProductMaterial
        fields = ['material', 'quantity']
